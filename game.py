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
import socket
import getpass
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

from quests import QUESTS, RANKS, XP_PER_LEVEL, WORLD_NAMES, WORLD_PASSWORDS

console = Console()
HOME = str(Path.home())
SAVE_FILE = Path(HOME) / ".terminal-quest-save.json"
USERNAME = getpass.getuser()
HOSTNAME = socket.gethostname().split('.')[0]   # np. MacBook-Pro-Piotr (bez .local)
PROMPT = f"[bold green]{USERNAME}@{HOSTNAME}[/bold green] [cyan]~[/cyan]$ "


class BossDefeatError(Exception):
    """Raised gdy gracz traci wszystkie zycia w boss fighcie."""
    pass


# ── Stan gracza ────────────────────────────────────────────────────────────

class SaveState:
    def __init__(self):
        self.total_xp: int = 0
        self.completed: list[str] = []   # lista id ukonczonch questow
        self.rules_shown: bool = False   # czy zasady juz wyswietlone

    def save(self):
        SAVE_FILE.write_text(json.dumps({
            "total_xp": self.total_xp,
            "completed": self.completed,
            "rules_shown": self.rules_shown,
        }, indent=2))

    @classmethod
    def load(cls) -> "SaveState":
        s = cls()
        if SAVE_FILE.exists():
            try:
                data = json.loads(SAVE_FILE.read_text())
                s.total_xp = data.get("total_xp", 0)
                s.completed = data.get("completed", [])
                s.rules_shown = data.get("rules_shown", False)
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
    """Uruchamia komende w zsh, zwraca (stdout, stderr).
    fc -R laduje historie zeby builtin 'history' dzialal w subprocesie."""
    wrapped = f"fc -R ~/.zsh_history 2>/dev/null; {cmd}"
    result = subprocess.run(
        wrapped,
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
        f"[bold cyan]TYTUL:[/bold cyan] [italic]{tytul}[/italic]   "
        f"[bold cyan]USER:[/bold cyan] [dim]{USERNAME}@{HOSTNAME}[/dim]",
    ]
    return Panel("\n".join(lines), title="[bold]STATUS POSTACI[/bold]", border_style="blue", padding=(0, 1))


# ── UI: tabela teorii ──────────────────────────────────────────────────────

def print_theory_table(quest: dict):
    table = Table(box=box.ROUNDED, border_style="cyan", show_lines=True)
    table.add_column("Komenda", style="bold green", no_wrap=True)
    table.add_column("Co robi", style="white")
    table.add_column("Uwagi", style="dim yellow")

    for row in quest["theory"]:
        table.add_row(row.get("cmd", ""), row["what"], row.get("notes", ""))

    console.print(table)


# ── UI: ekran zasad ────────────────────────────────────────────────────────

def show_rules(state: SaveState):
    console.clear()
    rules_text = (
        f"[bold yellow]WITAJ W TERMINAL QUEST![/bold yellow]\n"
        f"[dim]Grasz jako: {USERNAME}@{HOSTNAME}[/dim]\n\n"
        "[bold cyan]JAK DZIALA GRA:[/bold cyan]\n"
        "  Kazdy [bold]Swiat[/bold] (np. Las Plikow, Kopalnia Potokow) to temat.\n"
        "  Swiat ma kilka [green]misji treningowych[/green] — cwiczysz bez kary.\n"
        "  Swiat konczy [red]Boss Fight[/red] — prawdziwy test wiedzy.\n\n"
        "[bold red]SYSTEM ZYCIA (Boss Fight):[/bold red]\n"
        "  Masz [bold]3 zycia[/bold] na Boss Fighcie.\n"
        "  Kazda bledna komenda = [red]-1 zycie[/red].\n"
        "  0 zyc = [bold red]BOSS POKONAT CIE[/bold red]!\n"
        "  Tracisz postep w biezacym i poprzednim swiecie.\n\n"
        "[bold yellow]HASLA ZAPISU:[/bold yellow]\n"
        "  Po ukonczeniu kazdego swiata dostajesz [bold]jednowyrazowe haslo[/bold].\n"
        "  Wpisz je w menu glownym (opcja [cyan]haslo[/cyan]) lub wprost\n"
        "  w prompt, by przeskakiwac do danego swiata.\n\n"
        "[bold green]EKWIPUNEK:[/bold green]\n"
        "  Wpisz [bold]e[/bold] w menu — zobaczysz poznane komendy z opisami.\n"
        "  [dim]Ekwipunek niedostepny podczas Boss Fightu![/dim]\n\n"
        "[bold cyan]SKROTY PODCZAS QUESTOW:[/bold cyan]\n"
        "  [bold]/hint[/bold]  — pokaz podpowiedz\n"
        "  [bold]/skip[/bold]  — pominij krok [dim](tylko w treningu)[/dim]\n"
    )
    console.print(Panel(rules_text, border_style="yellow", padding=(1, 2)))
    try:
        console.input("\n[dim]Nacisnij Enter zeby zaczac przygode...[/dim]")
    except (EOFError, KeyboardInterrupt):
        raise SystemExit(0)
    state.rules_shown = True
    state.save()


# ── UI: ekwipunek ──────────────────────────────────────────────────────────

def show_inventory(state: SaveState):
    console.clear()
    completed = set(state.completed)

    console.print(Panel(
        "[bold yellow]EKWIPUNEK — Poznane komendy[/bold yellow]\n"
        "[dim]Komendy z ukonczonych misji treningowych i boss fightow[/dim]",
        border_style="yellow",
        padding=(0, 1),
    ))
    console.print()

    completed_quests = [q for q in QUESTS if q["id"] in completed]

    if not completed_quests:
        console.print("  [dim]Ekwipunek pusty. Ukoncz pierwsze misje, by zdobyc komendy.[/dim]")
        console.print()
        try:
            console.input("[dim]Nacisnij Enter zeby wrocic...[/dim]")
        except (EOFError, KeyboardInterrupt):
            pass
        return

    worlds_done = sorted(set(q["world"] for q in completed_quests))

    for world_num in worlds_done:
        world_quests = [q for q in completed_quests if q["world"] == world_num]
        console.print(f"[bold yellow]── Swiat {world_num}: {WORLD_NAMES[world_num]} ──[/bold yellow]")

        table = Table(box=box.SIMPLE, show_lines=False, padding=(0, 1))
        table.add_column("Komenda", style="bold green", no_wrap=True, min_width=28)
        table.add_column("Co robi", style="white")
        table.add_column("Flagi / Uwagi", style="dim yellow")

        seen_cmds: set[str] = set()
        for quest in world_quests:
            for row in quest["theory"]:
                cmd = row.get("cmd", "")
                if cmd and cmd not in seen_cmds:
                    seen_cmds.add(cmd)
                    table.add_row(cmd, row["what"], row.get("notes", ""))

        console.print(table)
        console.print()

    try:
        console.input("[dim]Nacisnij Enter zeby wrocic do menu...[/dim]")
    except (EOFError, KeyboardInterrupt):
        pass


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

        has_boss = any(q.get("is_boss") for q in world_quests)
        boss_tag = "  [red][BOSS][/red]" if has_boss else ""

        # Pokaz haslo do tego swiata jezeli jest ukonczone
        pwd = WORLD_PASSWORDS.get(w)
        pwd_tag = f"  [dim]haslo: {pwd}[/dim]" if (done == total and total > 0 and pwd) else ""

        console.print(f"  [bold]Swiat {w}[/bold] — {WORLD_NAMES[w]:<30} {status}{boss_tag}{pwd_tag}")

    console.print()
    try:
        console.input("[dim]Nacisnij Enter zeby wrocic do menu...[/dim]")
    except (EOFError, KeyboardInterrupt):
        pass


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


# ── UI: ekran przegranej boss fight ────────────────────────────────────────

def show_boss_defeat(quest: dict, worlds_reset: list[int]):
    console.print()
    worlds_str = " i ".join(f"[yellow]Swiat {w}[/yellow]" for w in sorted(worlds_reset))
    console.print(Panel(
        f"[bold red]  ✗  BOSS POKONAT CIE!  ✗  [/bold red]\n\n"
        f"  Nie przetrwales Boss Fightu swiata [bold]{quest['world']}[/bold]!\n\n"
        f"  Tracisz postep w: {worlds_str}\n"
        f"  Wracasz do poprzedniego swiata...\n\n"
        f"  [dim]Przypomnij sobie lekcje i sprobuj ponownie.[/dim]",
        title="[bold red]⚔   GAME OVER   ⚔[/bold red]",
        border_style="red",
        padding=(1, 4),
    ))
    time.sleep(2)
    try:
        console.input("\n[dim]Nacisnij Enter zeby wrocic do menu...[/dim]")
    except (EOFError, KeyboardInterrupt):
        pass


# ── Krok treningu (unlimited retries) ─────────────────────────────────────

def run_shell_step(step: dict, step_num: int, total_steps: int, quest_id: str):
    """Obslugiuje krok treningowy — bez ograniczen prob."""
    expected = step["cmd"]
    hint = step.get("hint", "")
    description = step.get("description", "")

    while True:
        console.print()
        header = f"Krok {step_num}/{total_steps}"
        if description:
            body = f"[bold]{description}[/bold]\n\n[cyan]Wykonaj:[/cyan] [bold green]{expected}[/bold green]"
        else:
            body = f"[cyan]Wykonaj:[/cyan] [bold green]{expected}[/bold green]"
        if hint:
            body += f"\n[dim]Wskazowka: {hint}[/dim]"

        console.print(Panel(body, title=f"[bold]{header}[/bold]", border_style="cyan", padding=(0, 1)))

        try:
            user_input = console.input(PROMPT).strip()
        except (EOFError, KeyboardInterrupt):
            raise SystemExit(0)

        if user_input == "":
            continue

        if user_input == "/skip":
            console.print("[dim]Pomijam krok...[/dim]")
            output = step.get("output", "")
            if output:
                console.print(output)
            break

        if user_input == "/hint":
            console.print(f"[yellow]Podpowiedz:[/yellow] [bold]{expected}[/bold]")
            if hint:
                console.print(f"[dim]{hint}[/dim]")
            continue

        if cmd_matches(user_input, expected):
            output = step.get("output", "")
            if output:
                console.print(output)
            console.print("[bold green]✓ Poprawnie![/bold green]")
            time.sleep(0.4)
            break
        else:
            console.print(f"[red]Nie ta komenda. Sprobuj jeszcze raz.[/red]")
            console.print(f"[dim]Wpisz dokladnie: {expected}[/dim]")
            if hint:
                console.print(f"[dim]{hint}[/dim]")


# ── Krok boss fightu (3 zycia wspoldzielone miedzy krokami) ────────────────

def run_boss_shell_step(step: dict, step_num: int, total_steps: int, lives: list):
    """
    Obslugiuje krok boss fightu.
    lives = [int] — mutowalny kontener z liczba zyc wspoldzielonych miedzy krokami.
    Raises BossDefeatError gdy lives[0] <= 0.
    """
    expected = step["cmd"]
    hint = step.get("hint", "")
    description = step.get("description", "")

    while True:
        hearts = "[red]♥[/red]" * lives[0] + "[dim]♡[/dim]" * (3 - lives[0])
        header = f"BOSS  Krok {step_num}/{total_steps}  {hearts}"

        if description:
            body = f"[bold]{description}[/bold]\n\n[cyan]Wykonaj:[/cyan] [bold green]{expected}[/bold green]"
        else:
            body = f"[cyan]Wykonaj:[/cyan] [bold green]{expected}[/bold green]"
        if hint:
            body += f"\n[dim]Wskazowka: {hint}[/dim]"

        console.print()
        console.print(Panel(body, title=f"[bold red]{header}[/bold red]", border_style="red", padding=(0, 1)))

        try:
            user_input = console.input(PROMPT).strip()
        except (EOFError, KeyboardInterrupt):
            raise SystemExit(0)

        if user_input == "":
            continue

        if user_input == "/hint":
            console.print(f"[yellow]Podpowiedz:[/yellow] [bold]{expected}[/bold]")
            if hint:
                console.print(f"[dim]{hint}[/dim]")
            continue

        if user_input == "/skip":
            console.print("[bold red]⚔ /skip jest zablokowany podczas Boss Fightu![/bold red]")
            continue

        if cmd_matches(user_input, expected):
            output = step.get("output", "")
            if output:
                console.print(output)
            console.print("[bold green]✓ Poprawnie![/bold green]")
            time.sleep(0.4)
            break
        else:
            lives[0] -= 1
            if lives[0] <= 0:
                console.print("[bold red]✗ Bledna komenda! Tracisz ostatnie zycie![/bold red]")
                time.sleep(1.5)
                raise BossDefeatError()
            else:
                remaining = "[red]♥[/red]" * lives[0] + "[dim]♡[/dim]" * (3 - lives[0])
                console.print(f"[bold red]✗ Bledna komenda! Pozostale zycia: {remaining}[/bold red]")
                time.sleep(0.5)


def run_confirm_step(step: dict, step_num: int, total_steps: int):
    """Obslugiuje krok typu 'confirm' — pytanie T/N."""
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
            ans = console.input(PROMPT + "[dim](T/N)[/dim] ").strip().lower()
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


# ── Konsekwencja przegranej boss fight ─────────────────────────────────────

def apply_boss_defeat(state: SaveState, quest: dict) -> list[int]:
    """
    Usuwa postep w biezacym i poprzednim swiecie po przegranej boss fight.
    Zwraca liste numerow swiatow ktore zostaly zresetowane.
    """
    current_world = quest["world"]
    prev_world = current_world - 1

    worlds_to_reset: set[int] = {current_world}
    if prev_world >= 1:
        worlds_to_reset.add(prev_world)

    quests_to_remove = {q["id"] for q in QUESTS if q["world"] in worlds_to_reset}
    xp_lost = sum(q["xp"] for q in QUESTS
                  if q["id"] in state.completed and q["world"] in worlds_to_reset)

    state.completed = [qid for qid in state.completed if qid not in quests_to_remove]
    state.total_xp = max(0, state.total_xp - xp_lost)
    state.save()

    return sorted(worlds_to_reset)


# ── Pelny quest ────────────────────────────────────────────────────────────

def run_quest(quest: dict, state: SaveState):
    is_boss = quest.get("is_boss", False)

    console.clear()
    console.print(make_stats_panel(state))
    console.print()

    quest_type_label = "[bold red]⚔  BOSS FIGHT[/bold red]" if is_boss else "[bold cyan]Misja Treningowa[/bold cyan]"

    console.print(Panel(
        f"[bold]{quest['world_flavor']}[/bold]",
        title=f"[bold yellow]Swiat {quest['world']}: {quest['world_name']}[/bold yellow]",
        border_style="yellow",
        padding=(0, 1),
    ))
    console.print()

    console.print(f"{quest_type_label}   "
                  f"[bold cyan]Quest {quest['id']}: {quest['title']}[/bold cyan]   "
                  f"[dim]Nagroda: {quest['xp']} XP[/dim]")
    console.print()

    # ── Teoria ──
    console.print("[bold]── LEKCJA ──────────────────────────────────────────────────────[/bold]")
    print_theory_table(quest)
    console.print()

    if is_boss:
        console.print("[bold red]⚠  BOSS FIGHT: masz 3 zycia wspoldzielone miedzy krokami.[/bold red]")
        console.print("[dim]/hint — pokaz podpowiedz   /skip — zablokowany[/dim]")
        try:
            console.input("[dim]Przeczytaj powyzej, potem Enter zeby zaczac Boss Fight...[/dim]")
        except (EOFError, KeyboardInterrupt):
            raise SystemExit(0)
    else:
        console.print("[dim]/hint — pokaz podpowiedz   /skip — pominij krok[/dim]")
        try:
            console.input("[dim]Przeczytaj powyzej, potem Enter zeby zaczac cwiczenie...[/dim]")
        except (EOFError, KeyboardInterrupt):
            raise SystemExit(0)

    # ── Boss fight / cwiczenie ──
    boss = quest["boss"]
    border_color = "red" if is_boss else "cyan"
    title_color = "bold red" if is_boss else "bold cyan"

    console.print()
    console.print(Panel(
        f"[bold]{boss['description']}[/bold]",
        title=f"[{title_color}]⚔  {boss['title']}  ⚔[/{title_color}]",
        border_style=border_color,
        padding=(0, 1),
    ))
    if not is_boss:
        console.print("[dim]/hint — pokaz odpowiedz   /skip — pominij krok[/dim]")
    console.print()

    steps = boss["steps"]
    total = len(steps)
    lives = [3]   # mutowalny kontener — zycia wspoldzielone miedzy krokami boss fightu

    try:
        for i, step in enumerate(steps, 1):
            stype = step.get("type", "shell")
            if stype == "shell":
                if is_boss:
                    run_boss_shell_step(step, i, total, lives)
                else:
                    run_shell_step(step, i, total, quest["id"])
            elif stype == "confirm":
                run_confirm_step(step, i, total)
            elif stype == "info":
                run_info_step(step, i, total)
    except BossDefeatError:
        worlds_reset = apply_boss_defeat(state, quest)
        show_boss_defeat(quest, worlds_reset)
        return

    # ── Nagroda ──
    old_level = state.level
    state.total_xp += quest["xp"]
    state.completed.append(quest["id"])
    state.save()

    reward_lines = [
        f"[bold green]Quest ukonczony![/bold green]",
        f"  +{quest['xp']} XP   Lacznie: {state.total_xp} XP",
    ]

    # Po boss fighcie ujawnij haslo do nastepnego swiata
    if is_boss:
        next_world = quest["world"] + 1
        next_pwd = WORLD_PASSWORDS.get(next_world)
        if next_pwd:
            reward_lines.append(f"\n  [bold yellow]Haslo do Swiata {next_world}:[/bold yellow] [bold cyan]{next_pwd}[/bold cyan]")
            reward_lines.append(f"  [dim]Zapisz! Uzyj opcji 'haslo' w menu po resecie gry.[/dim]")

    console.print()
    console.print(Panel("\n".join(reward_lines), border_style="green", padding=(0, 1)))

    if state.level > old_level:
        print_level_up(state.level, state)

    try:
        console.input("\n[dim]Nacisnij Enter zeby wrocic do menu...[/dim]")
    except (EOFError, KeyboardInterrupt):
        raise SystemExit(0)


# ── Haslo zapisu ───────────────────────────────────────────────────────────

def apply_password(state: SaveState, password: str) -> tuple[bool, int | None]:
    """
    Sprawdza haslo i odblokowuje dostep do docelowego swiata.
    Haslo dla swiata N oznacza: wszystkie questy do swiata N-1 sa ukonczone.
    Zwraca (True, world_num) albo (False, None).
    """
    pwd = password.lower().strip()

    target_world = None
    for world_num, world_pwd in WORLD_PASSWORDS.items():
        if world_pwd == pwd:
            target_world = world_num
            break

    if target_world is None:
        return False, None

    xp_gained = 0
    for quest in QUESTS:
        if quest["world"] < target_world and quest["id"] not in state.completed:
            state.completed.append(quest["id"])
            xp_gained += quest["xp"]

    if xp_gained > 0:
        state.total_xp += xp_gained
        state.save()

    return True, target_world


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

    completed = set(state.completed)
    console.print("[bold]Dostepne questy:[/bold]")
    console.print()

    available = []
    for q in QUESTS:
        if q["id"] in completed:
            boss_tag = " [red][BOSS][/red]" if q.get("is_boss") else ""
            console.print(f"  [dim green]✓ {q['id']}: {q['title']} ({q['xp']} XP){boss_tag}[/dim green]")
        else:
            available.append(q)

    if not available:
        console.print("  [bold green]Wszystkie questy ukonczone! Jestes ARCYMISTRZEM![/bold green]")
    else:
        nq = available[0]
        nq_tag = " [red][BOSS FIGHT][/red]" if nq.get("is_boss") else " [cyan][TRENING][/cyan]"
        console.print(f"  [bold cyan]► {nq['id']}: {nq['title']} ({nq['xp']} XP){nq_tag}[/bold cyan]  [dim]← nastepny[/dim]")
        for q in available[1:4]:
            bt = " [red][BOSS][/red]" if q.get("is_boss") else ""
            console.print(f"  [dim]  {q['id']}: {q['title']}{bt}[/dim]")
        if len(available) > 4:
            console.print(f"  [dim]  ... i {len(available) - 4} wiecej[/dim]")

    console.print()
    console.print("[bold]Opcje:[/bold]")
    console.print("  [cyan]Enter[/cyan]   — kontynuuj (nastepny quest)")
    console.print("  [cyan]e[/cyan]       — ekwipunek (poznane komendy)")
    console.print("  [cyan]m[/cyan]       — mapa swiata")
    console.print("  [cyan]haslo[/cyan]   — wpisz haslo zapisu")
    console.print("  [cyan]r[/cyan]       — reset postaci")
    console.print("  [cyan]q[/cyan]       — wyjscie")
    console.print()

    try:
        choice = console.input("[bold]> [/bold]").strip().lower()
    except (EOFError, KeyboardInterrupt):
        return "q"
    return choice


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    state = SaveState.load()

    # Pokaz zasady przy pierwszym uruchomieniu
    if not state.rules_shown:
        console.clear()
        show_rules(state)

    while True:
        choice = print_main_menu(state)

        if choice in ("q", "quit", "exit"):
            console.print("[dim]Do zobaczenia, poszukiwaczu konsoli![/dim]")
            break

        elif choice == "m":
            print_world_map(state)

        elif choice == "e":
            show_inventory(state)

        elif choice == "haslo":
            console.print()
            try:
                pwd_input = console.input("[bold cyan]Wpisz haslo zapisu: [/bold cyan]").strip()
            except (EOFError, KeyboardInterrupt):
                continue
            success, target_world = apply_password(state, pwd_input)
            if success:
                console.print(f"[bold green]Haslo poprawne! Odblokowano dostep do Swiata {target_world}.[/bold green]")
                time.sleep(1.5)
            else:
                console.print("[red]Nieznane haslo.[/red]")
                time.sleep(1)

        elif choice == "r":
            console.print()
            try:
                confirm = console.input(
                    "[red]Na pewno resetowac postac? Stracisz caly postep! (tak/nie): [/red]"
                ).strip().lower()
            except (EOFError, KeyboardInterrupt):
                continue
            if confirm in ("tak", "t", "yes", "y"):
                state = SaveState()
                state.save()
                console.print("[yellow]Postac zresetowana.[/yellow]")
                time.sleep(1)

        else:
            completed = set(state.completed)
            available = [q for q in QUESTS if q["id"] not in completed]

            if not available:
                console.print("[bold green]Wszystkie questy ukonczone![/bold green]")
                time.sleep(1.5)
                continue

            # Sprawdz czy wpisano ID questa
            target = None
            for q in QUESTS:
                if q["id"] == choice:
                    target = q
                    break

            # Sprawdz czy wpisano haslo bezposrednio w promcie
            if target is None and choice and len(choice) >= 2 and choice not in ("m", "e", "r", "q"):
                success, target_world = apply_password(state, choice)
                if success:
                    console.print(f"[bold green]Haslo poprawne! Odblokowano Swiat {target_world}.[/bold green]")
                    time.sleep(1.5)
                    continue

            if target is None:
                target = available[0]

            run_quest(target, state)


if __name__ == "__main__":
    main()
