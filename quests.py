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

XP_PER_LEVEL = 20

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

WORLD_PASSWORDS = {
    1:  "wioska",
    2:  "las",
    3:  "kopalnia",
    4:  "wieza",
    5:  "twierdza",
    6:  "labirynt",
    7:  "kuznia",
    8:  "swiatynia",
    9:  "otchlan",
    10: "tron",
}

QUESTS = [

    # ══════════════════════════════════════════════════════════════════════
    # SWIAT 0: PRZYGOTOWANIE
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "0.1",
        "world": 0,
        "is_boss": False,
        "world_name": "Przygotowanie macOS",
        "world_flavor": (
            "Kazdy wielki wojownik przed bitwa sprawdza swoj ekwipunek. "
            "Homebrew to twoj osobisty zbrojmistrz — jednym slowem instaluje kazde narzedzie. "
            "Bez niego ani rusz."
        ),
        "title": "Homebrew — menedzer pakietow",
        "xp": 10,
        "theory": [
            {"cmd": "brew install nazwa",     "what": "Zainstaluj program",           "notes": "np. brew install git  — Homebrew szuka pakietu w swoim rejestrze i instaluje"},
            {"cmd": "brew uninstall nazwa",   "what": "Odinstaluj program",           "notes": "Usuwa program i jego pliki, nie dotyka zaleznosci"},
            {"cmd": "brew list",              "what": "Co mam zainstalowane?",        "notes": "Lista wszystkich pakietow zainstalowanych przez Homebrew"},
            {"cmd": "brew update",            "what": "Aktualizuj liste pakietow",    "notes": "Pobiera informacje o nowych wersjach — nie instaluje jeszcze nic"},
            {"cmd": "brew upgrade",           "what": "Aktualizuj wszystkie pakiety", "notes": "Po brew update, upgrade faktycznie pobiera nowe wersje"},
            {"cmd": "brew install --cask app","what": "Zainstaluj aplikacje GUI",     "notes": "--cask = aplikacje .app (iTerm2, VSCode, Firefox) — nie narzedzia CLI"},
        ],
        "boss": {
            "title": "CWICZENIE 0.1 — Ekwipunek",
            "description": "Straznik bramy sprawdza twoj ekwipunek zanim wpusci cie do Wioski. Udowodnij ze masz co trzeba:",
            "steps": [
                {"type": "shell", "cmd": "brew --version",
                 "hint": "Powinnas zobaczyc 'Homebrew X.Y.Z'",
                 "output": "Homebrew 4.2.21\nHomebrew/homebrew-core (git revision f3f3c5eba; last commit 2024-03-20)"},
                {"type": "shell", "cmd": "git --version",
                 "hint": "Powinnas zobaczyc 'git version X.Y.Z'",
                 "output": "git version 2.44.0"},
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
        "world_flavor": (
            "Budzisz sie w terminalu. Migajacy kursor czeka jak wierny sluga gotowy spelniac rozkazy. "
            "Zanim wyruszysz w swiat, musisz nauczyc sie poruszac — pwd to twoj kompas, ls to latarka, cd to nogi. "
            "Te trzy komendy to fundament wszystkiego co przyjdzie pozniej."
        ),
        "title": "Pierwsze kroki",
        "xp": 15,
        "theory": [
            {"cmd": "pwd",        "what": "Gdzie jestem? (Print Working Directory)",        "notes": f"Zawsze wypisuje pelna sciezke absolutna, np. {HOME}"},
            {"cmd": "ls",         "what": "Co tu jest? Listuje pliki w katalogu",           "notes": "Bez argumentu = biezacy katalog. Podaj sciezke: ls /etc"},
            {"cmd": "ls -la",     "what": "Pokaz WSZYSTKO z detalami",                      "notes": "-l = szczegoly (uprawnienia, rozmiar, data)  -a = ukryte pliki (nazwa zaczyna sie od .)"},
            {"cmd": "cd katalog", "what": "Idz do katalogu (Change Directory)",             "notes": "Sciezka wzgledna: cd Documents  absolutna: cd /etc"},
            {"cmd": "cd ..",      "what": "Cofnij sie o jeden katalog w gore",              "notes": ".. = zawsze oznacza katalog nadrzedny. ../../ = dwa poziomy wyzej"},
            {"cmd": "cd ~",       "what": f"Wroc do domu ({HOME})",                        "notes": "~ to skrot do twojego katalogu domowego, dziala wszedzie"},
            {"cmd": "cd -",       "what": "Wroc tam gdzie bylem ostatnio",                 "notes": "Shell pamięta poprzednie miejsce — - to jak przycisk Wstecz"},
            {"cmd": "clear",      "what": "Wyczysc ekran",                                 "notes": "Ctrl+L dziala tak samo — ale historia nie znika, tylko przesuwa ekran"},
        ],
        "boss": {
            "title": "CWICZENIE 1.1 — Nawigator",
            "description": "Przewodnik po Wiosce daje ci probe — przejdz przez 5 znanych adresow i wroc do domu:",
            "steps": [
                {"type": "shell", "cmd": "cd /tmp",
                 "hint": "/tmp = pliki tymczasowe, czyszczone po restarcie",
                 "output": ""},
                {"type": "shell", "cmd": "cd /var/log",
                 "hint": "/var/log = logi systemowe — tu system zapisuje co sie dzieje",
                 "output": ""},
                {"type": "shell", "cmd": "cd /usr/local",
                 "hint": "/usr/local = tu Homebrew instaluje programy",
                 "output": ""},
                {"type": "shell", "cmd": "cd /etc",
                 "hint": "/etc = konfiguracja systemu — pliki tekstowe z ustawieniami",
                 "output": ""},
                {"type": "shell", "cmd": "cd ~/Documents",
                 "hint": "~/Documents = twoj folder Dokumenty  ~ = skrot do home",
                 "output": ""},
                {"type": "shell", "cmd": "cd ~",
                 "hint": "Wroc do katalogu domowego",
                 "output": ""},
                {"type": "shell", "cmd": "pwd",
                 "hint": f"Powinienes zobaczyc {HOME}",
                 "output": f"{HOME}"},
            ],
        },
    },

    {
        "id": "1.2",
        "world": 1,
        "is_boss": False,
        "world_name": "Wioska Startowa",
        "world_flavor": (
            "Szpieg zawsze najpierw zbiera informacje o terenie przed akcja. "
            "Zanim zaatakujesz problem, sprawdz kto jestes, gdzie jestes i co cie otacza. "
            "whoami, date, uname — twoje narzedzia rozpoznawcze."
        ),
        "title": "Rozpoznanie terenu",
        "xp": 15,
        "theory": [
            {"cmd": "whoami",       "what": "Kim jestem? Wypisuje nazwe uzytkownika",      "notes": f"Twoj: {USERNAME}  Wazne gdy uzywasz sudo lub ssh na inny serwer"},
            {"cmd": "date",         "what": "Aktualna data i czas",                        "notes": "date '+%Y-%m-%d' = tylko data  date '+%H:%M' = tylko godzina"},
            {"cmd": "cal",          "what": "Kalendarz miesiezny",                         "notes": "cal 2026 = caly rok  cal 3 2026 = marzec 2026"},
            {"cmd": "uname -a",     "what": "Info o systemie (OS, kernel, architektura)",  "notes": "-a = all. Szukaj 'arm64' = Apple Silicon, 'x86_64' = Intel"},
            {"cmd": "echo 'tekst'", "what": "Wypisz tekst na ekran",                       "notes": "echo $HOME = wartosc zmiennej srodowiskowej"},
            {"cmd": "history",      "what": "Historia ostatnich komend",                   "notes": "history | grep git = tylko komendy zawierajace 'git'"},
            {"cmd": "man ls",       "what": "Manual (dokumentacja) komendy",               "notes": "/ = szukaj frazy  n = nastepny wynik  q = wyjscie"},
        ],
        "boss": {
            "title": "CWICZENIE 1.2 — Wywiad",
            "description": "Stary szpieg w tawernie daje ci liste pytan wywiadowczych — odpowiedz uzywajac komend terminala:",
            "steps": [
                {"type": "shell", "cmd": "whoami",
                 "hint": f"Wypisuje nazwe uzytkownika — powinno byc: {USERNAME}",
                 "output": f"{USERNAME}"},
                {"type": "shell", "cmd": "date",
                 "hint": "Pokazuje dzisiejszy dzien tygodnia i godzine",
                 "output": "Sun Apr  6 14:32:17 CEST 2026"},
                {"type": "shell", "cmd": "uname -a",
                 "hint": "Pokazuje system i architekture (arm64 = Apple Silicon)",
                 "output": f"Darwin {HOSTNAME}.local 24.3.0 Darwin Kernel Version 24.3.0: Thu Jan  2 20:24:16 PST 2026; root:xnu-11215.81.4~3/RELEASE_ARM64_T8112 arm64"},
                {"type": "shell", "cmd": "history",
                 "hint": "Lista ostatnich komend — historia twoich dzialan",
                 "output": "  107  brew install git\n  108  cd ~\n  109  ls -la\n  110  pwd\n  111  whoami\n  112  date\n  113  uname -a\n  114  clear\n  115  history"},
            ],
        },
    },

    {
        "id": "1.3",
        "world": 1,
        "is_boss": True,
        "world_name": "Wioska Startowa",
        "world_flavor": (
            "Prawdziwy wojownik nie szuka rzeczy w kieszeniach — jego palce same trafiaja gdzie trzeba. "
            "Skroty klawiszowe to roznica miedzy amatorem a profesjonalista. "
            "Jeden skrot moze zaoszczedzic tysiac klikniec."
        ),
        "title": "Skroty klawiszowe",
        "xp": 20,
        "theory": [
            {"cmd": "Tab",         "what": "AUTOUZUPELNIANIE — najwazniejszy skrot",  "notes": "Dwa razy Tab = pokaz wszystkie mozliwosci"},
            {"cmd": "Ctrl+C",      "what": "Przerwij biezaca komende",                "notes": "Wysyla sygnal SIGINT do procesu. Ratuje gdy komenda sie zawieszla"},
            {"cmd": "Ctrl+R",      "what": "Szukaj wstecz w historii komend",         "notes": "Wpisz fragment, ENTER = wykonaj, Ctrl+R znowu = nastepny wynik"},
            {"cmd": "Ctrl+L",      "what": "Wyczysc ekran",                           "notes": "To samo co clear — ale nie kasuje historii"},
            {"cmd": "Ctrl+A",      "what": "Skocz na poczatek linii",                 "notes": "A jak poczAtek. Pomocne gdy chcesz dodac sudo na poczatku dlugiej komendy"},
            {"cmd": "Ctrl+E",      "what": "Skocz na koniec linii",                   "notes": "E jak End. Tandem z Ctrl+A"},
            {"cmd": "Ctrl+W",      "what": "Usun slowo w lewo",                       "notes": "Szybsze niz trzymanie Backspace"},
            {"cmd": "Ctrl+U",      "what": "Usun cala linie od kursora w lewo",       "notes": "Ctrl+K usuwa od kursora w prawo"},
            {"cmd": "!!",          "what": "Powtorz ostatnia komende",                "notes": "Najczesciej: sudo !! gdy ostatnia komenda odrzucona przez brak uprawnien"},
            {"cmd": "strzalka UP", "what": "Poprzednia komenda w historii",           "notes": "DOWN = nastepna"},
        ],
        "boss": {
            "title": "BOSS FIGHT 1.3 — Mistrz Skrotow",
            "description": (
                "Straznik Wioski blokuje brame i pyta o skroty. "
                "Udowodnij ze je znasz — trzy zycia wspolne:"
            ),
            "steps": [
                {"type": "quiz",
                 "question": "Jakim skrotem PRZERWIESZ zawieszona komende?",
                 "answers": ["ctrl+c", "^c"],
                 "hint": "Wysyla sygnal SIGINT — zabija to co teraz dziala w terminalu"},
                {"type": "quiz",
                 "question": "Jakim skrotem WYSZUKASZ poprzednia komende w historii?",
                 "answers": ["ctrl+r"],
                 "hint": "Otwiera interaktywne wyszukiwanie wstecz (reverse search)"},
                {"type": "quiz",
                 "question": "Jakim skrotem SKOCZYSZ na poczatek linii?",
                 "answers": ["ctrl+a", "^a"],
                 "hint": "A jak poczAtek — przesuwa kursor na sam poczatek wpisywanej komendy"},
                {"type": "quiz",
                 "question": "Wpisujesz dlugie polecenie i chesz USUNAC ostatnie slowo. Jaki skrot?",
                 "answers": ["ctrl+w", "^w"],
                 "hint": "Szybsze niz trzymanie Backspace — usuwa od kursora do poprzedniej spacji"},
                {"type": "quiz",
                 "question": "Jakim skrotem POWTORZYSZ ostatnio wykonana komende bez przepisywania?",
                 "answers": ["!!", "sudo !!"],
                 "hint": "Dwa wykrzykniki z rzedu — historia shella"},
                {"type": "shell", "cmd": "history | tail -5",
                 "hint": "Pokaz ostatnie 5 komend z historii — sprawdz co wpisywales",
                 "output": "  112  whoami\n  113  date\n  114  uname -a\n  115  clear\n  116  history | tail -5"},
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
        "world_flavor": (
            "Wkraczasz w gesty Las Plikow. Tu wszystko jest drzewem — katalogi to galęzie, pliki to liscie. "
            "Mozesz zbudowac caly projekt jednym poleceniem albo zrowac go z ziemia rownie szybko. "
            "Opanujesz tworzenie i niszczenie — bez Kosza, bez ostrzezen."
        ),
        "title": "Tworzenie i niszczenie",
        "xp": 20,
        "theory": [
            {"cmd": "touch plik.txt",     "what": "Stworz pusty plik",                    "notes": "Jesli plik istnieje — tylko aktualizuje date modyfikacji, nie niszczy zawartosci"},
            {"cmd": "mkdir folder",       "what": "Stworz katalog",                        "notes": "Blad jesli katalog juz istnieje — uzyj -p zeby tego uniknac"},
            {"cmd": "mkdir -p a/b/c",     "what": "Stworz zagniezdzone katalogi",          "notes": "-p = parents: tworzy wszystkie brakujace katalogi po drodze"},
            {"cmd": "cp zrodlo cel",      "what": "Kopiuj plik",                           "notes": "Jesli cel istnieje — nadpisuje BEZ pytania! cp -i = pytaj przed nadpisaniem"},
            {"cmd": "cp -r folder kopia", "what": "Kopiuj caly katalog",                   "notes": "-r = recursive: wchodzi w podkatalogi i kopiuje wszystko"},
            {"cmd": "mv stary nowy",      "what": "Przenies lub zmien nazwe",              "notes": "Ta sama komenda robi obie rzeczy"},
            {"cmd": "rm plik",            "what": "USUN plik (NIEODWRACALNE!)",            "notes": "Brak Kosza — rm usuwa na zawsze. Ctrl+Z nie pomoze"},
            {"cmd": "rm -r folder",       "what": "USUN katalog z zawartoscia",            "notes": "-r = recursive: wchodzi i usuwa wszystko. rm -rf / to koniec systemu!"},
            {"cmd": "rmdir folder",       "what": "Usun PUSTY katalog",                    "notes": "Odmowi jesli nie pusty — bezpieczniejsza alternatywa dla rm -r"},
        ],
        "boss": {
            "title": "CWICZENIE 2.1 — Budowniczy i Niszczyciel",
            "description": "Duch Lasu daje ci zadanie: zbuduj strukture projektu, sprawdz ja i posprzataj po sobie:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}/{{src/utils,docs,tests}}",
                 "hint": "-p = parents  {{a,b}} = brace expansion: tworzy kilka katalogow naraz",
                 "output": ""},
                {"type": "shell", "cmd": f"touch {QP}/src/main.sh",
                 "hint": "touch = stworz pusty plik  .sh = rozszerzenie skryptu bash",
                 "output": ""},
                {"type": "shell", "cmd": f"touch {QP}/src/utils/helpers.sh",
                 "hint": "plik funkcji pomocniczych w podkatalogu",
                 "output": ""},
                {"type": "shell", "cmd": f"touch {QP}/docs/README.md",
                 "hint": "dokumentacja  .md = markdown",
                 "output": ""},
                {"type": "shell", "cmd": f"touch {QP}/tests/test_main.sh",
                 "hint": "plik testow",
                 "output": ""},
                {"type": "shell", "cmd": f"ls -R {QP}",
                 "hint": "-R = recursive: pokazuje zawartosc wszystkich podkatalogow",
                 "output": (
                     f"{QP}:\ndocs    src     tests\n\n"
                     f"{QP}/docs:\nREADME.md\n\n"
                     f"{QP}/src:\nmain.sh utils\n\n"
                     f"{QP}/src/utils:\nhelpers.sh\n\n"
                     f"{QP}/tests:\ntest_main.sh"
                 )},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "-r = recursive: usuwa katalog razem z cala zawartoscia NIEODWRACALNIE",
                 "output": ""},
                {"type": "shell", "cmd": f"ls ~ | grep quest-project",
                 "hint": "brak outputu = sukces, folder zniknal",
                 "output": ""},
            ],
        },
    },

    {
        "id": "2.2",
        "world": 2,
        "is_boss": False,
        "world_name": "Las Plikow",
        "world_flavor": (
            "Las skrywa wiele tajemnic zapisanych w plikach. "
            "Nie musisz czytac wszystkiego — wystarczy zajrzec na poczatek lub koniec, policzyc linie. "
            "cat nie jest odpowiedzia na wszystko: duzy plik zaflooduje terminal — uzyj less."
        ),
        "title": "Czytanie plikow",
        "xp": 20,
        "theory": [
            {"cmd": "cat plik",        "what": "Pokaz cala zawartosc pliku",           "notes": "Uzyj tylko dla malych plikow (do ~50 linii). Na duzych — less"},
            {"cmd": "less plik",       "what": "Przegladarka plikow",                  "notes": "Strzalki / PageUp/Down  /szukaj  n — nastepny  q — wyjscie"},
            {"cmd": "head -n 10 plik", "what": "Pierwsze 10 linii",                   "notes": "-n = ile linii. head -1 plik = tylko pierwsza linia (np. naglowek CSV)"},
            {"cmd": "tail -n 10 plik", "what": "Ostatnie 10 linii",                   "notes": "-n = ile linii. tail -1 = ostatnia linia"},
            {"cmd": "tail -f plik",    "what": "Sledz plik na zywo",                  "notes": "-f = follow. Nowe linie pojawiaja sie automatycznie. Ctrl+C zeby zatrzymac"},
            {"cmd": "wc -l plik",      "what": "Policz linie",                        "notes": "wc bez flag = linie slowa bajty naraz. -l = lines  -w = words  -c = bytes"},
            {"cmd": "wc -w plik",      "what": "Policz slowa",                        "notes": "Slowo = ciag znakow oddzielony spacjami"},
            {"cmd": "diff plik1 plik2","what": "Porownaj dwa pliki",                  "notes": "< = linia tylko w pierwszym pliku  > = tylko w drugim"},
        ],
        "boss": {
            "title": "CWICZENIE 2.2 — Czytacz",
            "description": "Bibliotekarz Lasu daje ci zwoj z 100 liniami — przeanalizuj go bez otwierania edytora:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "stworz folder na pliki",
                 "output": ""},
                {"type": "shell", "cmd": f"seq 1 100 > {QP}/numbers.txt",
                 "hint": "seq 1 100 = generuj liczby od 1 do 100  > = zapisz do pliku",
                 "output": ""},
                {"type": "shell", "cmd": f"wc -l {QP}/numbers.txt",
                 "hint": "Policz ile linii ma plik — powinno byc 100",
                 "output": f"     100 {QP}/numbers.txt"},
                {"type": "shell", "cmd": f"head -n 5 {QP}/numbers.txt",
                 "hint": "Pierwsze 5 linii — sprawdz ze plik zaczyna sie od 1",
                 "output": "1\n2\n3\n4\n5"},
                {"type": "shell", "cmd": f"tail -n 3 {QP}/numbers.txt",
                 "hint": "Ostatnie 3 linie — sprawdz ze plik konczy sie na 100",
                 "output": "98\n99\n100"},
                {"type": "shell", "cmd": f"head -n 55 {QP}/numbers.txt | tail -n 11",
                 "hint": "Linie 45-55: head bierze pierwsze 55, tail bierze ostatnie 11 z tych 55",
                 "output": "45\n46\n47\n48\n49\n50\n51\n52\n53\n54\n55"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj",
                 "output": ""},
                {"type": "shell", "cmd": f"ls ~ | grep quest-project",
                 "hint": "brak outputu = sukces",
                 "output": ""},
            ],
        },
    },

    {
        "id": "2.3",
        "world": 2,
        "is_boss": True,
        "world_name": "Las Plikow",
        "world_flavor": (
            "Tropiciel wie, ze nie wystarczy chodzic po lesie — trzeba umiec w nim szukac. "
            "find szuka plikow po nazwie, rozmiarze, dacie modyfikacji. "
            "grep szuka tekstu wewnatrz plikow. To dwa rozne narzedzia — oba bezcenne."
        ),
        "title": "Wyszukiwanie",
        "xp": 25,
        "theory": [
            {"cmd": "find . -name '*.txt'",  "what": "Znajdz pliki po nazwie",            "notes": ". = szukaj tutaj i w podkatalogach  * = dowolny ciag znakow"},
            {"cmd": "find . -type d",        "what": "Znajdz tylko katalogi",             "notes": "-type f = pliki  -type l = linki symboliczne  -type d = katalogi"},
            {"cmd": "find . -size +1M",      "what": "Znajdz pliki wieksze niz 1MB",      "notes": "+1M = wieksze  -1M = mniejsze  Jednostki: k, M, G"},
            {"cmd": "grep 'tekst' plik",     "what": "Szukaj tekstu w pliku",             "notes": "Wypisuje CALE linie zawierajace wzorzec"},
            {"cmd": "grep -r 'tekst' .",     "what": "Szukaj rekurencyjnie w katalogu",   "notes": "-r = recursive: przeszukuj wszystkie podkatalogi"},
            {"cmd": "grep -i 'tekst' plik",  "what": "Szukaj (ignoruj wielkosc liter)",   "notes": "-i = ignore case: 'Error' znajdzie ERROR, error, Error"},
            {"cmd": "grep -n 'tekst' plik",  "what": "Szukaj z numerami linii",           "notes": "-n = numery linii przy wynikach"},
            {"cmd": "which python3",         "what": "Gdzie jest zainstalowany program?", "notes": "Pokazuje pelna sciezke: /usr/bin/python3"},
        ],
        "boss": {
            "title": "BOSS FIGHT 2.3 — Tropiciel",
            "description": (
                "Straznik Lasu, stary tropiciel, wystawia cie na probe. "
                "Stworz projekt z trescia, znajdz pliki i przeszukaj je. Trzy zycia:"
            ),
            "steps": [
                {"type": "info",
                 "text": (
                     "Tropiciel mowi: 'Roznica miedzy find a grep:\n"
                     "  find  — szuka PLIKOW po nazwie, rozmiarze, dacie\n"
                     "  grep  — szuka TEKSTU wewnatrz plikow\n\n"
                     "Wildcards w find owijaj w cudzyslowy: find . -name '*.sh'\n"
                     "Bo bez cudzyslowow shell sam rozwinylby *.sh zanim find to zobaczy."
                 )},
                {"type": "shell", "cmd": f"mkdir -p {QP}/{{src/utils,docs,tests}}",
                 "hint": "stworz strukture katalogow",
                 "output": ""},
                {"type": "shell",
                 "cmd": f"echo $'TODO: fix bug\\nDONE: add feature\\nTODO: write tests' > {QP}/src/main.sh",
                 "hint": "$'...' = skladnia zsh dla \\n (nowa linia wewnatrz stringa)",
                 "output": ""},
                {"type": "shell",
                 "cmd": f"echo $'# Helper functions\\nTODO: implement helpers' > {QP}/src/utils/helpers.sh",
                 "hint": "drugi plik z trescia",
                 "output": ""},
                {"type": "shell", "cmd": f"find {QP} -name '*.sh'",
                 "hint": "Znajdz wszystkie pliki .sh w projekcie",
                 "output": f"{QP}/src/utils/helpers.sh\n{QP}/src/main.sh"},
                {"type": "shell", "cmd": f"grep -r 'TODO' {QP}",
                 "hint": "-r = przeszukaj wszystkie podkatalogi rekurencyjnie",
                 "output": (
                     f"{QP}/src/utils/helpers.sh:TODO: implement helpers\n"
                     f"{QP}/src/main.sh:TODO: fix bug\n"
                     f"{QP}/src/main.sh:TODO: write tests"
                 )},
                {"type": "shell", "cmd": f"grep -r 'TODO' {QP} | wc -l",
                 "hint": "| wc -l = policz ile linii wynikow zwrocil grep",
                 "output": "       3"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj",
                 "output": ""},
                {"type": "shell", "cmd": f"ls ~ | grep quest-project",
                 "hint": "brak outputu = sukces",
                 "output": ""},
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
        "world_flavor": (
            "Kopalnia ukrywa skarby gleboko — trzeba laczyc narzedzia jak wagoniki, "
            "kazdy przenoszacy output poprzedniego do wejscia nastepnego. "
            "Pipe | to filozofia Unixa: kazdy program robi JEDNA rzecz dobrze, ty je laczysz."
        ),
        "title": "Pipe — laczenie komend",
        "xp": 25,
        "theory": [
            {"cmd": "ls -la | less",                 "what": "Ogromna lista → przewijalna",        "notes": "| = przekaz stdout lewej komendy jako stdin prawej"},
            {"cmd": "ls -la | wc -l",                "what": "Ile plikow jest w katalogu?",        "notes": "wc -l liczy linie outputu ls"},
            {"cmd": "ls -la | grep '.txt'",          "what": "Tylko pliki .txt z listy",           "notes": "grep filtruje linie — wypisuje tylko te zawierajace wzorzec"},
            {"cmd": "ls -la | sort -k5 -n",          "what": "Posortuj po rozmiarze",              "notes": "-k5 = 5. kolumna (rozmiar w ls -la)  -n = numerycznie"},
            {"cmd": "history | grep 'cd' | tail -5", "what": "Ostatnie 5 komend z cd",            "notes": "Lancuch 3 komend! history → filtruj grep → ostatnie 5 tail"},
            {"cmd": "ps aux | grep chrome | wc -l",  "what": "Ile procesow chrome dziala?",       "notes": "Wynik zawiera tez sam grep — odejmij 1 od wyniku"},
        ],
        "boss": {
            "title": "CWICZENIE 3.1 — Lacznik",
            "description": "Gornik Potokow uczy cie laczyc komendy. Polacz je pipe'em:",
            "steps": [
                {"type": "shell", "cmd": "ls -la ~ | wc -l",
                 "hint": "Ile plikow/katalogow jest w twoim home?",
                 "output": "      32"},
                {"type": "shell", "cmd": "ls -la ~ | sort -k5 -rn | head -5",
                 "hint": "5 najwiekszych elementow w home: -r = odwrotnie  -n = numerycznie",
                 "output": (
                     f"drwxr-xr-x+  82 {USERNAME}  staff    2624 Apr  6 14:31 .\n"
                     f"drwxr-xr-x    5 root      admin     160 Jan 15 09:22 ..\n"
                     f"-rw-r--r--    1 {USERNAME}  staff   14562 Mar 28 16:45 .zsh_history\n"
                     f"drwx------   28 {USERNAME}  staff     896 Apr  5 11:30 Library\n"
                     f"drwxr-xr-x   17 {USERNAME}  staff     544 Apr  3 09:15 Downloads"
                 )},
                {"type": "shell", "cmd": "history | grep 'cd' | wc -l",
                 "hint": "Ile razy uzywales komendy cd? Trzy komendy w lancuchu",
                 "output": "      18"},
            ],
        },
    },

    {
        "id": "3.2",
        "world": 3,
        "is_boss": False,
        "world_name": "Kopalnia Potokow",
        "world_flavor": (
            "Kazda komenda ma trzy strumienie: stdin (wejscie), stdout (wyjscie), stderr (bledy). "
            "Przekierowania to klapki na tych strumieniach — decydujesz gdzie ida dane. "
            "> nadpisuje, >> dopisuje, 2> lapie bledy, /dev/null to wirtualny kosz."
        ),
        "title": "Przekierowania",
        "xp": 25,
        "theory": [
            {"cmd": ">",   "what": "Zapisz stdout do pliku (NADPISUJE!)",  "notes": "Tworzy plik jesli nie istnieje. Jesli istnieje — niszczy zawartosc bez pytania"},
            {"cmd": ">>",  "what": "Dopisz do pliku",                      "notes": "Nie niszczy istniejacych danych — dolicza na koniec"},
            {"cmd": "<",   "what": "Wczytaj z pliku jako stdin",           "notes": "sort < lista.txt to samo co sort lista.txt"},
            {"cmd": "2>",  "what": "Przekieruj stderr (bledy)",            "notes": "2>/dev/null = ignoruj bledy. /dev/null = wirtualny kosz"},
            {"cmd": "&>",  "what": "Przekieruj stdout I stderr razem",     "notes": "Skrot dla > plik 2>&1"},
            {"cmd": "tee", "what": "Wyswietl I zapisz jednoczesnie",       "notes": "Jak rozgaleznik Y — dane ida i na ekran i do pliku"},
        ],
        "boss": {
            "title": "CWICZENIE 3.2 — Przekierowania",
            "description": "Mistrz Przekierowan probuje twoja wiedze o strumieniach danych:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "stworz folder",
                 "output": ""},
                {"type": "shell", "cmd": f"ls -la ~ > {QP}/listing.txt",
                 "hint": "> = zapisz stdout do pliku (nadpisuje jesli istnieje)",
                 "output": ""},
                {"type": "shell", "cmd": f"echo '# Moja lista' >> {QP}/listing.txt",
                 "hint": ">> = dopisz na koniec (nie nadpisuje istniejacych danych)",
                 "output": ""},
                {"type": "shell", "cmd": f"wc -l < {QP}/listing.txt",
                 "hint": "< = uzyj pliku jako stdin komendy",
                 "output": "      33"},
                {"type": "shell", "cmd": "find / -name '*.conf' 2>/dev/null | head -5",
                 "hint": "2>/dev/null = ignoruj bledy braku dostepu do katalogow systemowych",
                 "output": "/etc/ntp.conf\n/etc/resolv.conf\n/etc/pf.conf\n/private/etc/apache2/httpd.conf\n/private/etc/paths.d/10-pkgsrc.conf"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj",
                 "output": ""},
            ],
        },
    },

    {
        "id": "3.3",
        "world": 3,
        "is_boss": True,
        "world_name": "Kopalnia Potokow",
        "world_flavor": (
            "Na dnie kopalni kryja sie najpotezniejsze narzedzia. "
            "sort, uniq, cut, sed, awk — w reku mistrza tworza jednolinijkowe programy "
            "zdolne przeanalizowac gigabajtowe logi w sekunde."
        ),
        "title": "Potezne narzedzia tekstowe",
        "xp": 30,
        "theory": [
            {"cmd": "sort",              "what": "Sortuj alfabetycznie",                  "notes": "-n = numerycznie  -r = odwrotnie  -rn = od najwiekszego"},
            {"cmd": "uniq",              "what": "Usun sasiadujace duplikaty",             "notes": "ZAWSZE poprzedz sort! uniq nie widzi duplikatow ktore nie sasiaduja"},
            {"cmd": "uniq -c",           "what": "Policz wystapienia",                    "notes": "-c = count: dodaje licznik przed kazdym wierszem"},
            {"cmd": "cut -d: -f1",       "what": "Wytnij kolumne",                        "notes": "-d = delimiter  -f1 = pierwsza kolumna"},
            {"cmd": "tr 'a-z' 'A-Z'",   "what": "Zamien znaki (male na duze)",           "notes": "Tylko z pipe — nie przyjmuje pliku bezposrednio"},
            {"cmd": "sed 's/old/new/g'", "what": "Znajdz i zamien tekst",                 "notes": "s = substitute  g = global (wszystkie w linii)"},
            {"cmd": "awk '{print $1}'",  "what": "Wypisz pierwsza kolumne",               "notes": "$1 = pierwsza kolumna  $NF = ostatnia  -F: = separator :"},
            {"cmd": "xargs",             "what": "Zamien stdin na argumenty",             "notes": "find . -name '*.tmp' | xargs rm"},
        ],
        "boss": {
            "title": "BOSS FIGHT 3.3 — Wielki Boss Kopalni: Analiza logow",
            "description": (
                "Wielki Gornik rzuca ci wyzwanie: stworz log serwera i przeanalizuj go jak prawdziwy administrator. "
                "Trzy zycia — kazda komenda musi byc precyzyjna:"
            ),
            "steps": [
                {"type": "info",
                 "text": (
                     "Zadanie: analiza logow dostepow do serwera HTTP.\n\n"
                     "Schemat logu: IP METODA SCIEZKA KOD_HTTP\n"
                     "Bedziesz szukac:\n"
                     "  1. Ktore IP wyslalo najwiecej requestow\n"
                     "  2. Ktore requesty skonczyly sie bledem (kody 4xx i 5xx)\n\n"
                     "Klucz: cut → sort → uniq -c → sort -rn to klasyczny lancuch zliczajacy wystapienia."
                 )},
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "przygotuj folder",
                 "output": ""},
                {"type": "shell",
                 "cmd": f"printf '192.168.1.1 GET /index.html 200\\n10.0.0.5 GET /about.html 200\\n192.168.1.1 POST /login 401\\n10.0.0.5 GET /dashboard 200\\n172.16.0.1 GET /index.html 404\\n10.0.0.5 GET /api/data 500\\n' > {QP}/access.log",
                 "hint": "printf tworzy plik logu z 6 wpisami — format: IP METODA SCIEZKA KOD",
                 "output": ""},
                {"type": "shell", "cmd": f"cut -d' ' -f1 {QP}/access.log | sort | uniq -c | sort -rn",
                 "hint": "Ktore IP ma najwiecej requestow? cut→sort→uniq -c→sort -rn",
                 "output": "   3 10.0.0.5\n   2 192.168.1.1\n   1 172.16.0.1"},
                {"type": "shell", "cmd": f"grep -E ' [45][0-9]{{2}}$' {QP}/access.log",
                 "hint": "Bledy 4xx i 5xx: -E = extended regex  [45] = 4 lub 5  $ = koniec linii",
                 "output": "192.168.1.1 POST /login 401\n172.16.0.1 GET /index.html 404\n10.0.0.5 GET /api/data 500"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj",
                 "output": ""},
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
        "world_flavor": (
            "Na dnie Wiezy Edytora nauczysz sie ze nie zawsze trzeba wchodzic do srodka. "
            "Czesto mozna zmodyfikowac plik z zewnatrz jednym poleceniem. "
            "echo, sed, printf — szybsze niz otwieranie edytora gdy zmiana jest mala."
        ),
        "title": "Edycja bez edytora",
        "xp": 15,
        "theory": [
            {"cmd": "echo 'tekst' > plik.txt",       "what": "Stworz plik z trescia (nadpisuje)",  "notes": "> nadpisuje — jesli plik istnieje, poprzednia zawartosc znika"},
            {"cmd": "echo 'wiecej' >> plik.txt",      "what": "Dopisz na koniec pliku",             "notes": "Bezpieczne — nie niszczy istniejacych danych"},
            {"cmd": "cat > plik.txt",                 "what": "Wpisuj z klawiatury do pliku",       "notes": "Ctrl+D = koniec (EOF = End Of File) — zapisuje"},
            {"cmd": "sed -i 's/stare/nowe/g' plik",  "what": "Zamien tekst w pliku (in-place)",    "notes": "-i = in-place: modyfikuje sam plik. Na macOS: sed -i '' 's/...' plik"},
            {"cmd": "sed -n '5,10p' plik",            "what": "Wypisz linie 5-10",                  "notes": "-n = nie wypisuj domyslnie  p = print dla zakresu"},
            {"cmd": "printf 'linia1\\nlinia2\\n'",    "what": "Wypisz tekst z interpretacja \\n",  "notes": "printf rozumie \\n jako nowa linia"},
        ],
        "boss": {
            "title": "CWICZENIE 4.1 — Edycja bez edytora",
            "description": "Czlowiek bez edytora na dolnym poziomie Wiezy — manipuluj plikami bez otwierania czegolwiek:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "stworz folder",
                 "output": ""},
                {"type": "shell", "cmd": f"printf 'imie: {USERNAME}\\nhost: {HOSTNAME}\\ndata: 2026\\n' > {QP}/info.txt",
                 "hint": "printf z \\n tworzy wieloliniowy plik od razu",
                 "output": ""},
                {"type": "shell", "cmd": f"cat {QP}/info.txt",
                 "hint": "sprawdz zawartosc pliku — powinny byc 3 linie",
                 "output": f"imie: {USERNAME}\nhost: {HOSTNAME}\ndata: 2026"},
                {"type": "shell", "cmd": f"echo 'system: macOS' >> {QP}/info.txt",
                 "hint": ">> = dopisz na koniec bez nadpisywania",
                 "output": ""},
                {"type": "shell", "cmd": f"sed -i '' 's/2026/$(date +%Y)/g' {QP}/info.txt",
                 "hint": "sed -i '' na macOS (pusty string po -i = brak backupu)",
                 "output": ""},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj",
                 "output": ""},
            ],
        },
    },

    {
        "id": "4.2",
        "world": 4,
        "is_boss": False,
        "world_name": "Wieza Edytora",
        "world_flavor": (
            "Pierwsze pietro Wiezy: nano. Prosty, przyjazny, ze skrotami widocznymi na dole. "
            "^ oznacza Ctrl. Idealne dla poczatkujacych i szybkich poprawek. "
            "Nie musisz go kochac — wystarczy ze umiesz wyjsc i zapisac."
        ),
        "title": "Nano — latwiejszy start",
        "xp": 15,
        "theory": [
            {"cmd": "nano plik.txt", "what": "Otworz plik (stworzy jesli nie istnieje)", "notes": "Skroty widoczne na dole ekranu. ^ = Ctrl"},
            {"cmd": "Ctrl+O",        "what": "Zapisz (O jak Output/Write Out)",          "notes": "Enter potwierdza nazwe pliku"},
            {"cmd": "Ctrl+X",        "what": "Wyjdz",                                   "notes": "Jesli sa niezapisane zmiany — zapyta: Y = tak, N = nie"},
            {"cmd": "Ctrl+W",        "what": "Szukaj tekstu",                           "notes": "Enter = nastepny wynik"},
            {"cmd": "Ctrl+K",        "what": "Wytnij cala linie",                       "notes": ""},
            {"cmd": "Ctrl+U",        "what": "Wklej wycieta linie (UnCut)",             "notes": "Tandem z Ctrl+K — wytnij i wklej to kopiowanie linii"},
            {"cmd": "Ctrl+G",        "what": "Pomoc — pelna lista skrotow",             "notes": "Q lub Ctrl+X zeby wyjsc z pomocy"},
        ],
        "boss": {
            "title": "CWICZENIE 4.2 — Nano",
            "description": "Stroz pierwszego pietra daje ci prosty sprawdzian z nano:",
            "steps": [
                {"type": "info",
                 "text": "Otworz nano: nano ~/quest-nano.txt\nWpisz dowolny tekst, zapisz Ctrl+O + Enter, wyjdz Ctrl+X"},
                {"type": "shell", "cmd": "cat ~/quest-nano.txt",
                 "hint": "Sprawdz ze plik zostal zapisany — powinienes zobaczyc swoj tekst",
                 "output": "[Twoj tekst zapisany w nano]\n[Nano dziala poprawnie!]"},
                {"type": "shell", "cmd": "rm ~/quest-nano.txt",
                 "hint": "posprzataj",
                 "output": ""},
            ],
        },
    },

    {
        "id": "4.3",
        "world": 4,
        "is_boss": True,
        "world_name": "Wieza Edytora",
        "world_flavor": (
            "Na szczycie Wiezy mieszka Vim — legendarny edytor z 1976 roku, uzywany przez miliony do dzis. "
            "Trudny na poczatku, ale po opanowaniu szybszy od kazdego innego. "
            "Jego sekret: tryby. Normal to podstawa, Insert to pisanie, :komenda to akcje."
        ),
        "title": "Vim — bron legendarna",
        "xp": 40,
        "theory": [
            {"cmd": "i",       "what": "Wejdz w INSERT mode — tu mozesz pisac",        "notes": "Po otwarciu Vima JESTES w NORMAL mode i NIE mozesz pisac!"},
            {"cmd": "ESC",     "what": "Wroc do NORMAL mode — zawsze bezpieczny",      "notes": "Nie wiesz w jakim trybie jestes? Nacisnij ESC kilka razy"},
            {"cmd": ":w",      "what": "Zapisz plik",                                  "notes": "Musi byc w NORMAL mode. Jesli plik nie ma nazwy: :w nazwa.txt"},
            {"cmd": ":q",      "what": "Wyjdz",                                        "notes": "Blad jesli sa niezapisane zmiany"},
            {"cmd": ":wq",     "what": "Zapisz i wyjdz",                               "notes": "Najczesciej uzywane. Alternatywa: ZZ w NORMAL mode"},
            {"cmd": ":q!",     "what": "Wyjdz BEZ zapisu",                             "notes": "! = na sile. Awaryjna ucieczka"},
            {"cmd": "h j k l", "what": "Nawigacja: lewo dol gora prawo",               "notes": "Jak strzalki ale rece nie opuszczaja home row"},
            {"cmd": "gg / G",  "what": "Poczatek / koniec pliku",                      "notes": "gg = pierwsza linia  G = ostatnia  5G = skocz do linii 5"},
            {"cmd": "/tekst",  "what": "Szukaj w dol",                                 "notes": "n = nastepny wynik  N = poprzedni"},
            {"cmd": "dd",      "what": "Usun (wytnij) cala linie",                     "notes": "3dd = usun 3 linie"},
            {"cmd": "yy / p",  "what": "Kopiuj linie / wklej ponizej",                 "notes": "y = yank (kopiuj)  p = paste ponizej"},
            {"cmd": "u",       "what": "Cofnij (undo)",                                "notes": "Ctrl+R = ponow (redo)"},
        ],
        "boss": {
            "title": "BOSS FIGHT 4.3 — Wiezmistrz Edytora",
            "description": (
                "Wiezmistrz wskazuje na terminal: "
                "'Nie ma skrotow do nauki Vima. Jest tylko vimtutor.' "
                "Trzy zycia:"
            ),
            "steps": [
                {"type": "info",
                 "text": (
                     "Uruchom: vimtutor\n\n"
                     "vimtutor to interaktywny samouczek wbudowany w Vima.\n"
                     "Tworzy tymczasowy plik — nie musisz nic czyscic po zakonczeniu.\n"
                     "Czas: ok. 30 minut.\n\n"
                     "Najwazniejsze lekcje z vimtutor:\n"
                     "  :q!  — wyjdz bez zapisu\n"
                     "  :wq  — zapisz i wyjdz\n"
                     "  i    — wejdz w tryb pisania\n"
                     "  ESC  — wroc do trybu normalnego"
                 )},
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
        "world_flavor": (
            "Twierdza ma straznikow i klucze do kazdych drzwi. "
            "W systemie Unix kazdy zasob ma wlasciciela i prawa dostepu. "
            "sudo to klucz do bram krolewskich — daje chwilowa moc administratora. Uzywaj ostroznie."
        ),
        "title": "sudo i uzytkownicy",
        "xp": 15,
        "theory": [
            {"cmd": "whoami",         "what": "Aktualna nazwa uzytkownika",            "notes": f"Twoj: {USERNAME}"},
            {"cmd": "id",             "what": "UID, GID i grupy uzytkownika",          "notes": "UID=0 to root (administrator)"},
            {"cmd": "groups",         "what": "Do jakich grup naleze?",               "notes": "Czlonek grupy 'admin' = mozesz uzywac sudo"},
            {"cmd": "sudo komenda",   "what": "Uruchom komende jako root",            "notes": "Superuser Do. Pyta o twoje haslo"},
            {"cmd": "sudo -l",        "what": "Jakie komendy moge uruchamiac sudo?",  "notes": "-l = list"},
            {"cmd": "su - uzytkownik","what": "Przelacz sie na innego uzytkownika",   "notes": "su = switch user. - = zaladuj jego profil shellowy"},
            {"cmd": "last",           "what": "Historia logowan do systemu",          "notes": "Kiedy i skad sie logowali uzytkownicy"},
        ],
        "boss": {
            "title": "CWICZENIE 5.1 — Wywiad o uzytkownikach",
            "description": "Kapitan Twierdzy sprawdza czy znasz system uprawnien:",
            "steps": [
                {"type": "shell", "cmd": "id",
                 "hint": f"Wypisuje UID uzytkownika {USERNAME}, GID i wszystkie grupy",
                 "output": f"uid=501({USERNAME}) gid=20(staff) groups=20(staff),12(everyone),61(localaccounts),79(_appserverusr),80(admin),81(_appserveradm),98(_lpadmin)"},
                {"type": "shell", "cmd": "groups",
                 "hint": "Pokaz do jakich grup nalezysz — szukaj 'admin' lub 'wheel'",
                 "output": f"staff everyone localaccounts _appserverusr admin _appserveradm _lpadmin _developer _analyticsusers"},
                {"type": "shell", "cmd": "sudo -l",
                 "hint": "Sprawdz jakie uprawnienia sudo masz",
                 "output": f"User {USERNAME} may run the following commands on {HOSTNAME}:\n    (ALL) ALL"},
            ],
        },
    },

    {
        "id": "5.2",
        "world": 5,
        "is_boss": False,
        "world_name": "Twierdza Uprawnien",
        "world_flavor": (
            "Dziewiec liter ktore decyduja o wszystkim: rwxrwxrwx. "
            "r = czytaj, w = pisz, x = wykonuj. Trzy grupy: wlasciciel, jego grupa, wszyscy inni. "
            "chmod zmienia te prawa — chmod 755 to klasyczne uprawnienia dla programow."
        ),
        "title": "Uprawnienia plikow",
        "xp": 25,
        "theory": [
            {"cmd": "ls -la",           "what": "Pokaz uprawnienia plikow",             "notes": "Format: -rwxr-xr-- = typ|wlasciciel|grupa|inni"},
            {"cmd": "chmod 755 plik",   "what": "Ustaw uprawnienia liczbowo",            "notes": "r=4 w=2 x=1. 7=rwx 5=r-x 4=r--. 755 = wlasciciel wszystko, reszta czyta i wykonuje"},
            {"cmd": "chmod 644 plik",   "what": "Typowe uprawnienia dla plikow",        "notes": "644 = rw-r--r-- : wlasciciel czyta+pisze, reszta tylko czyta"},
            {"cmd": "chmod +x plik",    "what": "Dodaj prawo wykonywania",              "notes": "+x = dla wszystkich  u+x = tylko wlasciciel"},
            {"cmd": "chmod u+w plik",   "what": "Dodaj pisanie dla wlasciciela",        "notes": "u = user  g = group  o = others  a = all"},
            {"cmd": "sudo chown u:g p", "what": "Zmien wlasciciela i grupe",            "notes": "Wymaga sudo. chown user:group plik"},
        ],
        "boss": {
            "title": "CWICZENIE 5.2 — Straznik Uprawnien",
            "description": "Straznik Twierdzy pokazuje ci plik i kaduze sprawdzic i zmienic jego uprawnienia:",
            "steps": [
                {"type": "shell", "cmd": f"touch {HOME}/quest-perm.sh",
                 "hint": "stworz plik testowy",
                 "output": ""},
                {"type": "shell", "cmd": f"ls -la {HOME}/quest-perm.sh",
                 "hint": "sprawdz uprawnienia — domyslnie rw-r--r-- (644)",
                 "output": f"-rw-r--r--  1 {USERNAME}  staff  0 Apr  6 14:32 {HOME}/quest-perm.sh"},
                {"type": "shell", "cmd": f"chmod +x {HOME}/quest-perm.sh",
                 "hint": "+x = dodaj prawo wykonywania dla wszystkich",
                 "output": ""},
                {"type": "shell", "cmd": f"chmod 600 {HOME}/quest-perm.sh",
                 "hint": "600 = rw------- : tylko ty mozesz czytac i pisac",
                 "output": ""},
                {"type": "shell", "cmd": f"ls -la {HOME}/quest-perm.sh",
                 "hint": "potwierdz zmiane uprawnien — powinno byc rw-------",
                 "output": f"-rw-------  1 {USERNAME}  staff  0 Apr  6 14:32 {HOME}/quest-perm.sh"},
                {"type": "shell", "cmd": f"rm {HOME}/quest-perm.sh",
                 "hint": "posprzataj",
                 "output": ""},
            ],
        },
    },

    {
        "id": "5.3",
        "world": 5,
        "is_boss": True,
        "world_name": "Twierdza Uprawnien",
        "world_flavor": (
            "Kazdy profesjonalny wojownik personalizuje swoja zbroje. "
            "Zmienne srodowiskowe to twoja konfiguracja sesji — PATH mowi gdzie szukac programow. "
            "Aliasy to skroty do ulubionych komend, ~/.zshrc to twoj osobisty grimuar."
        ),
        "title": "Zmienne i aliasy",
        "xp": 20,
        "theory": [
            {"cmd": "echo $HOME",        "what": f"Twoj katalog domowy ({HOME})",       "notes": "$HOME, $USER, $PATH to zmienne systemowe dostepne zawsze"},
            {"cmd": "echo $PATH",        "what": "Gdzie system szuka programow",        "notes": "Lista katalogow oddzielona :"},
            {"cmd": "echo $USER",        "what": f"Twoja nazwa uzytkownika ({USERNAME})","notes": "$USER = whoami ale szybciej (bez uruchamiania procesu)"},
            {"cmd": "export VAR='val'",  "what": "Ustaw zmienna dla tej sesji",         "notes": "Bez export = tylko w biezacym shellu"},
            {"cmd": "source ~/.zshrc",   "what": "Przeladuj konfiguracje bez restartu", "notes": "Po dodaniu aliasu do .zshrc musisz source zeby zaczal dzialac"},
            {"cmd": "alias ll='ls -laG'","what": "Stworz skrot do komendy",            "notes": "-G = kolory na macOS. Alias zyje tylko w sesji — zeby byl staly, dodaj do ~/.zshrc"},
        ],
        "boss": {
            "title": "BOSS FIGHT 5.3 — Konfiguracja Powloki",
            "description": (
                "Komandant Twierdzy wymaga personalizacji — dowiedz sie o swoim srodowisku i skonfiguruj je. "
                "Trzy zycia:"
            ),
            "steps": [
                {"type": "info",
                 "text": (
                     "Zadanie: zbadaj swoje srodowisko i stworz uzyteczny alias.\n\n"
                     "PATH to sciezka wyszukiwania programow.\n"
                     "Alias to skrot — ll='ls -laG' pozwala pisac 'll' zamiast 'ls -laG'.\n"
                     "Aliasy zyja tylko w sesji chyba ze zapiszesz je do ~/.zshrc."
                 )},
                {"type": "shell", "cmd": "echo $PATH | tr ':' '\\n'",
                 "hint": "Pokaz PATH czytelnie — tr ':' '\\n' zamienia : na nowe linie",
                 "output": f"/opt/homebrew/bin\n/opt/homebrew/sbin\n/usr/local/bin\n/usr/bin\n/bin\n/usr/sbin\n/sbin\n{HOME}/.cargo/bin"},
                {"type": "shell", "cmd": "alias ll='ls -laG'",
                 "hint": "Stworz tymczasowy alias ll  -G = kolory na macOS",
                 "output": ""},
                {"type": "shell", "cmd": "ll ~",
                 "hint": "Przetestuj alias — powinien dzialac jak 'ls -laG ~'",
                 "output": (
                     f"total 256\n"
                     f"drwxr-xr-x+  82 \033[34m{USERNAME}\033[m  staff   2624 Apr  6 14:31 \033[34m.\033[m\n"
                     f"drwxr-xr-x    5 root      admin    160 Jan 15 09:22 \033[34m..\033[m\n"
                     f"-rw-r--r--    1 {USERNAME}  staff  14562 Apr  6 14:31 .zsh_history\n"
                     f"drwx------   28 \033[34m{USERNAME}\033[m  staff    896 Apr  5 11:30 \033[34m.config\033[m\n"
                     f"drwxr-xr-x    4 \033[34m{USERNAME}\033[m  staff    128 Mar 15 09:15 \033[34mDesktop\033[m\n"
                     f"drwxr-xr-x   12 \033[34m{USERNAME}\033[m  staff    384 Apr  5 11:30 \033[34mDocuments\033[m\n"
                     f"drwxr-xr-x   17 \033[34m{USERNAME}\033[m  staff    544 Apr  3 09:15 \033[34mDownloads\033[m"
                 )},
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
        "world_flavor": (
            "Labirynt Procesow to miasto nigdy nie spiacych demonow. "
            "Kazdy uruchomiony program to demon z unikalnym ID (PID). "
            "Dzisiaj nie walczysz — obserwujesz. ps i top to twoje oczy w tym chaosie."
        ),
        "title": "Obserwacja procesow",
        "xp": 15,
        "theory": [
            {"cmd": "ps",             "what": "Procesy biezacej sesji terminala",       "notes": "Bez argumentow — tylko procesy twojego terminala"},
            {"cmd": "ps aux",         "what": "WSZYSTKIE procesy systemu",              "notes": "a = wszyscy uzytkownicy  u = format czytelny  x = procesy bez terminala"},
            {"cmd": f"ps aux | grep {USERNAME}", "what": "Procesy konkretnego uzytkownika", "notes": f"Podmien {USERNAME} na dowolna nazwe"},
            {"cmd": "top -o cpu",     "what": "Monitor na zywo — sortuj po CPU",       "notes": "q = wyjdz  -o cpu/mem = kolumna sortowania"},
            {"cmd": "uptime",         "what": "Czas pracy systemu + obciazenie",        "notes": "load avg: srednie z 1, 5 i 15 minut"},
            {"cmd": "echo $$",        "what": "PID biezacego procesu shella",           "notes": "$$ = zmienna specjalna. $! = PID ostatnio uruchomionego w tle"},
        ],
        "boss": {
            "title": "CWICZENIE 6.1 — Obserwator",
            "description": "Przewodnik po Labiryncie uczy cie obserwowac bez interwencji:",
            "steps": [
                {"type": "shell", "cmd": "uptime",
                 "hint": "Sprawdz jak dlugo system dziala i srednie obciazenie CPU",
                 "output": "14:32  up 3 days,  2:15, 2 users, load averages: 1.23 0.87 0.76"},
                {"type": "shell", "cmd": "ps aux | wc -l",
                 "hint": "Policz ile procesow dziala w systemie",
                 "output": "     342"},
                {"type": "shell", "cmd": f"ps aux | grep {USERNAME}",
                 "hint": f"Znajdz wszystkie procesy uzytkownika {USERNAME}",
                 "output": (
                     f"{USERNAME}   1234   0.0  0.1 4353456  16384   ??  S  Mon12PM   0:01.23 /sbin/launchd\n"
                     f"{USERNAME}   5678   0.0  0.2 5678900  32768   ??  S  Mon12PM   1:23.45 /usr/local/bin/python3\n"
                     f"{USERNAME}  91011   0.0  0.0 4292548   4096 s001  S+  2:31PM   0:00.01 -zsh"
                 )},
                {"type": "shell", "cmd": "echo $$",
                 "hint": "Wypisz PID biezacego shella",
                 "output": "91234"},
            ],
        },
    },

    {
        "id": "6.2",
        "world": 6,
        "is_boss": True,
        "world_name": "Labirynt Procesow",
        "world_flavor": (
            "Czas wziac rzeczy w swoje rece. Uruchomisz demona, znajdziesz go i wyeliminujesz. "
            "& wysyla proces do tla, jobs pokazuje liste, kill wysyla sygnal. "
            "SIGTERM = prosba o zakonczenie, SIGKILL (-9) = natychmiastowe unicestwienie."
        ),
        "title": "Zarzadzanie procesami",
        "xp": 25,
        "theory": [
            {"cmd": "komenda &",      "what": "Uruchom w tle",                         "notes": "& na koncu — shell od razu wraca do promptu. Wypisuje [numer_joba] PID"},
            {"cmd": "Ctrl+Z",         "what": "Zawies biezacy proces",                 "notes": "Zatrzymuje (nie zabija) — mozna wznowic przez bg lub fg"},
            {"cmd": "bg / fg",        "what": "Wznow w tle / przywroc na pierwszy plan","notes": "bg %1 = wznow job 1 w tle  fg %1 = przywroc na foreground"},
            {"cmd": "jobs -l",        "what": "Lista procesow w tle z PID",            "notes": "-l = long (pokaz PID). Numer joba (%1) rozny od PID"},
            {"cmd": "kill PID",       "what": "Grzeczna prosba o zakonczenie",         "notes": "Wysyla SIGTERM (15) — proces moze ignorowac"},
            {"cmd": "kill -9 PID",    "what": "Natychmiastowe zabicie",                "notes": "-9 = SIGKILL. Nie mozna zignorowac. Ostatecznosc"},
            {"cmd": "kill %1",        "what": "Zabij pierwszy job z listy jobs",       "notes": "%1 = numer joba z 'jobs', nie PID"},
            {"cmd": "lsof -i :8080",  "what": "Co uzywa portu 8080?",                 "notes": "Gdy 'port is already in use'"},
        ],
        "boss": {
            "title": "BOSS FIGHT 6.2 — Pogromca Procesow",
            "description": (
                "Wielki Demon Labiryntu wymaga dowodu mestwa — uruchom demona, znajdz go i wyeliminuj. "
                "Trzy zycia:"
            ),
            "steps": [
                {"type": "info",
                 "text": (
                     "Roznica miedzy numerem joba a PID:\n"
                     "  jobs -l  wypisuje: [1] 12345 Running   sleep 300\n"
                     "           [1]   = numer joba (lokalne id w tej sesji)\n"
                     "           12345 = PID (globalny id procesu w systemie)\n\n"
                     "  kill %1    zabija po numerze joba (szybciej)\n"
                     "  kill 12345 zabija po PID\n\n"
                     "sleep 300 = usnij na 300 sekund — idealny demon testowy."
                 )},
                {"type": "shell", "cmd": "sleep 300 &",
                 "hint": "& = uruchom w tle. Shell od razu wraca do promptu",
                 "output": "[1] 12345"},
                {"type": "shell", "cmd": "jobs -l",
                 "hint": "Pokaz liste procesow w tle z PID — -l dodaje kolumne z numerem PID",
                 "output": "[1]+ 12345 Running                 sleep 300"},
                {"type": "shell", "cmd": "kill %1",
                 "hint": "%1 = pierwszy job z listy jobs (wygodniejsze niz szukanie PID)",
                 "output": ""},
                {"type": "shell", "cmd": "jobs",
                 "hint": "Lista powinna byc pusta lub pokazywac '[1] Terminated'",
                 "output": "[1]+  Terminated              sleep 300"},
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
        "world_flavor": (
            "W Kuzni Skryptow nauczysz sie jak kazac shellowi myslec. "
            "Zmienne przechowuja dane, substytucje wstawiaja wyniki komend w srodku stringow, "
            "(( )) liczy jak kalkulator. To klocki z ktorych budujesz automatyzacje."
        ),
        "title": "Zmienne i substytucje",
        "xp": 15,
        "theory": [
            {"cmd": "ZMIENNA='wartosc'",        "what": "Przypisz wartosc (brak spacji przy =!)",  "notes": "BLAD: ZMIENNA = 'x'  DOBRZE: ZMIENNA='x'"},
            {"cmd": "echo $ZMIENNA",             "what": "Odczytaj wartosc zmiennej",              "notes": "$ = odwolanie"},
            {"cmd": "echo ${ZMIENNA:-domyslna}", "what": "Wartosc domyslna jesli pusta",           "notes": ":- = jesli pusta lub niezdefiniowana, uzyj wartosci po :-"},
            {"cmd": "echo $(komenda)",           "what": "Wstaw wynik komendy (command subst.)",   "notes": f"np. echo \"Dzis: $(date +%A)\""},
            {"cmd": "echo $((5 * 7))",           "what": "Obliczenia arytmetyczne",                "notes": "(( )) = kontekst matematyczny. Tylko liczby calkowite"},
            {"cmd": "read -p 'Imie: ' IMIE",    "what": "Pobierz input od uzytkownika",           "notes": "-p = prompt (wyswietl pytanie przed czekaniem)"},
            {"cmd": "unset ZMIENNA",             "what": "Usun zmienna",                           "notes": "Po unset, echo $ZMIENNA = pusty ciag"},
        ],
        "boss": {
            "title": "CWICZENIE 7.1 — Zmienne",
            "description": "Kowal probuje twoje klocki — cwicz zmienne i substytucje:",
            "steps": [
                {"type": "shell", "cmd": f"IMIE='{USERNAME}' && echo \"Witaj, $IMIE!\"",
                 "hint": "Przypisz zmienna i wypisz z substytucja. && = wykonaj drugie tylko jesli pierwsze OK",
                 "output": f"Witaj, {USERNAME}!"},
                {"type": "shell", "cmd": "echo $((3 * 14))",
                 "hint": "Oblicz 3 * 14 uzywajac arytmetyki powloki (( ))",
                 "output": "42"},
                {"type": "shell", "cmd": "echo \"Teraz jest $(date +%H:%M) na ${HOSTNAME:-komputerze}\"",
                 "hint": "$(date +%H:%M) = wstaw aktualny czas  ${HOSTNAME:-...} = zmienna lub default",
                 "output": f"Teraz jest 14:32 na {HOSTNAME}"},
            ],
        },
    },

    {
        "id": "7.2",
        "world": 7,
        "is_boss": True,
        "world_name": "Kuznia Skryptow",
        "world_flavor": (
            "Teraz odlejesz swoja pierwsza bron. Skrypt to plik tekstowy z komendami i logika — "
            "raz napisany dziala tysiac razy bez nadzoru. "
            "Shebang na gorze mowi systemowi jak czytac plik. chmod +x obudza go do zycia."
        ),
        "title": "Pierwszy skrypt",
        "xp": 30,
        "theory": [
            {"cmd": "#!/bin/bash",       "what": "Shebang — pierwsza linia skryptu",   "notes": "Mowi systemowi jakiego interpretera uzyc. Musi byc w linii 1"},
            {"cmd": "NAME='Zenon'",      "what": "Zmienna",                             "notes": "Brak spacji przy =! $NAME = odczyt wartosci"},
            {"cmd": "echo \"$NAME\"",    "what": "Wypisz zmienna",                     "notes": "Podwojne cudzyslowy interpretuja zmienne i $()"},
            {"cmd": "$0 $1 $#",          "what": "Argumenty skryptu",                  "notes": "$0 = nazwa skryptu  $1 = pierwszy argument  $# = liczba argumentow"},
            {"cmd": "if [ -f $1 ]",      "what": "Sprawdz czy plik istnieje",          "notes": "-f = plik  -d = katalog  -z = pusty string  -e = cokolwiek"},
            {"cmd": "for i in 1 2 3",    "what": "Petla for",                          "notes": "for i in $(seq 1 10) = petla 1-10. done = koniec petli"},
            {"cmd": "$(( count + 1 ))",  "what": "Obliczenia arytmetyczne",            "notes": "count=$((count+1)) = inkrementacja zmiennej"},
            {"cmd": "chmod +x skrypt.sh","what": "Nadaj prawo wykonywania",            "notes": "Tylko raz! Potem uruchamiac: ./skrypt.sh"},
        ],
        "boss": {
            "title": "BOSS FIGHT 7.2 — Kowal Skryptow",
            "description": (
                "Mistrz Kuzni wymaga odlewu pierwszej broni. "
                "Napisz skrypt, nadaj mu prawa, uruchom. Trzy zycia:"
            ),
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "stworz folder na skrypt",
                 "output": ""},
                {"type": "info",
                 "text": (
                     f"Napisz skrypt w nano: nano {QP}/hello.sh\n\n"
                     "Wpisz dokladnie to:\n"
                     "#!/bin/bash\n"
                     "NAME=${1:-'Nieznajomy'}\n"
                     "echo \"Witaj, $NAME!\"\n"
                     "echo \"Uzytkownik: $(whoami)\"\n"
                     "echo \"Host: $(hostname)\"\n"
                     "echo \"Data: $(date '+%Y-%m-%d')\"\n\n"
                     "Zapisz: Ctrl+O + Enter, wyjdz: Ctrl+X"
                 )},
                {"type": "shell", "cmd": f"chmod +x {QP}/hello.sh",
                 "hint": "nadaj prawo wykonywania — bez tego shell odmowi uruchomienia",
                 "output": ""},
                {"type": "shell", "cmd": f"{QP}/hello.sh",
                 "hint": "uruchom bez argumentu — zobaczysz 'Witaj, Nieznajomy!'",
                 "output": f"Witaj, Nieznajomy!\nUzytkownik: {USERNAME}\nHost: {HOSTNAME}\nData: 2026-04-06"},
                {"type": "shell", "cmd": f"{QP}/hello.sh {USERNAME}",
                 "hint": f"uruchom z argumentem — zobaczysz 'Witaj, {USERNAME}!'",
                 "output": f"Witaj, {USERNAME}!\nUzytkownik: {USERNAME}\nHost: {HOSTNAME}\nData: 2026-04-06"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj",
                 "output": ""},
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
        "world_flavor": (
            "Swiatynia Sieci skrywa tajemnice polaczen miedzy maszynami. "
            "Zanim zaczniesz atakowac zdalne serwery, opanuj diagnostyke: "
            "czy jest polaczenie? Jakie IP? Jaka latencja? ping, ifconfig, host — narzedzia zwiadowcy."
        ),
        "title": "Diagnostyka sieci",
        "xp": 15,
        "theory": [
            {"cmd": "ping -c 3 1.1.1.1",   "what": "Sprawdz polaczenie (3 pakiety)",     "notes": "1.1.1.1 = Cloudflare DNS, zawsze online. -c = count. time = latencja w ms"},
            {"cmd": "hostname",             "what": "Nazwa twojego komputera",             "notes": f"Twoj: {HOSTNAME}"},
            {"cmd": "ifconfig | grep inet", "what": "Adresy IP interfejsow sieciowych",   "notes": "inet = IPv4  inet6 = IPv6  lo0 = localhost (127.0.0.1)"},
            {"cmd": "curl -I URL",          "what": "Pobierz tylko naglowki HTTP",         "notes": "-I = HEAD request: sprawdz status bez pobierania body"},
            {"cmd": "netstat -nr",          "what": "Tablica routingu",                    "notes": "-n = numerycznie  -r = routing"},
            {"cmd": "host domena",          "what": "Zamien domene na IP (DNS lookup)",    "notes": "host google.com = IP Googla"},
        ],
        "boss": {
            "title": "CWICZENIE 8.1 — Diagnostyka",
            "description": "Kapłan Swiatyni uczy cie diagnostyki zanim wpusci glebiej. Sprawdz stan swojej sieci:",
            "steps": [
                {"type": "shell", "cmd": "ping -c 3 1.1.1.1",
                 "hint": "Wyslij 3 pakiety do 1.1.1.1. -c 3 = zakoncz po 3 pakietach",
                 "output": (
                     "PING 1.1.1.1 (1.1.1.1): 56 data bytes\n"
                     "64 bytes from 1.1.1.1: icmp_seq=0 ttl=58 time=8.234 ms\n"
                     "64 bytes from 1.1.1.1: icmp_seq=1 ttl=58 time=7.891 ms\n"
                     "64 bytes from 1.1.1.1: icmp_seq=2 ttl=58 time=8.156 ms\n\n"
                     "--- 1.1.1.1 ping statistics ---\n"
                     "3 packets transmitted, 3 packets received, 0.0% packet loss\n"
                     "round-trip min/avg/max/stddev = 7.891/8.094/8.234/0.143 ms"
                 )},
                {"type": "shell", "cmd": "hostname",
                 "hint": f"Sprawdz nazwe komputera — powinno byc: {HOSTNAME}",
                 "output": f"{HOSTNAME}.local"},
                {"type": "shell", "cmd": "ifconfig | grep 'inet '",
                 "hint": "'inet ' ze spacja = tylko IPv4, nie lapie inet6",
                 "output": "        inet 127.0.0.1 netmask 0xff000000\n        inet 192.168.1.42 netmask 0xffffff00 broadcast 192.168.1.255"},
            ],
        },
    },

    {
        "id": "8.2",
        "world": 8,
        "is_boss": True,
        "world_name": "Swiatynia Sieci",
        "world_flavor": (
            "curl to twoja reka siegajaca przez internet po dane bez przegladarki. "
            "SSH to szyfrowany tunel do zdalnego serwera — jakbys siedzial bezposrednio przed nim. "
            "Klucze SSH zastepuja hasla: raz wygenerowany klucz ed25519 uwierzytelnia cie na zawsze."
        ),
        "title": "curl i SSH",
        "xp": 25,
        "theory": [
            {"cmd": "curl ifconfig.me",    "what": "Pokaz swoje publiczne IP",           "notes": "Odpytuje serwis zewnetrzny ktory zwraca IP z ktorego przyszedl request"},
            {"cmd": "curl -s URL",         "what": "Pobierz dane bez paska postepu",     "notes": "-s = silent. Idealne w skryptach gdy chcesz tylko dane"},
            {"cmd": "curl -o plik URL",    "what": "Pobierz i zapisz do pliku",          "notes": "-o = output: podaj nazwe pliku. -O = uzyj nazwy z URL"},
            {"cmd": "networkQuality",      "what": "Test predkosci internetu (macOS 12+)","notes": "Wbudowane narzedzie macOS do pomiaru upload/download"},
            {"cmd": "ssh user@serwer",     "what": "Polacz sie z serwerem SSH",          "notes": "Domyslny port: 22"},
            {"cmd": "ssh -p 2222 u@s",     "what": "Polacz sie na innym porcie",         "notes": "-p = port"},
            {"cmd": "scp plik u@s:/path",  "what": "Kopiuj plik na serwer",             "notes": "scp = secure copy, ten sam protokol co SSH"},
            {"cmd": "ssh-keygen -t ed25519","what": "Generuj klucz SSH",                "notes": "ed25519 = nowoczesny algorytm. Generuje pare: klucz prywatny + .pub"},
        ],
        "boss": {
            "title": "BOSS FIGHT 8.2 — Sieciowy Mag",
            "description": (
                "Wielki Kapłan Swiatyni wymaga dowodu opanowania sieci. "
                "Odpytaj serwisy i sprawdz polaczenie. Trzy zycia:"
            ),
            "steps": [
                {"type": "info",
                 "text": (
                     "curl to terminal-przegladarka. Najwazniejsze flagi:\n"
                     "  -s  = silent (brak paska postepu)\n"
                     "  -I  = HEAD request (tylko naglowki)\n"
                     "  -o  = zapisz do pliku\n"
                     "  -L  = podazaj za przekierowaniami\n\n"
                     "curl zwraca tresc strony lub API — mozna pipe'owac do grep, jq, head."
                 )},
                {"type": "shell", "cmd": "curl -s ifconfig.me",
                 "hint": "Pokaz swoje publiczne IP — -s = silent, bez paska postepu",
                 "output": "185.123.45.67"},
                {"type": "shell", "cmd": "ping -c 4 google.com",
                 "hint": "-c 4 = wyslij tylko 4 pakiety i zakoncz automatycznie",
                 "output": (
                     "PING google.com (142.250.185.46): 56 data bytes\n"
                     "64 bytes from 142.250.185.46: icmp_seq=0 ttl=117 time=12.345 ms\n"
                     "64 bytes from 142.250.185.46: icmp_seq=1 ttl=117 time=11.987 ms\n"
                     "64 bytes from 142.250.185.46: icmp_seq=2 ttl=117 time=12.123 ms\n"
                     "64 bytes from 142.250.185.46: icmp_seq=3 ttl=117 time=11.876 ms\n\n"
                     "--- google.com ping statistics ---\n"
                     "4 packets transmitted, 4 packets received, 0.0% packet loss\n"
                     "round-trip min/avg/max/stddev = 11.876/12.083/12.345/0.176 ms"
                 )},
                {"type": "shell", "cmd": "curl -s https://api.github.com | head -5",
                 "hint": "Pobierz dane z publicznego API GitHub i pokaz tylko 5 linii",
                 "output": (
                     '{\n'
                     '  "current_user_url": "https://api.github.com/user",\n'
                     '  "authorizations_url": "https://api.github.com/authorizations",\n'
                     '  "code_search_url": "https://api.github.com/search/code?q={query}",\n'
                     '  "commit_search_url": "https://api.github.com/search/commits?q={query}",'
                 )},
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
        "world_flavor": (
            "Otchlan Gita to macierz czasu — kazda zmiana jest zapisana, "
            "kazdy commit to punkt w historii do ktorego mozna wroczyc. "
            "git init buduje te macierze od zera. Historia zaczyna sie od pierwszego commita."
        ),
        "title": "Git podstawy",
        "xp": 30,
        "theory": [
            {"cmd": "git init",           "what": "Stworz nowe repo (.git folder)",     "notes": "Tworzy ukryty folder .git z cala historia"},
            {"cmd": "git status",         "what": "Co sie zmienilo?",                   "notes": "Uzywaj czesto! Pokazuje: niesledzone pliki, zmodyfikowane, stage"},
            {"cmd": "git add plik.txt",   "what": "Dodaj plik do stage",                "notes": "Stage = obszar przygotowany do commita"},
            {"cmd": "git add .",          "what": "Dodaj WSZYSTKIE zmiany do stage",    "notes": ". = biezacy katalog i podkatalogi"},
            {"cmd": "git commit -m 'msg'","what": "Zapisz stage jako commit",           "notes": "-m = krotki opis zmian. Dobry opis: 'fix: null pointer in auth'"},
            {"cmd": "git log --oneline",  "what": "Historia commitow",                  "notes": "--oneline = 1 linia na commit. --graph = drzewo ASCII"},
            {"cmd": "git diff",           "what": "Zmiany ktore NIE sa w stage",        "notes": "--staged = zmiany ktore SA juz w stage"},
        ],
        "boss": {
            "title": "CWICZENIE 9.1 — Git Basics",
            "description": "Stroz Otchlani prowadzi cie przez pelny cykl Gita — init, add, commit:",
            "steps": [
                {"type": "shell", "cmd": f"git init {QP}",
                 "hint": "zainicjuj repo git w folderze quest-project — tworzy .git/",
                 "output": f"Initialized empty Git repository in {QP}/.git/"},
                {"type": "shell", "cmd": f"echo 'Hello Git z {HOSTNAME}' > {QP}/plik.txt",
                 "hint": "stworz plik z trescia",
                 "output": ""},
                {"type": "shell", "cmd": f"git -C {QP} status",
                 "hint": "sprawdz status — plik powinien byc jako 'untracked files'",
                 "output": (
                     "On branch master\n\nNo commits yet\n\n"
                     "Untracked files:\n"
                     "  (use \"git add <file>...\" to include in what will be committed)\n"
                     "\tplik.txt\n\n"
                     "nothing added to commit but untracked files present"
                 )},
                {"type": "shell", "cmd": f"git -C {QP} add plik.txt",
                 "hint": "dodaj plik do stage",
                 "output": ""},
                {"type": "shell", "cmd": f"git -C {QP} commit -m 'Initial commit'",
                 "hint": "zapisz commit z wiadomoscia",
                 "output": "[master (root-commit) a1b2c3d] Initial commit\n 1 file changed, 1 insertion(+)\n create mode 100644 plik.txt"},
                {"type": "shell", "cmd": f"git -C {QP} log --oneline",
                 "hint": "sprawdz historie — powinien byc jeden commit",
                 "output": "a1b2c3d (HEAD -> master) Initial commit"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj",
                 "output": ""},
            ],
        },
    },

    {
        "id": "9.2",
        "world": 9,
        "is_boss": True,
        "world_name": "Otchlan Gita",
        "world_flavor": (
            "Branch to rownolegly swiat — pracujesz na feature bez psuciai main. "
            "Gdy feature gotowy, merge laczy swiat powrotem. "
            "Konflikty to starcia miedzy wersjami — Git pyta kto ma racje."
        ),
        "title": "Branche i merge",
        "xp": 30,
        "theory": [
            {"cmd": "git branch",          "what": "Pokaz liste branchy",               "notes": "* = aktualny branch. -a = pokaz tez zdalne"},
            {"cmd": "git branch feature",  "what": "Stworz nowy branch",               "notes": "Nie przelacza sie automatycznie"},
            {"cmd": "git checkout feature","what": "Przelacz sie na branch",            "notes": "Nowoczesna alternatywa: git switch feature"},
            {"cmd": "git checkout -b feat","what": "Stworz i przelacz w jednym",       "notes": "-b = branch: skrot z dwoch komend"},
            {"cmd": "git merge feature",   "what": "Polacz branch z aktualnym",         "notes": "Bedac na main: git merge feature"},
            {"cmd": "git branch -d feat",  "what": "Usun branch",                      "notes": "-d = tylko jesli juz zmergowany  -D = na sile"},
        ],
        "boss": {
            "title": "BOSS FIGHT 9.2 — Mistrz Branchy",
            "description": (
                "Wielki Stroz Otchlani wymaga przejscia przez pelny cykl branchy. "
                "Stworz branch, commituj, zmerguj. Trzy zycia:"
            ),
            "steps": [
                {"type": "info",
                 "text": (
                     "Cykl pracy z branchami:\n"
                     "  1. Stworz repo i zrob pierwszy commit na main\n"
                     "  2. Stworz branch feature i przelacz sie na niego\n"
                     "  3. Zrob zmiany i commituj na feature\n"
                     "  4. Wroc na main i zmerguj feature\n\n"
                     "Dlaczego branche?\n"
                     "  main zawsze musi dzialac. Feature branch = eksperymentujesz\n"
                     "  bez ryzyka. Gdy gotowe — merge. Gdy nieudane — branch usuwasz."
                 )},
                {"type": "shell", "cmd": f"git init {QP}",
                 "hint": "stworz repo",
                 "output": f"Initialized empty Git repository in {QP}/.git/"},
                {"type": "shell", "cmd": f"echo 'main' > {QP}/plik.txt && git -C {QP} add . && git -C {QP} commit -m 'init'",
                 "hint": "stworz pierwszy commit na main (trzy komendy lancuchem &&)",
                 "output": "[master (root-commit) a1b2c3d] init\n 1 file changed, 1 insertion(+)\n create mode 100644 plik.txt"},
                {"type": "shell", "cmd": f"git -C {QP} checkout -b feature",
                 "hint": "-b = stworz i przelacz na nowy branch feature",
                 "output": "Switched to a new branch 'feature'"},
                {"type": "shell", "cmd": f"echo 'feature' >> {QP}/plik.txt && git -C {QP} add . && git -C {QP} commit -m 'add feature'",
                 "hint": "dodaj zmiane i commituj na feature branch",
                 "output": "[feature b2c3d4e] add feature\n 1 file changed, 1 insertion(+)"},
                {"type": "shell", "cmd": f"git -C {QP} checkout main",
                 "hint": "wroc na main",
                 "output": "Switched to branch 'main'"},
                {"type": "shell", "cmd": f"git -C {QP} merge feature",
                 "hint": "zmerguj feature do main",
                 "output": "Updating a1b2c3d..b2c3d4e\nFast-forward\n plik.txt | 1 +\n 1 file changed, 1 insertion(+)"},
                {"type": "shell", "cmd": f"git -C {QP} log --oneline --graph",
                 "hint": "--graph = drzewo branchy ASCII",
                 "output": "* b2c3d4e (HEAD -> main, feature) add feature\n* a1b2c3d init"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "posprzataj",
                 "output": ""},
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
        "world_flavor": (
            "Stanales przed Tronem. Ostatnie sekrety nie sa trudne — sa eleganckie. "
            "Brace expansion, process substitution, find -exec — narzedzia ktore skracaja 10 linii do jednej. "
            "Arcymistrz nie uderza wiecej niz trzeba."
        ),
        "title": "Zaawansowane techniki",
        "xp": 40,
        "theory": [
            {"cmd": "mkdir -p proj/{src,tests}/{v1,v2}", "what": "Brace expansion: 4 katalogi naraz",  "notes": "{a,b} = lista  {1..5} = sekwencja  Bash/zsh rozwijaja to PRZED wykonaniem"},
            {"cmd": "touch plik{1..10}.txt",             "what": "Stworz 10 plikow jednym poleceniem","notes": "{01..10} = z zerowaniem  {a..z} = alfabet"},
            {"cmd": "echo $(date +%H:%M)",               "what": "Wstaw wynik komendy",               "notes": "$() = command substitution"},
            {"cmd": "diff <(ls dir1) <(ls dir2)",        "what": "Porownaj outputy dwoch komend",     "notes": "<() = process substitution: output komendy jak plik tymczasowy"},
            {"cmd": "find . -mtime +30 -exec rm {} \\;", "what": "Znajdz i usun pliki starsze niz 30 dni", "notes": "-exec = wykonaj dla kazdego  {} = miejsce na znaleziony plik  \\; = koniec -exec"},
            {"cmd": "cmd1 & cmd2 & wait",                "what": "Uruchom rownolegle i czekaj",       "notes": "& po kazdej = uruchom w tle  wait = czekaj az wszystkie skoncza"},
            {"cmd": "awk -F: '{print $1}' /etc/passwd",  "what": "Wypisz pierwsza kolumne z : jako sep.", "notes": "-F: = separator  $1 = pierwsza kolumna  NR = numer wiersza"},
        ],
        "boss": {
            "title": "FINAL BOSS — Arcymistrz Terminala",
            "description": (
                "Sam Arcymistrz Terminala wstaje z Tronu. "
                "'Pokaz mi brace expansion i zaawansowane techniki — lub pozostan na zawsze nowicjuszem.' "
                "Trzy zycia na to ostateczne wyzwanie:"
            ),
            "steps": [
                {"type": "info",
                 "text": (
                     "Ostatni sprawdzian — brace expansion i find.\n\n"
                     "Brace expansion rozwijane PRZED wykonaniem komendy:\n"
                     "  mkdir {a,b}/{x,y}  →  mkdir a/x a/y b/x b/y\n"
                     "  touch plik{1..3}   →  touch plik1 plik2 plik3\n\n"
                     "find -exec: dla kazdego znalezionego pliku wykonaj komende\n"
                     "  find . -name '*.tmp' -exec rm {} \\;\n"
                     "  {} = miejsce dla znalezionego pliku\n"
                     "  \\; = koniec -exec (srednik musi byc poprzedzony \\ )"
                 )},
                {"type": "shell", "cmd": f"mkdir -p {HOME}/projekt/{{src,tests,docs}}/{{v1,v2}}",
                 "hint": "tworzy 6 katalogow naraz: src/v1, src/v2, tests/v1, tests/v2, docs/v1, docs/v2",
                 "output": ""},
                {"type": "shell", "cmd": f"ls -R {HOME}/projekt",
                 "hint": "sprawdz pelna strukture (-R = recursive)",
                 "output": (
                     f"{HOME}/projekt:\ndocs  src  tests\n\n"
                     f"{HOME}/projekt/docs:\nv1  v2\n\n"
                     f"{HOME}/projekt/docs/v1:\n\n"
                     f"{HOME}/projekt/docs/v2:\n\n"
                     f"{HOME}/projekt/src:\nv1  v2\n\n"
                     f"{HOME}/projekt/src/v1:\n\n"
                     f"{HOME}/projekt/src/v2:\n\n"
                     f"{HOME}/projekt/tests:\nv1  v2\n\n"
                     f"{HOME}/projekt/tests/v1:\n\n"
                     f"{HOME}/projekt/tests/v2:"
                 )},
                {"type": "shell", "cmd": f"touch {HOME}/projekt/plik{{1..5}}.txt",
                 "hint": "{{1..5}} = sekwencja: tworzy plik1.txt ... plik5.txt naraz",
                 "output": ""},
                {"type": "shell", "cmd": f"find {HOME}/projekt -name '*.txt' | wc -l",
                 "hint": "policz ile plikow .txt zostalo stworzonych — powinno byc 5",
                 "output": "       5"},
                {"type": "shell", "cmd": f"rm -r {HOME}/projekt",
                 "hint": "posprzataj — ostatni raz!",
                 "output": ""},
                {"type": "confirm",
                 "prompt": "Gratulacje Arcymistrzu! Czy ukonczyłes Terminal Quest?"},
            ],
        },
    },
]
