"""
Terminal Quest — dane wszystkich questów.

Autor: Piotr Żabrowski
Licencja: MIT
"""

import socket
import getpass
from pathlib import Path

HOME = str(Path.home())
QP = f"{HOME}/quest-project"                    # skrót do ~/quest-project
USERNAME = getpass.getuser()                    # np. zenon
HOSTNAME = socket.gethostname().split('.')[0]   # np. MacBook-Pro-Piotr

# ── Rangi ─────────────────────────────────────────────────────────────────
# (max_level, klasa, tytul)
RANKS = [
    (3,  "Nowicjusz Powloki",    "Zagubiony w Shellu"),
    (6,  "Wedrowiec Konsoli",    "Poszukiwacz Plikow"),
    (9,  "Wladca Potokow",       "Lacznik Komend"),
    (12, "Mage Edycji",          "Oswojony z Vimem"),
    (15, "Straznik Bram",        "Pan Uprawnien"),
    (18, "Pogromca Procesow",    "Zabojca Zombie"),
    (22, "Kowal Skryptow",       "Tworca Automatyzacji"),
    (25, "Sieciowy Mag",         "Podroznik SSH"),
    (28, "Wladca Repozytoriow",  "Mistrz Gita"),
    (30, "ARCYMISTRZ TERMINALA", "Legenda Konsoli"),
]

XP_PER_LEVEL = 20  # level 30 przy ~580 XP (suma wszystkich questów ≈ 580)

WORLD_NAMES = {
    0:  "Przygotowanie macOS",
    1:  "Wioska Startowa",
    2:  "Las Plikow",
    3:  "Kopalnia Potokow",
    4:  "Wieza Edytora",
    5:  "Twierdza Uprawnien",
    6:  "Labirynt Procesow",
    7:  "Kuznia Skryptow",
    8:  "Swiatynia Sieci",
    9:  "Otchlan Gita",
    10: "Tron Arcymistrza",
}

# ── Hasla zapisu ──────────────────────────────────────────────────────────
# Klucz = numer swiata do ktorego haslo przenosi (odblokuje swiaty 0..N-1).
# Hasla ujawniane sa po ukonczeniu boss fightu poprzedniego swiata.
WORLD_PASSWORDS = {
    1:  "wioska",    # odblokuj swiat 1 (pominij swiat 0)
    2:  "las",       # odblokuj swiat 2
    3:  "kopalnia",  # odblokuj swiat 3
    4:  "wieza",     # odblokuj swiat 4
    5:  "twierdza",  # odblokuj swiat 5
    6:  "labirynt",  # odblokuj swiat 6
    7:  "kuznia",    # odblokuj swiat 7
    8:  "swiatynia", # odblokuj swiat 8
    9:  "otchlan",   # odblokuj swiat 9
    10: "tron",      # odblokuj swiat 10
}

# ── Questy ────────────────────────────────────────────────────────────────
# is_boss=True  → boss fight z systemem zyc (3 zycia wspoldzielone miedzy krokami)
# is_boss=False → misja treningowa (nieograniczone proby, /skip dostepny)
QUESTS = [

    # ══════════════════════════════════════════════════════════════════════
    # SWIAT 0: PRZYGOTOWANIE
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "0.1",
        "world": 0,
        "is_boss": False,
        "world_name": "Przygotowanie macOS",
        "world_flavor": "Kazdy wojownik potrzebuje dobrego ekwipunku. Upewnijmy sie ze masz wszystko.",
        "title": "Homebrew — menedzer pakietow",
        "xp": 10,
        "theory": [
            {"cmd": "brew install nazwa",     "what": "Zainstaluj program",           "notes": "np. brew install git"},
            {"cmd": "brew uninstall nazwa",   "what": "Odinstaluj program",           "notes": ""},
            {"cmd": "brew list",              "what": "Co mam zainstalowane?",        "notes": ""},
            {"cmd": "brew update",            "what": "Aktualizuj liste pakietow",    "notes": ""},
            {"cmd": "brew upgrade",           "what": "Aktualizuj wszystkie pakiety", "notes": ""},
            {"cmd": "brew install --cask app","what": "Zainstaluj aplikacje GUI",     "notes": "np. iterm2, vscode"},
        ],
        "boss": {
            "title": "CWICZENIE 0.1 — Ekwipunek",
            "description": "Sprawdz czy Homebrew i Git sa zainstalowane:",
            "steps": [
                {"type": "shell", "cmd": "brew --version",
                 "hint": "Powinnas zobaczyc 'Homebrew X.Y.Z'"},
                {"type": "shell", "cmd": "git --version",
                 "hint": "Powinnas zobaczyc 'git version X.Y.Z'"},
            ],
        },
    },

    # ══════════════════════════════════════════════════════════════════════
    # SWIAT 1: WIOSKA STARTOWA
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "1.1",
        "world": 1,
        "is_boss": False,
        "world_name": "Wioska Startowa",
        "world_flavor": "Budzisz sie w terminalu. Migajacy kursor czeka na twoj pierwszy rozkaz...",
        "title": "Pierwsze kroki",
        "xp": 15,
        "theory": [
            {"cmd": "pwd",        "what": "Gdzie jestem? (Print Working Directory)",        "notes": f"pwd -> {HOME}"},
            {"cmd": "ls",         "what": "Co tu jest? Listuje pliki w katalogu",           "notes": ""},
            {"cmd": "ls -la",     "what": "Pokaz WSZYSTKO z detalami",                      "notes": "-l = szczegoly  -a = ukryte pliki (zaczynaja sie od .)"},
            {"cmd": "cd katalog", "what": "Idz do katalogu (Change Directory)",             "notes": "sciezka wzgledna: cd Documents  absolutna: cd /etc"},
            {"cmd": "cd ..",      "what": "Cofnij sie o jeden katalog w gore",              "notes": ".. = katalog nadrzedny"},
            {"cmd": "cd ~",       "what": f"Wroc do domu ({HOME})",                        "notes": "~ to zawsze skrot do twojego home"},
            {"cmd": "cd -",       "what": "Wroc tam gdzie bylem ostatnio",                 "notes": "Skakaj miedzy dwoma miejscami"},
            {"cmd": "clear",      "what": "Wyczysc ekran",                                 "notes": "Ctrl+L dziala tak samo"},
        ],
        "boss": {
            "title": "CWICZENIE 1.1 — Nawigator",
            "description": "Nawiguj przez 5 katalogow i wroc do domu:",
            "steps": [
                {"type": "shell", "cmd": "cd /tmp",
                 "hint": "/tmp = pliki tymczasowe, czyszczone po restarcie"},
                {"type": "shell", "cmd": "cd /var/log",
                 "hint": "/var/log = logi systemowe"},
                {"type": "shell", "cmd": "cd /usr/local",
                 "hint": "/usr/local = tu Homebrew instaluje programy"},
                {"type": "shell", "cmd": "cd /etc",
                 "hint": "/etc = konfiguracja systemu"},
                {"type": "shell", "cmd": "cd ~/Documents",
                 "hint": "~/Documents = twoj folder Dokumenty"},
                {"type": "shell", "cmd": "cd ~",
                 "hint": "Wroc do katalogu domowego"},
                {"type": "shell", "cmd": "pwd",
                 "hint": f"Powinienes zobaczyc {HOME}"},
            ],
        },
    },

    {
        "id": "1.2",
        "world": 1,
        "is_boss": False,
        "world_name": "Wioska Startowa",
        "world_flavor": "Czas poznac swoj system i dowiedziec sie kim jestes.",
        "title": "Rozpoznanie terenu",
        "xp": 15,
        "theory": [
            {"cmd": "whoami",       "what": "Kim jestem? Wypisuje nazwe uzytkownika",      "notes": f"Twoj: {USERNAME}"},
            {"cmd": "date",         "what": "Aktualna data i czas",                        "notes": "date '+%Y-%m-%d' = tylko data"},
            {"cmd": "cal",          "what": "Kalendarz miesiezny",                         "notes": "cal 2026 = caly rok"},
            {"cmd": "uname -a",     "what": "Info o systemie (OS, kernel, architektura)",  "notes": "-a = all. arm64 = Apple Silicon"},
            {"cmd": "echo 'tekst'", "what": "Wypisz tekst na ekran",                       "notes": "echo $HOME = wartosc zmiennej"},
            {"cmd": "history",      "what": "Historia ostatnich komend",                   "notes": "history | grep git = tylko komendy z git"},
            {"cmd": "man ls",       "what": "Manual (dokumentacja) komendy",               "notes": "/ = szukaj  n = nastepny  q = wyjscie"},
        ],
        "boss": {
            "title": "CWICZENIE 1.2 — Wywiad",
            "description": "Odpowiedz na pytania uzywajac komend terminala:",
            "steps": [
                {"type": "shell", "cmd": "whoami",
                 "hint": f"Wypisuje nazwe uzytkownika — powinno byc: {USERNAME}"},
                {"type": "shell", "cmd": "date",
                 "hint": "Pokazuje dzisiejszy dzien tygodnia i godzine"},
                {"type": "shell", "cmd": "uname -a",
                 "hint": "Pokazuje system i architekture (arm64 = Apple Silicon)"},
                {"type": "shell", "cmd": "history",
                 "hint": "Lista ostatnich komend"},
            ],
        },
    },

    {
        "id": "1.3",
        "world": 1,
        "is_boss": True,
        "world_name": "Wioska Startowa",
        "world_flavor": "Skroty to roznica miedzy nowicjuszem a wojownikiem.",
        "title": "Skroty klawiszowe",
        "xp": 20,
        "theory": [
            {"cmd": "Tab",         "what": "AUTOUZUPELNIANIE — najwazniejszy skrot",  "notes": "Dwa razy Tab = pokaz mozliwosci"},
            {"cmd": "Ctrl+C",      "what": "Przerwij biezaca komende",                "notes": "Wysyla SIGINT do procesu"},
            {"cmd": "Ctrl+R",      "what": "Szukaj w historii komend",                "notes": "Wpisz fragment, Enter = wykonaj"},
            {"cmd": "Ctrl+L",      "what": "Wyczysc ekran",                           "notes": "To samo co clear"},
            {"cmd": "Ctrl+A",      "what": "Skocz na poczatek linii",                 "notes": ""},
            {"cmd": "Ctrl+E",      "what": "Skocz na koniec linii",                   "notes": "A jak poczAtek, E jak End"},
            {"cmd": "Ctrl+W",      "what": "Usun slowo w lewo",                       "notes": "Szybsze niz trzymanie Backspace"},
            {"cmd": "Ctrl+U",      "what": "Usun cala linie",                         "notes": ""},
            {"cmd": "!!",          "what": "Powtorz ostatnia komende",                "notes": "Czesto: sudo !!"},
            {"cmd": "strzalka UP", "what": "Poprzednia komenda w historii",           "notes": "DOWN = nastepna"},
        ],
        "boss": {
            "title": "BOSS FIGHT 1.3 — Mistrz Skrotow",
            "description": "Pokaz ze opanowales skroty i nawigacje:",
            "steps": [
                {"type": "shell", "cmd": "echo 'test Ctrl+A i Ctrl+E'",
                 "hint": "Wpisz komende, uzyj Ctrl+A zeby skoczyc na poczatek, Ctrl+E na koniec"},
                {"type": "shell", "cmd": "history | tail -5",
                 "hint": "Pokaz ostatnie 5 komend z historii"},
                {"type": "confirm",
                 "prompt": "Czy udalo ci sie przerwac komende przez Ctrl+C i wyszukac cos przez Ctrl+R?"},
            ],
        },
    },

    # ══════════════════════════════════════════════════════════════════════
    # SWIAT 2: LAS PLIKOW
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "2.1",
        "world": 2,
        "is_boss": False,
        "world_name": "Las Plikow",
        "world_flavor": "Wkraczasz w gesty las plikow i katalogow. Musisz nauczyc sie nimi wladac.",
        "title": "Tworzenie i niszczenie",
        "xp": 20,
        "theory": [
            {"cmd": "touch plik.txt",     "what": "Stworz pusty plik",                    "notes": "Jesli plik istnieje — tylko aktualizuje date"},
            {"cmd": "mkdir folder",       "what": "Stworz katalog",                        "notes": ""},
            {"cmd": "mkdir -p a/b/c",     "what": "Stworz zagniezdzone katalogi",          "notes": "-p = parents: tworzy wszystkie brakujace katalogi"},
            {"cmd": "cp zrodlo cel",      "what": "Kopiuj plik",                           "notes": "Jesli cel istnieje — nadpisuje bez pytania!"},
            {"cmd": "cp -r folder kopia", "what": "Kopiuj caly katalog",                   "notes": "-r = recursive: kopiuj z cala zawartoscia"},
            {"cmd": "mv stary nowy",      "what": "Przenies lub zmien nazwe",              "notes": "Ta sama komenda robi obie rzeczy"},
            {"cmd": "rm plik",            "what": "USUN plik (NIEODWRACALNE!)",            "notes": "Brak Kosza — rm usuwa na zawsze"},
            {"cmd": "rm -r folder",       "what": "USUN katalog z zawartoscia",            "notes": "-r = recursive: wejdz i usun wszystko w srodku"},
            {"cmd": "rmdir folder",       "what": "Usun PUSTY katalog",                    "notes": "Bezpieczniejsze — odmowi jesli nie pusty"},
        ],
        "boss": {
            "title": "CWICZENIE 2.1 — Budowniczy i Niszczyciel",
            "description": "Zbuduj strukture projektu, sprawdz i posprzataj:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}/{{src/utils,docs,tests}}",
                 "hint": "-p = parents  {..} = brace expansion: 3 katalogi naraz"},
                {"type": "shell", "cmd": f"touch {QP}/src/main.sh",
                 "hint": "touch = stworz pusty plik  .sh = skrypt"},
                {"type": "shell", "cmd": f"touch {QP}/src/utils/helpers.sh",
                 "hint": "funkcje pomocnicze"},
                {"type": "shell", "cmd": f"touch {QP}/docs/README.md",
                 "hint": "dokumentacja  .md = markdown"},
                {"type": "shell", "cmd": f"touch {QP}/tests/test_main.sh",
                 "hint": "plik testow"},
                {"type": "shell", "cmd": f"ls -R {QP}",
                 "hint": "-R = recursive: pokazuje zawartosc wszystkich podkatalogow"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "-r = recursive: usuwa katalog razem z cala zawartoscia"},
                {"type": "shell", "cmd": f"ls ~ | grep quest-project",
                 "hint": "brak outputu = sukces, folder zniknal"},
            ],
        },
    },

    {
        "id": "2.2",
        "world": 2,
        "is_boss": False,
        "world_name": "Las Plikow",
        "world_flavor": "Nie otwieraj duzych plikow w cat — zaflooduje terminal.",
        "title": "Czytanie plikow",
        "xp": 20,
        "theory": [
            {"cmd": "cat plik",        "what": "Pokaz cala zawartosc pliku",           "notes": "Uzyj tylko dla malych plikow (do ~50 linii)"},
            {"cmd": "less plik",       "what": "Przegladarka plikow",                  "notes": "strzalki/PageUp/Down  /szukaj  n=nastepny  q=wyjscie"},
            {"cmd": "head -n 10 plik", "what": "Pierwsze 10 linii",                   "notes": "-n = ile linii. Domyslnie 10"},
            {"cmd": "tail -n 10 plik", "what": "Ostatnie 10 linii",                   "notes": "-n = ile linii. Domyslnie 10"},
            {"cmd": "tail -f plik",    "what": "Sledz plik na zywo",                  "notes": "-f = follow. Ctrl+C zeby zatrzymac"},
            {"cmd": "wc -l plik",      "what": "Policz linie",                        "notes": "wc bez flag = linie slowa bajty"},
            {"cmd": "wc -w plik",      "what": "Policz slowa",                        "notes": "-c = bajty"},
            {"cmd": "diff plik1 plik2","what": "Porownaj dwa pliki",                  "notes": "< = tylko w pierwszym  > = tylko w drugim"},
        ],
        "boss": {
            "title": "CWICZENIE 2.2 — Czytacz",
            "description": "Stworz plik z 100 liniami i przeanalizuj go:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "stworz folder na pliki"},
                {"type": "shell", "cmd": f"seq 1 100 > {QP}/numbers.txt",
                 "hint": "seq 1 100 = generuj liczby 1-100  > = zapisz do pliku"},
                {"type": "shell", "cmd": f"wc -l {QP}/numbers.txt",
                 "hint": "Ile linii ma plik?"},
                {"type": "shell", "cmd": f"head -n 5 {QP}/numbers.txt",
                 "hint": "Pierwsze 5 linii"},
                {"type": "shell", "cmd": f"tail -n 3 {QP}/numbers.txt",
                 "hint": "Ostatnie 3 linie"},
                {"type": "shell", "cmd": f"head -n 55 {QP}/numbers.txt | tail -n 11",
                 "hint": "Linie 45-55: head bierze pierwsze 55, tail bierze ostatnie 11 z tych 55"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj"},
                {"type": "shell", "cmd": f"ls ~ | grep quest-project",
                 "hint": "brak outputu = sukces"},
            ],
        },
    },

    {
        "id": "2.3",
        "world": 2,
        "is_boss": True,
        "world_name": "Las Plikow",
        "world_flavor": "find = szukaj plikow. grep = szukaj tekstu wewnatrz plikow. Dwa rozne narzedzia.",
        "title": "Wyszukiwanie",
        "xp": 25,
        "theory": [
            {"cmd": "find . -name '*.txt'",  "what": "Znajdz pliki po nazwie",            "notes": ". = tutaj  * = dowolny ciag znakow"},
            {"cmd": "find . -type d",        "what": "Znajdz tylko katalogi",             "notes": "-type f = plik  -type l = link"},
            {"cmd": "find . -size +1M",      "what": "Znajdz pliki wieksze niz 1MB",      "notes": "+1M = wieksze  -1M = mniejsze  jednostki: k, M, G"},
            {"cmd": "grep 'tekst' plik",     "what": "Szukaj tekstu w pliku",             "notes": "Wypisuje linie zawierajace wzorzec"},
            {"cmd": "grep -r 'tekst' .",     "what": "Szukaj rekurencyjnie w katalogu",   "notes": "-r = recursive: przeszukaj podkatalogi"},
            {"cmd": "grep -i 'tekst' plik",  "what": "Szukaj (ignoruj wielkosc liter)",   "notes": "-i = ignore case"},
            {"cmd": "grep -n 'tekst' plik",  "what": "Szukaj z numerami linii",           "notes": "-n = numery linii przy wynikach"},
            {"cmd": "which python3",         "what": "Gdzie jest zainstalowany program?", "notes": "Pokazuje pelna sciezke: /usr/bin/python3"},
        ],
        "boss": {
            "title": "BOSS FIGHT 2.3 — Tropiciel",
            "description": "Stworz projekt z trescia i przeszukaj go:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}/{{src/utils,docs,tests}}",
                 "hint": "stworz strukture katalogow"},
                {"type": "shell",
                 "cmd": f"echo $'TODO: fix bug\\nDONE: add feature\\nTODO: write tests' > {QP}/src/main.sh",
                 "hint": "$'...' = skladnia zsh dla \\n (nowa linia)"},
                {"type": "shell",
                 "cmd": f"echo $'# Helper functions\\nTODO: implement helpers' > {QP}/src/utils/helpers.sh",
                 "hint": "drugi plik z trescia"},
                {"type": "shell", "cmd": f"find {QP} -name '*.sh'",
                 "hint": "Znajdz wszystkie pliki .sh w projekcie"},
                {"type": "shell", "cmd": f"grep -r 'TODO' {QP}",
                 "hint": "-r = przeszukaj wszystkie podkatalogi"},
                {"type": "shell", "cmd": f"grep -r 'TODO' {QP} | wc -l",
                 "hint": "| wc -l = policz ile linii wynikow zwrocil grep"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj"},
                {"type": "shell", "cmd": f"ls ~ | grep quest-project",
                 "hint": "brak outputu = sukces"},
            ],
        },
    },

    # ══════════════════════════════════════════════════════════════════════
    # SWIAT 3: KOPALNIA POTOKOW
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "3.1",
        "world": 3,
        "is_boss": False,
        "world_name": "Kopalnia Potokow",
        "world_flavor": "Pipe | to serce filozofii Unixa. Kazdy program robi JEDNA rzecz dobrze. Laczysz je w lancuchy.",
        "title": "Pipe — laczenie komend",
        "xp": 25,
        "theory": [
            {"cmd": "ls -la | less",                 "what": "Ogromna lista → przewijalna",        "notes": "| przekazuje stdout dalej jako stdin"},
            {"cmd": "ls -la | wc -l",                "what": "Ile plikow jest w katalogu?",        "notes": ""},
            {"cmd": "ls -la | grep '.txt'",          "what": "Tylko pliki .txt z listy",           "notes": ""},
            {"cmd": "ls -la | sort -k5 -n",          "what": "Posortuj po rozmiarze",              "notes": "-k5 = 5. kolumna (rozmiar)  -n = numerycznie"},
            {"cmd": "history | grep 'cd' | tail -5", "what": "Ostatnie 5 komend z cd",            "notes": "Lancuch 3 komend!"},
            {"cmd": "ps aux | grep chrome | wc -l",  "what": "Ile procesow chrome dziala?",       "notes": ""},
        ],
        "boss": {
            "title": "CWICZENIE 3.1 — Lacznik",
            "description": "Polacz komendy pipe'em:",
            "steps": [
                {"type": "shell", "cmd": "ls -la ~ | wc -l",
                 "hint": "Ile plikow/katalogow jest w twoim home?"},
                {"type": "shell", "cmd": "ls -la ~ | sort -k5 -rn | head -5",
                 "hint": "5 najwiekszych elementow w home  -r = odwrotnie"},
                {"type": "shell", "cmd": "history | grep 'cd' | wc -l",
                 "hint": "Ile razy uzywales komendy cd?"},
            ],
        },
    },

    {
        "id": "3.2",
        "world": 3,
        "is_boss": False,
        "world_name": "Kopalnia Potokow",
        "world_flavor": "Kazda komenda ma 3 strumienie: stdin, stdout, stderr. Przekierowania zmieniaja dokad ida.",
        "title": "Przekierowania",
        "xp": 25,
        "theory": [
            {"cmd": ">",   "what": "Zapisz stdout do pliku (NADPISUJE!)",  "notes": "Jesli plik istnieje — nadpisuje bez pytania"},
            {"cmd": ">>",  "what": "Dopisz do pliku",                      "notes": "Bezpieczne — nie niszczy istniejacych danych"},
            {"cmd": "<",   "what": "Wczytaj z pliku jako stdin",           "notes": "sort < lista.txt = to samo co sort lista.txt"},
            {"cmd": "2>",  "what": "Przekieruj stderr (bledy)",            "notes": "/dev/null = wirtualny kosz, dane znikaja"},
            {"cmd": "&>",  "what": "Przekieruj stdout I stderr razem",     "notes": "Skrot dla > plik 2>&1"},
            {"cmd": "tee", "what": "Wyswietl I zapisz jednoczesnie",       "notes": "Jak rozgaleznik — dane ida i na ekran i do pliku"},
        ],
        "boss": {
            "title": "CWICZENIE 3.2 — Przekierowania",
            "description": "Cwicz przekierowania plikow:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "stworz folder"},
                {"type": "shell", "cmd": f"ls -la ~ > {QP}/listing.txt",
                 "hint": "> = zapisz stdout do pliku (nadpisuje jesli istnieje)"},
                {"type": "shell", "cmd": f"echo '# Moja lista' >> {QP}/listing.txt",
                 "hint": ">> = dopisz na koniec (nie nadpisuje)"},
                {"type": "shell", "cmd": f"wc -l < {QP}/listing.txt",
                 "hint": "< = uzyj pliku jako stdin komendy"},
                {"type": "shell", "cmd": "find / -name '*.conf' 2>/dev/null | head -5",
                 "hint": "2>/dev/null = ignoruj bledy braku dostepu"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj"},
            ],
        },
    },

    {
        "id": "3.3",
        "world": 3,
        "is_boss": True,
        "world_name": "Kopalnia Potokow",
        "world_flavor": "Narzedzia do przetwarzania tekstu. Uzywane z pipe tworza potezne jednolinijkowe programy.",
        "title": "Potezne narzedzia tekstowe",
        "xp": 30,
        "theory": [
            {"cmd": "sort",              "what": "Sortuj alfabetycznie",                  "notes": "-n = numerycznie  -r = odwrotnie  -rn = od najwiekszego"},
            {"cmd": "uniq",              "what": "Usun sasiadujace duplikaty",             "notes": "ZAWSZE po sort! uniq nie widzi niesasiadujacych duplikatow"},
            {"cmd": "uniq -c",           "what": "Policz wystapienia",                    "notes": "-c = count: dodaje licznik przed kazdym wierszem"},
            {"cmd": "cut -d: -f1",       "what": "Wytnij kolumne",                        "notes": "-d = delimiter (separator)  -f1 = pierwsza kolumna"},
            {"cmd": "tr 'a-z' 'A-Z'",   "what": "Zamien znaki (male na duze)",           "notes": "Tylko z pipe — nie przyjmuje pliku bezposrednio"},
            {"cmd": "sed 's/old/new/g'", "what": "Znajdz i zamien tekst",                 "notes": "s = substitute  g = global (wszystkie, nie tylko pierwsze)"},
            {"cmd": "awk '{print $1}'",  "what": "Wypisz pierwsza kolumne",               "notes": "$1 = pierwsza  $NF = ostatnia  -F: = separator :"},
            {"cmd": "xargs",             "what": "Zamien stdin na argumenty",             "notes": "find . -name '*.tmp' | xargs rm"},
        ],
        "boss": {
            "title": "BOSS FIGHT 3.3 — Wielki Boss: Analiza logow",
            "description": "Stworz log i przeanalizuj go jak prawdziwy admin:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "przygotuj folder"},
                {"type": "shell",
                 "cmd": f"printf '192.168.1.1 GET /index.html 200\\n10.0.0.5 GET /about.html 200\\n192.168.1.1 POST /login 401\\n10.0.0.5 GET /dashboard 200\\n172.16.0.1 GET /index.html 404\\n10.0.0.5 GET /api/data 500\\n' > {QP}/access.log",
                 "hint": "printf tworzy plik logu z 6 wpisami"},
                {"type": "shell", "cmd": f"cut -d' ' -f1 {QP}/access.log | sort | uniq -c | sort -rn",
                 "hint": "Ktore IP ma najwiecej requestow? cut→sort→uniq -c→sort -rn"},
                {"type": "shell", "cmd": f"grep -E ' [45][0-9]{{2}}$' {QP}/access.log",
                 "hint": "Wszystkie bledy (kody 4xx i 5xx) — -E = extended regex"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj"},
            ],
        },
    },

    # ══════════════════════════════════════════════════════════════════════
    # SWIAT 4: WIEZA EDYTORA
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "4.1",
        "world": 4,
        "is_boss": False,
        "world_name": "Wieza Edytora",
        "world_flavor": "Zanim opanujesz edytory, naucz sie tworzyc i modyfikowac pliki bez otwierania ich.",
        "title": "Edycja bez edytora",
        "xp": 15,
        "theory": [
            {"cmd": "echo 'tekst' > plik.txt",       "what": "Stworz plik z trescia (nadpisuje)",  "notes": "> = nadpisz  >> = dopisz na koniec"},
            {"cmd": "echo 'wiecej' >> plik.txt",      "what": "Dopisz na koniec pliku",             "notes": "Bezpieczne — nie niszczy istniejacych danych"},
            {"cmd": "cat > plik.txt",                 "what": "Wpisuj z klawiatury do pliku",       "notes": "Ctrl+D = koniec (EOF)"},
            {"cmd": "sed -i 's/stare/nowe/g' plik",  "what": "Zamien tekst w pliku (in-place)",    "notes": "-i = in-place: zmienia sam plik, nie stdout"},
            {"cmd": "sed -n '5,10p' plik",            "what": "Wypisz linie 5-10",                  "notes": "-n = nie wypisuj  p = print  5,10 = zakres"},
            {"cmd": "printf 'linia1\\nlinia2\\n'",    "what": "Wypisz tekst z interpretacja \\n",  "notes": "printf rozumie \\n  echo domyslnie nie (zalezy od shella)"},
        ],
        "boss": {
            "title": "CWICZENIE 4.1 — Edycja bez edytora",
            "description": "Manipuluj plikami tekstowymi bez otwierania edytora:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "stworz folder"},
                {"type": "shell", "cmd": f"printf 'imie: {USERNAME}\\nhost: {HOSTNAME}\\ndata: 2026\\n' > {QP}/info.txt",
                 "hint": "printf z \\n tworzy wieloliniowy plik"},
                {"type": "shell", "cmd": f"cat {QP}/info.txt",
                 "hint": "sprawdz zawartosc pliku"},
                {"type": "shell", "cmd": f"echo 'system: macOS' >> {QP}/info.txt",
                 "hint": ">> = dopisz na koniec"},
                {"type": "shell", "cmd": f"sed -i 's/2026/$(date +%Y)/g' {QP}/info.txt",
                 "hint": "zamien 2026 na aktualny rok"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj"},
            ],
        },
    },

    {
        "id": "4.2",
        "world": 4,
        "is_boss": False,
        "world_name": "Wieza Edytora",
        "world_flavor": "Nano to edytor przyjazny dla poczatkujacych. Skroty widoczne na dole ekranu. ^ = Ctrl.",
        "title": "Nano — latwiejszy start",
        "xp": 15,
        "theory": [
            {"cmd": "nano plik.txt", "what": "Otworz plik (stworzy jesli nie istnieje)", "notes": ""},
            {"cmd": "Ctrl+O",        "what": "Zapisz (O jak Output)",                   "notes": "Enter potwierdza nazwe pliku"},
            {"cmd": "Ctrl+X",        "what": "Wyjdz",                                   "notes": "Zapyta o zapis jesli sa niezapisane zmiany"},
            {"cmd": "Ctrl+W",        "what": "Szukaj tekstu",                           "notes": "Enter = nastepny wynik"},
            {"cmd": "Ctrl+K",        "what": "Wytnij cala linie",                       "notes": ""},
            {"cmd": "Ctrl+U",        "what": "Wklej wycieta linie",                     "notes": ""},
            {"cmd": "Ctrl+G",        "what": "Pomoc — wszystkie skroty",                "notes": ""},
        ],
        "boss": {
            "title": "CWICZENIE 4.2 — Nano",
            "description": "Stworz i edytuj plik w nano, potem posprzataj:",
            "steps": [
                {"type": "info",
                 "text": "Otworz nano: nano ~/quest-nano.txt\nWpisz dowolny tekst, zapisz Ctrl+O + Enter, wyjdz Ctrl+X"},
                {"type": "shell", "cmd": "cat ~/quest-nano.txt",
                 "hint": "Sprawdz ze plik zostal zapisany — powinienes zobaczyc swoj tekst"},
                {"type": "shell", "cmd": "rm ~/quest-nano.txt",
                 "hint": "posprzataj"},
            ],
        },
    },

    {
        "id": "4.3",
        "world": 4,
        "is_boss": True,
        "world_name": "Wieza Edytora",
        "world_flavor": "Vim jest trudny na poczatku ale po opanowaniu — szybszy niz kazdy inny edytor.",
        "title": "Vim — bron legendarna",
        "xp": 40,
        "theory": [
            {"cmd": "i",       "what": "Wejdz w INSERT mode — tu mozesz pisac",        "notes": "Po otwarciu Vima NIE mozesz od razu pisac!"},
            {"cmd": "ESC",     "what": "Wroc do NORMAL mode — zawsze bezpieczny",      "notes": ""},
            {"cmd": ":w",      "what": "Zapisz plik",                                  "notes": "w = write"},
            {"cmd": ":q",      "what": "Wyjdz",                                        "notes": "Tylko gdy brak niezapisanych zmian"},
            {"cmd": ":wq",     "what": "Zapisz i wyjdz",                               "notes": "Najczesciej uzywane"},
            {"cmd": ":q!",     "what": "Wyjdz BEZ zapisu",                             "notes": "! = na sile. Ucieczka awaryjna"},
            {"cmd": "h j k l", "what": "Nawigacja: lewo dol gora prawo",               "notes": "Jak strzalki — rece na home row"},
            {"cmd": "gg / G",  "what": "Poczatek / koniec pliku",                      "notes": ""},
            {"cmd": "/tekst",  "what": "Szukaj w dol",                                 "notes": "n = nastepny wynik  N = poprzedni"},
            {"cmd": "dd",      "what": "Usun (wytnij) cala linie",                     "notes": ""},
            {"cmd": "yy / p",  "what": "Kopiuj linie / wklej ponizej",                 "notes": "y = yank (kopiuj)"},
            {"cmd": "u",       "what": "Cofnij (undo)",                                "notes": "Ctrl+R = ponow (redo)"},
        ],
        "boss": {
            "title": "BOSS FIGHT 4.3 — Wiezmistrz Edytora",
            "description": "Ukoncz interaktywny tutorial Vima:",
            "steps": [
                {"type": "info",
                 "text": "Uruchom: vimtutor\nvimtutor to interaktywny samouczek wbudowany w Vima.\nTworzy i sprząta tymczasowy plik — nie musisz nic czyscic.\nCzas: ok. 30 minut."},
                {"type": "confirm",
                 "prompt": "Czy ukonczyłes vimtutor i wiesz jak wychodzic z Vima (:wq i :q!)?"},
            ],
        },
    },

    # ══════════════════════════════════════════════════════════════════════
    # SWIAT 5: TWIERDZA UPRAWNIEN
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "5.1",
        "world": 5,
        "is_boss": False,
        "world_name": "Twierdza Uprawnien",
        "world_flavor": "Kto moze co robic? Linux ma prosty ale potezny system uprawnien.",
        "title": "sudo i uzytkownicy",
        "xp": 15,
        "theory": [
            {"cmd": "whoami",         "what": "Aktualna nazwa uzytkownika",            "notes": f"Twoj: {USERNAME}"},
            {"cmd": "id",             "what": "UID, GID i grupy uzytkownika",          "notes": "UID=0 to root (administrator)"},
            {"cmd": "groups",         "what": "Do jakich grup naleze?",               "notes": "admin = mozesz uzywac sudo"},
            {"cmd": "sudo komenda",   "what": "Uruchom komende jako root",            "notes": "Superuser Do. Pyta o haslo"},
            {"cmd": "sudo -l",        "what": "Jakie komendy moge uruchamiac sudo?",  "notes": "-l = list"},
            {"cmd": "su - uzytkownik","what": "Przelacz sie na innego uzytkownika",   "notes": "su = switch user. - = zaladuj jego profil"},
            {"cmd": "last",           "what": "Historia logowan do systemu",          "notes": "Kiedy i skad sie logowali uzytkownicy"},
        ],
        "boss": {
            "title": "CWICZENIE 5.1 — Wywiad o uzytkownikach",
            "description": "Zbadaj system uprawnien i uzytkownikow:",
            "steps": [
                {"type": "shell", "cmd": "id",
                 "hint": f"Wypisuje UID ({USERNAME}), GID i grupy"},
                {"type": "shell", "cmd": "groups",
                 "hint": "Pokaz do jakich grup nalezysz"},
                {"type": "shell", "cmd": "sudo -l",
                 "hint": "Sprawdz jakie uprawnienia sudo masz (moze pytac o haslo)"},
            ],
        },
    },

    {
        "id": "5.2",
        "world": 5,
        "is_boss": False,
        "world_name": "Twierdza Uprawnien",
        "world_flavor": "Kto ma dostep? Kto jest krolem? Tu nauczysz sie kontroli.",
        "title": "Uprawnienia plikow",
        "xp": 25,
        "theory": [
            {"cmd": "ls -la",           "what": "Pokaz uprawnienia plikow",             "notes": "Format: -rwxr-xr-- (typ, wlasciciel, grupa, inni)"},
            {"cmd": "chmod 755 plik",   "what": "Ustaw uprawnienia liczbowo",            "notes": "7=rwx  5=r-x  4=r--  r=4 w=2 x=1"},
            {"cmd": "chmod 644 plik",   "what": "Typowe uprawnienia dla plikow",        "notes": "6=rw- (wlasciciel)  4=r-- (reszta)"},
            {"cmd": "chmod +x plik",    "what": "Dodaj prawo wykonywania",              "notes": "+x = dla wszystkich  u+x = tylko wlasciciel"},
            {"cmd": "chmod u+w plik",   "what": "Dodaj pisanie dla wlasciciela",        "notes": "u=wlasciciel  g=grupa  o=inni  a=wszyscy"},
            {"cmd": "sudo chown u:g p", "what": "Zmien wlasciciela i grupe",            "notes": "Wymaga sudo"},
        ],
        "boss": {
            "title": "CWICZENIE 5.2 — Straznik Uprawnien",
            "description": "Cwicz zarzadzanie uprawnieniami plikow:",
            "steps": [
                {"type": "shell", "cmd": f"touch {HOME}/quest-perm.sh",
                 "hint": "stworz plik testowy"},
                {"type": "shell", "cmd": f"ls -la {HOME}/quest-perm.sh",
                 "hint": "sprawdz uprawnienia — domyslnie rw-r--r-- (644)"},
                {"type": "shell", "cmd": f"chmod +x {HOME}/quest-perm.sh",
                 "hint": "+x = dodaj prawo wykonywania dla wszystkich"},
                {"type": "shell", "cmd": f"chmod 600 {HOME}/quest-perm.sh",
                 "hint": "600 = rw------- : tylko ty mozesz czytac i pisac"},
                {"type": "shell", "cmd": f"ls -la {HOME}/quest-perm.sh",
                 "hint": "potwierdz zmiane uprawnien na rw-------"},
                {"type": "shell", "cmd": f"rm {HOME}/quest-perm.sh",
                 "hint": "posprzataj"},
            ],
        },
    },

    {
        "id": "5.3",
        "world": 5,
        "is_boss": True,
        "world_name": "Twierdza Uprawnien",
        "world_flavor": "Zmienne srodowiskowe i aliasy to twoja osobista konfiguracja terminala.",
        "title": "Zmienne i aliasy",
        "xp": 20,
        "theory": [
            {"cmd": "echo $HOME",        "what": f"Twoj katalog domowy ({HOME})",       "notes": ""},
            {"cmd": "echo $PATH",        "what": "Gdzie system szuka programow",        "notes": "Lista katalogow oddzielona :"},
            {"cmd": "echo $USER",        "what": f"Twoja nazwa uzytkownika ({USERNAME})","notes": ""},
            {"cmd": "export VAR='val'",  "what": "Ustaw zmienna dla tej sesji",         "notes": "Bez export = tylko w biezacym shellu"},
            {"cmd": "source ~/.zshrc",   "what": "Przeladuj konfiguracje bez restartu", "notes": ""},
            {"cmd": "alias ll='ls -laG'","what": "Stworz skrot do komendy",            "notes": "-G = kolory na macOS"},
        ],
        "boss": {
            "title": "BOSS FIGHT 5.3 — Konfiguracja Powloki",
            "description": "Zbadaj zmienne i stworz alias:",
            "steps": [
                {"type": "shell", "cmd": "echo $PATH | tr ':' '\\n'",
                 "hint": "Pokaz PATH czytelnie — kazdy katalog w nowej linii"},
                {"type": "shell", "cmd": "alias ll='ls -laG'",
                 "hint": "Stworz tymczasowy alias ll  -G = kolory na macOS"},
                {"type": "shell", "cmd": "ll ~",
                 "hint": "Przetestuj alias — powinien dzialac jak ls -laG ~"},
                {"type": "confirm",
                 "prompt": "Czy chcesz zapisac alias permanentnie do ~/.zshrc? (echo \"alias ll='ls -laG'\" >> ~/.zshrc)"},
            ],
        },
    },

    # ══════════════════════════════════════════════════════════════════════
    # SWIAT 6: LABIRYNT PROCESOW
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "6.1",
        "world": 6,
        "is_boss": False,
        "world_name": "Labirynt Procesow",
        "world_flavor": "Kazdy uruchomiony program to proces z unikalnym PID. Naucz sie je obserwowac.",
        "title": "Obserwacja procesow",
        "xp": 15,
        "theory": [
            {"cmd": "ps",             "what": "Procesy biezacej sesji terminala",       "notes": "Domyslnie tylko twoje procesy w tym terminalu"},
            {"cmd": "ps aux",         "what": "WSZYSTKIE procesy systemu",              "notes": "a=wszyscy u=czytelny format x=procesy bez terminala"},
            {"cmd": f"ps aux | grep {USERNAME}", "what": "Procesy konkretnego uzytkownika", "notes": f"Podmien {USERNAME} na dowolna nazwe"},
            {"cmd": "top -o cpu",     "what": "Monitor na zywo — sortuj po CPU",       "notes": "q = wyjdz  -o cpu/mem = sortuj po kolumnie"},
            {"cmd": "uptime",         "what": "Czas pracy systemu + obciazenie",        "notes": "load avg: srednie 1min 5min 15min"},
            {"cmd": "echo $$",        "what": "PID biezacego procesu shella",           "notes": "$$ = zmienna specjalna z PID aktualnego shella"},
        ],
        "boss": {
            "title": "CWICZENIE 6.1 — Obserwator",
            "description": "Przyjrzyj sie procesom systemu:",
            "steps": [
                {"type": "shell", "cmd": "uptime",
                 "hint": "Sprawdz jak dlugo system dziala i obciazenie"},
                {"type": "shell", "cmd": "ps aux | wc -l",
                 "hint": "Policz ile procesow dziala w systemie"},
                {"type": "shell", "cmd": f"ps aux | grep {USERNAME}",
                 "hint": f"Znajdz wszystkie procesy uzytkownika {USERNAME}"},
                {"type": "shell", "cmd": "echo $$",
                 "hint": "Wypisz PID biezacego shella"},
            ],
        },
    },

    {
        "id": "6.2",
        "world": 6,
        "is_boss": True,
        "world_name": "Labirynt Procesow",
        "world_flavor": "Kazdy uruchomiony program to proces z unikalnym PID. System ma ich setki w tle.",
        "title": "Zarzadzanie procesami",
        "xp": 25,
        "theory": [
            {"cmd": "komenda &",      "what": "Uruchom w tle",                         "notes": "& na koncu — shell wraca do promptu od razu"},
            {"cmd": "Ctrl+Z",         "what": "Zawies biezacy proces",                 "notes": "Zatrzymaj, nie zabij — wraca do promptu"},
            {"cmd": "bg / fg",        "what": "Wznow w tle / przywroc na pierwszy plan","notes": "bg %1 = wznow pierwszy job w tle"},
            {"cmd": "jobs -l",        "what": "Lista procesow w tle z PID",            "notes": "-l = long (pokaz PID)"},
            {"cmd": "kill PID",       "what": "Grzeczna prosba o zakonczenie",         "notes": "Wysyla SIGTERM — proces moze zignorowac"},
            {"cmd": "kill -9 PID",    "what": "Natychmiastowe zabicie",                "notes": "-9 = SIGKILL. Ostatecznosc — nie mozna zignorowac"},
            {"cmd": "kill %1",        "what": "Zabij pierwszy job z listy jobs",       "notes": "%1 = numer joba (nie PID!)"},
            {"cmd": "lsof -i :8080",  "what": "Co uzywa portu 8080?",                 "notes": "Gdy 'port is already in use'"},
        ],
        "boss": {
            "title": "BOSS FIGHT 6.2 — Pogromca Procesow",
            "description": "Uruchom proces w tle, znajdz go i zabij:",
            "steps": [
                {"type": "shell", "cmd": "sleep 300 &",
                 "hint": "& = uruchom w tle. Shell od razu wraca do promptu"},
                {"type": "shell", "cmd": "jobs -l",
                 "hint": "Pokaz liste procesow w tle z PID"},
                {"type": "shell", "cmd": "kill %1",
                 "hint": "%1 = pierwszy job z listy jobs (nie PID!)"},
                {"type": "shell", "cmd": "jobs",
                 "hint": "Lista powinna byc pusta — proces zostal zabity"},
            ],
        },
    },

    # ══════════════════════════════════════════════════════════════════════
    # SWIAT 7: KUZNIA SKRYPTOW
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "7.1",
        "world": 7,
        "is_boss": False,
        "world_name": "Kuznia Skryptow",
        "world_flavor": "Zanim napiszesz skrypt, musisz opanowac zmienne, substytucje i obliczenia.",
        "title": "Zmienne i substytucje",
        "xp": 15,
        "theory": [
            {"cmd": "ZMIENNA='wartosc'",        "what": "Przypisz wartosc (brak spacji przy =!)",  "notes": "Blad: ZMIENNA = 'x'  Dobrze: ZMIENNA='x'"},
            {"cmd": "echo $ZMIENNA",             "what": "Odczytaj wartosc zmiennej",              "notes": "$ = odwolanie do zmiennej"},
            {"cmd": "echo ${ZMIENNA:-domyslna}", "what": "Wartosc domyslna jesli pusta",           "notes": ":- = jesli pusta/niezdefiniowana uzyj domyslnej"},
            {"cmd": "echo $(komenda)",           "what": "Wstaw wynik komendy (command subst.)",   "notes": f"np. echo \"Dzis: $(date +%A)\""},
            {"cmd": "echo $((5 * 7))",           "what": "Obliczenia arytmetyczne",                "notes": "(( )) = kontekst matematyczny w bashu/zsh"},
            {"cmd": "read -p 'Imie: ' IMIE",    "what": "Pobierz input od uzytkownika",           "notes": "-p = prompt (wyswietl pytanie przed czekaniem)"},
            {"cmd": "unset ZMIENNA",             "what": "Usun zmienna",                           "notes": "Po unset echo $ZMIENNA = pusty ciag"},
        ],
        "boss": {
            "title": "CWICZENIE 7.1 — Zmienne",
            "description": "Cwicz zmienne i substytucje:",
            "steps": [
                {"type": "shell", "cmd": f"IMIE='{USERNAME}' && echo \"Witaj, $IMIE!\"",
                 "hint": "Przypisz zmienna i wypisz z substytucja w jednej linii"},
                {"type": "shell", "cmd": "echo $((3 * 14))",
                 "hint": "Oblicz 3 * 14 uzywajac (( ))"},
                {"type": "shell", "cmd": "echo \"Teraz jest $(date +%H:%M) na ${HOSTNAME:-komputerze}\"",
                 "hint": "Wstaw czas przez command substitution, hostname przez zmienną"},
            ],
        },
    },

    {
        "id": "7.2",
        "world": 7,
        "is_boss": True,
        "world_name": "Kuznia Skryptow",
        "world_flavor": "Skrypt to plik tekstowy z komendami — jak lista zakupow dla terminala.",
        "title": "Pierwszy skrypt",
        "xp": 30,
        "theory": [
            {"cmd": "#!/bin/bash",       "what": "Shebang — pierwsza linia skryptu",   "notes": "Mowi systemowi jakiego interpretera uzyc"},
            {"cmd": "NAME='Zenon'",      "what": "Zmienna",                             "notes": "Brak spacji przy =! $NAME = odczyt wartosci"},
            {"cmd": "echo \"$NAME\"",    "what": "Wypisz zmienna",                     "notes": "Podwojne cudzyslowy interpretuja zmienne"},
            {"cmd": "$0 $1 $#",          "what": "Argumenty skryptu",                  "notes": "$0=nazwa  $1=pierwszy argument  $#=liczba argumentow"},
            {"cmd": "if [ -f $1 ]",      "what": "Sprawdz czy plik istnieje",          "notes": "-f = plik  -d = katalog  -z = pusty string"},
            {"cmd": "for i in 1 2 3",    "what": "Petla for",                          "notes": "done = koniec petli"},
            {"cmd": "$(( count + 1 ))",  "what": "Obliczenia arytmetyczne",            "notes": "$() = wykonaj komende i wstaw wynik"},
            {"cmd": "chmod +x skrypt.sh","what": "Nadaj prawo wykonywania",            "notes": "Raz! Potem: ./skrypt.sh"},
        ],
        "boss": {
            "title": "BOSS FIGHT 7.2 — Kowal Skryptow",
            "description": "Napisz, uruchom i posprzataj skrypt:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "stworz folder na skrypt"},
                {"type": "info",
                 "text": f"Napisz skrypt: nano {QP}/hello.sh\n\nWpisz w nano:\n#!/bin/bash\nNAME=${{1:-'Nieznajomy'}}\necho \"Witaj, $NAME!\"\necho \"Uzytkownik: $(whoami)\"\necho \"Host: $(hostname)\"\necho \"Data: $(date '+%Y-%m-%d')\"\n\nZapisz: Ctrl+O + Enter, wyjdz: Ctrl+X"},
                {"type": "shell", "cmd": f"chmod +x {QP}/hello.sh",
                 "hint": "nadaj prawo wykonywania skryptowi"},
                {"type": "shell", "cmd": f"{QP}/hello.sh",
                 "hint": "uruchom bez argumentu — zobaczysz 'Witaj, Nieznajomy!'"},
                {"type": "shell", "cmd": f"{QP}/hello.sh {USERNAME}",
                 "hint": f"uruchom z argumentem — zobaczysz 'Witaj, {USERNAME}!'"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj"},
            ],
        },
    },

    # ══════════════════════════════════════════════════════════════════════
    # SWIAT 8: SWIATYNIA SIECI
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "8.1",
        "world": 8,
        "is_boss": False,
        "world_name": "Swiatynia Sieci",
        "world_flavor": "Zanim zaczniesz czarowac siec, opanuj narzedzia diagnostyczne.",
        "title": "Diagnostyka sieci",
        "xp": 15,
        "theory": [
            {"cmd": "ping -c 3 1.1.1.1",   "what": "Sprawdz polaczenie (3 pakiety)",     "notes": "1.1.1.1 = Cloudflare DNS. -c = count"},
            {"cmd": "hostname",             "what": "Nazwa twojego komputera",             "notes": f"Twoj: {HOSTNAME}"},
            {"cmd": "ifconfig | grep inet", "what": "Adresy IP interfejsow sieciowych",   "notes": "inet = IPv4  inet6 = IPv6  lo0 = localhost"},
            {"cmd": "curl -I URL",          "what": "Pobierz tylko naglowki HTTP",         "notes": "-I = HEAD request: sprawdz status bez pobierania body"},
            {"cmd": "netstat -nr",          "what": "Tablica routingu",                    "notes": "-n = numerycznie  -r = routing (domyslna brama)"},
            {"cmd": "host domena",          "what": "Zamien domene na IP (DNS lookup)",    "notes": "np. host google.com  lub nslookup google.com"},
        ],
        "boss": {
            "title": "CWICZENIE 8.1 — Diagnostyka",
            "description": "Sprawdz stan swojej sieci:",
            "steps": [
                {"type": "shell", "cmd": "ping -c 3 1.1.1.1",
                 "hint": "Wyslij 3 pakiety do 1.1.1.1 (Cloudflare DNS, zawsze online)"},
                {"type": "shell", "cmd": "hostname",
                 "hint": f"Sprawdz nazwe komputera — powinno byc: {HOSTNAME}"},
                {"type": "shell", "cmd": "ifconfig | grep 'inet '",
                 "hint": "Znajdz adresy IPv4 (grep 'inet ' ze spacja = nie lapie inet6)"},
            ],
        },
    },

    {
        "id": "8.2",
        "world": 8,
        "is_boss": True,
        "world_name": "Swiatynia Sieci",
        "world_flavor": "curl to terminal-przegladarka. SSH pozwala zarzadzac zdalnymi serwerami.",
        "title": "curl i SSH",
        "xp": 25,
        "theory": [
            {"cmd": "curl ifconfig.me",    "what": "Pokaz swoje publiczne IP",           "notes": ""},
            {"cmd": "curl -s URL",         "what": "Pobierz dane bez paska postepu",     "notes": "-s = silent. Dobre w skryptach"},
            {"cmd": "curl -o plik URL",    "what": "Pobierz i zapisz do pliku",          "notes": "-o = output: podaj nazwe pliku"},
            {"cmd": "networkQuality",      "what": "Test predkosci internetu (macOS 12+)","notes": ""},
            {"cmd": "ssh user@serwer",     "what": "Polacz sie z serwerem SSH",          "notes": "Domyslny port: 22"},
            {"cmd": "ssh -p 2222 u@s",     "what": "Polacz sie na innym porcie",         "notes": "-p = port"},
            {"cmd": "scp plik u@s:/path",  "what": "Kopiuj plik na serwer",             "notes": "scp = secure copy, ten sam protokol co SSH"},
            {"cmd": "ssh-keygen -t ed25519","what": "Generuj klucz SSH",                "notes": "ed25519 = nowoczesny algorytm. Lepszy niz rsa"},
        ],
        "boss": {
            "title": "BOSS FIGHT 8.2 — Sieciowy Mag",
            "description": "Cwicz komendy sieciowe curl:",
            "steps": [
                {"type": "shell", "cmd": "curl -s ifconfig.me",
                 "hint": "Pokaz swoje publiczne IP (bez znakow postepu -s = silent)"},
                {"type": "shell", "cmd": "ping -c 4 google.com",
                 "hint": "-c 4 = wyslij tylko 4 pakiety i zakoncz automatycznie"},
                {"type": "shell", "cmd": "curl -s https://api.github.com | head -5",
                 "hint": "Pobierz dane z publicznego API GitHub i pokaz 5 linii"},
            ],
        },
    },

    # ══════════════════════════════════════════════════════════════════════
    # SWIAT 9: OTCHLAN GITA
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "9.1",
        "world": 9,
        "is_boss": False,
        "world_name": "Otchlan Gita",
        "world_flavor": "Git sledzi kazda zmiane w kodzie. Mozesz cofnac sie do dowolnego momentu w historii.",
        "title": "Git podstawy",
        "xp": 30,
        "theory": [
            {"cmd": "git init",           "what": "Stworz nowe repo (.git folder)",     "notes": ""},
            {"cmd": "git status",         "what": "Co sie zmienilo?",                   "notes": "Uzywaj czesto!"},
            {"cmd": "git add plik.txt",   "what": "Dodaj plik do stage",                "notes": "Stage = obszar przygotowany do commita"},
            {"cmd": "git add .",          "what": "Dodaj WSZYSTKIE zmiany do stage",    "notes": ". = biezacy katalog"},
            {"cmd": "git commit -m 'msg'","what": "Zapisz stage jako commit",           "notes": "-m = krotki opis zmian"},
            {"cmd": "git log --oneline",  "what": "Historia commitow",                  "notes": "--oneline = 1 linia na commit zamiast 6"},
            {"cmd": "git diff",           "what": "Zmiany ktore NIE sa w stage",        "notes": "--staged = zmiany ktore SA w stage"},
        ],
        "boss": {
            "title": "CWICZENIE 9.1 — Git Basics",
            "description": "Zrob pelny cykl: init, add, commit:",
            "steps": [
                {"type": "shell", "cmd": f"git init {QP}",
                 "hint": "zainicjuj repo git w folderze quest-project"},
                {"type": "shell", "cmd": f"echo 'Hello Git z {HOSTNAME}' > {QP}/plik.txt",
                 "hint": "stworz plik z trescia"},
                {"type": "shell", "cmd": f"git -C {QP} status",
                 "hint": "sprawdz status — plik powinien byc jako 'untracked'"},
                {"type": "shell", "cmd": f"git -C {QP} add plik.txt",
                 "hint": "dodaj plik do stage"},
                {"type": "shell", "cmd": f"git -C {QP} commit -m 'Initial commit'",
                 "hint": "zapisz commit z wiadomoscia"},
                {"type": "shell", "cmd": f"git -C {QP} log --oneline",
                 "hint": "sprawdz historie — powinien byc jeden commit"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj"},
            ],
        },
    },

    {
        "id": "9.2",
        "world": 9,
        "is_boss": True,
        "world_name": "Otchlan Gita",
        "world_flavor": "Branch = niezalezna linia rozwoju. Pracujesz na feature bez psucia main.",
        "title": "Branche i merge",
        "xp": 30,
        "theory": [
            {"cmd": "git branch",          "what": "Pokaz liste branchy",               "notes": "* = aktualny branch"},
            {"cmd": "git branch feature",  "what": "Stworz nowy branch",               "notes": "Nie przelacza sie automatycznie"},
            {"cmd": "git checkout feature","what": "Przelacz sie na branch",            "notes": ""},
            {"cmd": "git checkout -b feat","what": "Stworz i przelacz w jednym",       "notes": "-b = branch: skrot z dwoch komend"},
            {"cmd": "git merge feature",   "what": "Polacz branch z aktualnym",         "notes": "Bedac na main: git merge feature"},
            {"cmd": "git branch -d feat",  "what": "Usun branch",                      "notes": "-d = tylko jesli juz zmergowany. -D = na sile"},
        ],
        "boss": {
            "title": "BOSS FIGHT 9.2 — Mistrz Branchy",
            "description": "Stworz branch, zrob commit, zmerguj:",
            "steps": [
                {"type": "shell", "cmd": f"git init {QP}",
                 "hint": "stworz repo"},
                {"type": "shell", "cmd": f"echo 'main' > {QP}/plik.txt && git -C {QP} add . && git -C {QP} commit -m 'init'",
                 "hint": "stworz pierwszy commit na main"},
                {"type": "shell", "cmd": f"git -C {QP} checkout -b feature",
                 "hint": "-b = stworz i przelacz na nowy branch"},
                {"type": "shell", "cmd": f"echo 'feature' >> {QP}/plik.txt && git -C {QP} add . && git -C {QP} commit -m 'add feature'",
                 "hint": "dodaj zmiane i commituj na feature branch"},
                {"type": "shell", "cmd": f"git -C {QP} checkout main",
                 "hint": "wroc na main"},
                {"type": "shell", "cmd": f"git -C {QP} merge feature",
                 "hint": "zmerguj feature do main"},
                {"type": "shell", "cmd": f"git -C {QP} log --oneline --graph",
                 "hint": "--graph = drzewo branchy ASCII"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj"},
            ],
        },
    },

    # ══════════════════════════════════════════════════════════════════════
    # SWIAT 10: TRON ARCYMISTRZA
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "10.1",
        "world": 10,
        "is_boss": True,
        "world_name": "Tron Arcymistrza",
        "world_flavor": "Ostatnie sekrety. Po tym — jestes Arcymistrzem Terminala.",
        "title": "Zaawansowane techniki",
        "xp": 40,
        "theory": [
            {"cmd": "mkdir -p proj/{src,tests}/{v1,v2}", "what": "Brace expansion: 4 katalogi naraz",  "notes": "{a,b} = lista  {1..5} = zakres"},
            {"cmd": "touch plik{1..10}.txt",             "what": "Stworz 10 plikow jednym poleceniem","notes": ""},
            {"cmd": "echo $(date +%H:%M)",               "what": "Wstaw wynik komendy",               "notes": "$() = command substitution"},
            {"cmd": "diff <(ls dir1) <(ls dir2)",        "what": "Porownaj outputy dwoch komend",     "notes": "<() = process substitution"},
            {"cmd": "find . -mtime +30 -exec rm {} \\;", "what": "Znajdz i usun pliki starsze niz 30 dni", "notes": "-exec = wykonaj dla kazdego wyniku"},
            {"cmd": "cmd1 & cmd2 & wait",                "what": "Uruchom rownolegle i czekaj",       "notes": ""},
            {"cmd": "awk -F: '{print $1}' /etc/passwd",  "what": "Wypisz pierwsza kolumne z : jako sep.", "notes": "-F: = separator :"},
        ],
        "boss": {
            "title": "FINAL BOSS — Arcymistrz Terminala",
            "description": "Pokonaj ostateczne wyzwanie — brace expansion i zaawansowane techniki:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {HOME}/projekt/{{src,tests,docs}}/{{v1,v2}}",
                 "hint": "tworzy 6 katalogow naraz: src/v1, src/v2, tests/v1, tests/v2, docs/v1, docs/v2"},
                {"type": "shell", "cmd": f"ls -R {HOME}/projekt",
                 "hint": "sprawdz pelna strukture (-R = recursive)"},
                {"type": "shell", "cmd": f"touch {HOME}/projekt/plik{{1..5}}.txt",
                 "hint": "{1..5} = sekwencja: tworzy plik1.txt ... plik5.txt"},
                {"type": "shell", "cmd": f"find {HOME}/projekt -name '*.txt' | wc -l",
                 "hint": "policz ile plikow .txt zostalo stworzonych (powinno byc 5)"},
                {"type": "shell", "cmd": f"rm -r {HOME}/projekt",
                 "hint": "posprzataj — ostatni raz!"},
                {"type": "confirm",
                 "prompt": "Gratulacje Arcymistrzu! Czy ukonczyłes Terminal Quest?"},
            ],
        },
    },
]
