#!/usr/bin/env python3
"""
Terminal Quest — interaktywna gra RPG symulujaca terminal.
Uruchom: python3 ~/terminal-quest/game.py

Autor: Piotr Żabrowski
Licencja: MIT
"""

import sys
import subprocess
import json
import re
import os
import time
from pathlib import Path

# ── Auto-install rich ──────────────────────────────────────────────────────
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.progress import BarColumn, Progress, TextColumn
    from rich import box
except ImportError:
    print("Instalowanie rich (wymagane)...")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "rich", "--break-system-packages"],
        check=True,
    )
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.progress import BarColumn, Progress, TextColumn
    from rich import box

from quests import QUESTS, RANKS, XP_PER_LEVEL, WORLD_NAMES

console = Console()
HOME = str(Path.home())
SAVE_FILE = Path(HOME) / ".terminal-quest-save.json"


# ── Stan gracza ────────────────────────────────────────────────────────────

class SaveState:
    def __init__(self):
        self.total_xp: int = 0
        self.completed: list[str] = []  # lista id ukończonych questów

    def save(self):
        SAVE_FILE.write_text(json.dumps({
            "total_xp": self.total_xp,
            "completed": self.completed,
        }, indent=2))

    @classmethod
    def load(cls) -> "SaveState":
        s = cls()
        if SAVE_FILE.exists():
            try:
                data = json.loads(SAVE_FILE.read_text())
                s.total_xp = data.get("total_xp", 0)
                s.completed = data.get("completed", [])
            except Exception:
                pass
        return s

    @property
    def level(self) -> int:
        return min(30, 1 + self.total_xp // XP_PER_LEVEL)

    @property
    def rank(self) -> tuple[str, str]:
        for max_lvl, klasa, tytul in RANKS:
            if self.level <= max_lvl:
                return klasa, tytul
        return RANKS[-1][1], RANKS[-1][2]

    def xp_for_next_level(self) -> tuple[int, int]:
        """Zwraca (xp w biezacym levelu, xp potrzebne do nastepnego)."""
        current_level = self.level
        if current_level >= 30:
            return XP_PER_LEVEL, XP_PER_LEVEL
        level_start = (current_level - 1) * XP_PER_LEVEL
        xp_progress = self.total_xp - level_start
        return xp_progress, XP_PER_LEVEL


# ── Normalizacja komend ────────────────────────────────────────────────────

def normalize_cmd(cmd: str) -> str:
    """
    Normalizuje komende do porownania.
    - usuwa biale znaki z poczatku i konca
    - sortuje litery w flagach: ls -la == ls -al
    - zwija wiele spacji do jednej
    """
    tokens = cmd.strip().split()
    result = []
    for token in tokens:
        if re.match(r'^-[a-zA-Z]+$', token):
            token = '-' + ''.join(sorted(token[1:]))
        result.append(token)
    return ' '.join(result)


def cmd_matches(user_input: str, expected: str) -> bool:
    return normalize_cmd(user_input) == normalize_cmd(expected)


# ── Uruchamianie komend ────────────────────────────────────────────────────

def run_cmd(cmd: str) -> tuple[str, str]:
    """Uruchamia komende w zsh, zwraca (stdout, stderr)."""
    result = subprocess.run(
        cmd,
        shell=True,
        executable="/bin/zsh",
        capture_output=True,
        text=True,
        cwd=HOME,
    )
    return result.stdout, result.stderr


# ── UI: panel statystyk ────────────────────────────────────────────────────

def make_stats_panel(state: SaveState) -> Panel:
    klasa, tytul = state.rank
    xp_now, xp_max = state.xp_for_next_level()

    hp_bar = "█" * 10
    xp_filled = int((xp_now / xp_max) * 10)
    xp_bar = "█" * xp_filled + "░" * (10 - xp_filled)

    lines = [
        f"[bold cyan]HP:[/bold cyan]  [green]{hp_bar}[/green] 100/100   "
        f"[bold cyan]XP:[/bold cyan]  [yellow]{xp_bar}[/yellow] {xp_now}/{xp_max}",
        f"[bold cyan]LVL:[/bold cyan] [bold]{state.level}[/bold]   "
        f"[bold cyan]KLASA:[/bold cyan] [magenta]{klasa}[/magenta]",
        f"[bold cyan]TYTUL:[/bold cyan] [italic]{tytul}[/italic]",
    ]
    return Panel("\n".join(lines), title="[bold]STATUS POSTACI[/bold]", border_style="blue", padding=(0, 1))


# ── UI: tabela teorii ──────────────────────────────────────────────────────

def print_theory_table(quest: dict):
    table = Table(box=box.ROUNDED, border_style="cyan", show_lines=True)
    table.add_column("Komenda", style="bold green", no_wrap=True)
    table.add_column("Co robi", style="white")
    table.add_column("Uwagi", style="dim yellow")

    for row in quest["theory"]:
        table.add_row(row["cmd"], row["what"], row.get("notes", ""))

    console.print(table)


# ── UI: mapa swiata ────────────────────────────────────────────────────────

def print_world_map(state: SaveState):
    console.clear()
    console.print(Panel("[bold yellow]MAPA SWIATA[/bold yellow]", border_style="yellow"))
    console.print()

    completed_ids = set(state.completed)
    world_nums = sorted(WORLD_NAMES.keys())

    for w in world_nums:
        world_quests = [q for q in QUESTS if q["world"] == w]
        total = len(world_quests)
        done = sum(1 for q in world_quests if q["id"] in completed_ids)

        if done == total and total > 0:
            status = "[green]✓ UKONCZONE[/green]"
        elif done > 0:
            status = f"[yellow]w trakcie ({done}/{total})[/yellow]"
        else:
            status = "[dim]nieodkryte[/dim]"

        console.print(f"  [bold]Swiat {w}[/bold] — {WORLD_NAMES[w]:<30} {status}")

    console.print()
    console.input("[dim]Nacisnij Enter zeby wrocic do menu...[/dim]")


# ── UI: animacja level up ──────────────────────────────────────────────────

def print_level_up(new_level: int, state: SaveState):
    klasa, tytul = state.rank
    console.print()
    console.print(Panel(
        f"[bold yellow]  *** LEVEL UP! ***  [/bold yellow]\n\n"
        f"  Osiagnales poziom [bold cyan]{new_level}[/bold cyan]!\n"
        f"  Klasa: [magenta]{klasa}[/magenta]\n"
        f"  Tytul: [italic]{tytul}[/italic]",
        border_style="yellow",
        padding=(1, 4),
    ))
    time.sleep(1.5)


# ── Krok boss fighta ───────────────────────────────────────────────────────

def run_shell_step(step: dict, step_num: int, total_steps: int, quest_id: str):
    """Obslugiuje krok typu 'shell' — uzytkownik wpisuje komende."""
    expected = step["cmd"]
    hint = step.get("hint", "")
    description = step.get("description", "")

    while True:
        console.print()

        # Naglowek kroku
        header = f"Krok {step_num}/{total_steps}"
        if description:
            body = f"[bold]{description}[/bold]\n\n[cyan]Wykonaj:[/cyan] [bold green]{expected}[/bold green]"
        else:
            body = f"[cyan]Wykonaj:[/cyan] [bold green]{expected}[/bold green]"
        if hint:
            body += f"\n[dim]Wskazowka: {hint}[/dim]"

        console.print(Panel(body, title=f"[bold]{header}[/bold]", border_style="cyan", padding=(0, 1)))

        # Prompt terminala
        try:
            user_input = console.input(f"[bold green]zenon@quest ~$[/bold green] ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[yellow]Przerywam...[/yellow]")
            raise SystemExit(0)

        if user_input == "":
            continue

        # Specjalne komendy debugowe
        if user_input == "/skip":
            console.print("[dim]Pomijam krok...[/dim]")
            # Nie uruchamiamy komendy ale przechodzimy dalej
            stdout, stderr = run_cmd(expected)
            if stdout:
                console.print(stdout, end="")
            break

        if user_input == "/hint":
            console.print(f"[yellow]Podpowiedz:[/yellow] {expected}")
            if hint:
                console.print(f"[dim]{hint}[/dim]")
            continue

        # Sprawdz czy komenda pasuje
        if cmd_matches(user_input, expected):
            stdout, stderr = run_cmd(user_input)
            if stdout:
                console.print(stdout, end="")
            if stderr:
                console.print(f"[dim red]{stderr}[/dim red]", end="")
            console.print("[bold green]✓ Poprawnie![/bold green]")
            time.sleep(0.4)
            break
        else:
            console.print(f"[red]Nie ta komenda.[/red]")
            console.print(f"[dim]Wskazowka: {expected}[/dim]")
            if hint:
                console.print(f"[dim]{hint}[/dim]")


def run_confirm_step(step: dict, step_num: int, total_steps: int):
    """Obslugiuje krok typu 'confirm' — pytanie Y/N."""
    prompt = step.get("prompt", "Czy jestes gotowy?")
    console.print()
    console.print(Panel(
        f"[bold]{prompt}[/bold]",
        title=f"[bold]Krok {step_num}/{total_steps}[/bold]",
        border_style="cyan",
        padding=(0, 1),
    ))
    while True:
        try:
            ans = console.input("[bold green]zenon@quest ~$[/bold green] [dim](T/N)[/dim] ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            raise SystemExit(0)
        if ans in ("t", "y", "tak", "yes"):
            console.print("[bold green]✓ Swietnie![/bold green]")
            break
        elif ans in ("n", "nie", "no"):
            console.print("[yellow]Wróc kiedy bedziesz gotowy![/yellow]")
        else:
            console.print("[dim]Wpisz T (tak) lub N (nie)[/dim]")


def run_info_step(step: dict, step_num: int, total_steps: int):
    """Obslugiuje krok typu 'info' — wyswietla informacje, Enter dalej."""
    text = step.get("text", "")
    console.print()
    console.print(Panel(
        text,
        title=f"[bold]Krok {step_num}/{total_steps} — Informacja[/bold]",
        border_style="blue",
        padding=(0, 1),
    ))
    try:
        console.input("[dim]Nacisnij Enter zeby kontynuowac...[/dim]")
    except (EOFError, KeyboardInterrupt):
        raise SystemExit(0)


# ── Pelny quest ────────────────────────────────────────────────────────────

def run_quest(quest: dict, state: SaveState):
    console.clear()
    console.print(make_stats_panel(state))
    console.print()

    # Naglowek swiata
    console.print(Panel(
        f"[bold]{quest['world_flavor']}[/bold]",
        title=f"[bold yellow]Swiat {quest['world']}: {quest['world_name']}[/bold yellow]",
        border_style="yellow",
        padding=(0, 1),
    ))
    console.print()

    # Tytuł questa
    console.print(f"[bold cyan]Quest {quest['id']}: {quest['title']}[/bold cyan]   "
                  f"[dim]Nagroda: {quest['xp']} XP[/dim]")
    console.print()

    # ── Teoria ──
    console.print("[bold]── LEKCJA ──────────────────────────────────────────────────────[/bold]")
    print_theory_table(quest)
    console.print()
    try:
        console.input("[dim]Przeczytaj tablice powyzej, potem nacisnij Enter zeby zaczac Boss Fight...[/dim]")
    except (EOFError, KeyboardInterrupt):
        raise SystemExit(0)

    # ── Boss fight ──
    boss = quest["boss"]
    console.print()
    console.print(Panel(
        f"[bold]{boss['description']}[/bold]",
        title=f"[bold red]⚔  {boss['title']}  ⚔[/bold red]",
        border_style="red",
        padding=(0, 1),
    ))
    console.print("[dim]/hint — pokaz odpowiedz   /skip — pominij krok[/dim]")
    console.print()

    steps = boss["steps"]
    total = len(steps)

    for i, step in enumerate(steps, 1):
        stype = step.get("type", "shell")
        if stype == "shell":
            run_shell_step(step, i, total, quest["id"])
        elif stype == "confirm":
            run_confirm_step(step, i, total)
        elif stype == "info":
            run_info_step(step, i, total)

    # ── Nagroda ──
    old_level = state.level
    state.total_xp += quest["xp"]
    state.completed.append(quest["id"])
    state.save()

    console.print()
    console.print(Panel(
        f"[bold green]Quest ukończony![/bold green]\n"
        f"  +{quest['xp']} XP\n"
        f"  Lacznie XP: {state.total_xp}",
        border_style="green",
        padding=(0, 1),
    ))

    if state.level > old_level:
        print_level_up(state.level, state)

    try:
        console.input("\n[dim]Nacisnij Enter zeby wrocic do menu...[/dim]")
    except (EOFError, KeyboardInterrupt):
        raise SystemExit(0)


# ── Menu glowne ────────────────────────────────────────────────────────────

def print_main_menu(state: SaveState) -> str:
    console.clear()
    console.print(make_stats_panel(state))
    console.print()

    console.print(Panel(
        "[bold yellow]TERMINAL QUEST[/bold yellow]\n"
        "[dim]Interaktywna gra RPG — ucz sie terminala walczac z bossami[/dim]",
        border_style="yellow",
        padding=(0, 2),
    ))
    console.print()

    # Lista questów — pokaż aktualny i ukończone
    completed = set(state.completed)
    console.print("[bold]Dostepne questy:[/bold]")
    console.print()

    available = []
    for q in QUESTS:
        if q["id"] in completed:
            console.print(f"  [dim green]✓ Quest {q['id']}: {q['title']} ({q['xp']} XP)[/dim green]")
        else:
            available.append(q)

    if not available:
        console.print("  [bold green]Wszystkie questy ukonczone! Jestes ARCYMISTRZEM![/bold green]")
    else:
        next_q = available[0]
        console.print(f"  [bold cyan]► Quest {next_q['id']}: {next_q['title']} ({next_q['xp']} XP)[/bold cyan]  [dim]← nastepny[/dim]")
        for q in available[1:4]:
            console.print(f"  [dim]  Quest {q['id']}: {q['title']}[/dim]")
        if len(available) > 4:
            console.print(f"  [dim]  ... i {len(available) - 4} wiecej[/dim]")

    console.print()
    console.print("[bold]Opcje:[/bold]")
    console.print("  [cyan]Enter[/cyan]  — kontynuuj (nastepny quest)")
    console.print("  [cyan]m[/cyan]      — mapa swiata")
    console.print("  [cyan]r[/cyan]      — reset postaci")
    console.print("  [cyan]q[/cyan]      — wyjscie")
    console.print()

    try:
        choice = console.input("[bold]> [/bold]").strip().lower()
    except (EOFError, KeyboardInterrupt):
        return "q"
    return choice


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    state = SaveState.load()

    while True:
        choice = print_main_menu(state)

        if choice in ("q", "quit", "exit"):
            console.print("[dim]Do zobaczenia, poszukiwaczu konsoli![/dim]")
            break

        elif choice == "m":
            print_world_map(state)

        elif choice == "r":
            console.print()
            try:
                confirm = console.input("[red]Na pewno resetowac postac? Stracisz cały postep! (tak/nie): [/red]").strip().lower()
            except (EOFError, KeyboardInterrupt):
                continue
            if confirm in ("tak", "t", "yes", "y"):
                state = SaveState()
                state.save()
                console.print("[yellow]Postac zresetowana.[/yellow]")
                time.sleep(1)

        else:
            # Enter lub cokolwiek innego → kontynuuj
            completed = set(state.completed)
            available = [q for q in QUESTS if q["id"] not in completed]

            if not available:
                console.print("[bold green]Wszystkie questy ukonczone![/bold green]")
                time.sleep(1.5)
                continue

            # Sprawdź czy wpisano numer questa
            target = None
            for q in QUESTS:
                if q["id"] == choice:
                    target = q
                    break

            if target is None:
                target = available[0]

            run_quest(target, state)


if __name__ == "__main__":
    main()
