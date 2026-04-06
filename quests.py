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
            {"cmd": "cd katalog", "what": "Idz do katalogu (Change Directory)",             "notes": "Sciezka wzgledna: cd Documents  absolutna: cd /etc  (wzgledna = od miejsca gdzie jestem)"},
            {"cmd": "cd ..",      "what": "Cofnij sie o jeden katalog w gore",              "notes": ".. = zawsze oznacza katalog nadrzedny. ../../ = dwa poziomy wyzej"},
            {"cmd": "cd ~",       "what": f"Wroc do domu ({HOME})",                        "notes": "~ to skrot do twojego katalogu domowego, dziala wszedzie"},
            {"cmd": "cd -",       "what": "Wroc tam gdzie bylem ostatnio",                 "notes": "Shell pamięta poprzednie miejsce — - to jak przycisk Wstecz w przegladarce"},
            {"cmd": "clear",      "what": "Wyczysc ekran",                                 "notes": "Ctrl+L dziala tak samo — ale historia nie znika, tylko przesuwa ekran"},
        ],
        "boss": {
            "title": "CWICZENIE 1.1 — Nawigator",
            "description": "Przewodnik po Wiosce daje ci probe — przejdz przez 5 znanych adresow i wroc do domu:",
            "steps": [
                {"type": "shell", "cmd": "cd /tmp",
                 "hint": "/tmp = pliki tymczasowe, czyszczone po restarcie"},
                {"type": "shell", "cmd": "cd /var/log",
                 "hint": "/var/log = logi systemowe — tu system zapisuje co sie dzieje"},
                {"type": "shell", "cmd": "cd /usr/local",
                 "hint": "/usr/local = tu Homebrew instaluje programy"},
                {"type": "shell", "cmd": "cd /etc",
                 "hint": "/etc = konfiguracja systemu — pliki tekstowe z ustawieniami"},
                {"type": "shell", "cmd": "cd ~/Documents",
                 "hint": "~/Documents = twoj folder Dokumenty  ~ = skrot do home"},
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
        "world_flavor": (
            "Szpieg zawsze najpierw zbiera informacje o terenie przed akcja. "
            "Zanim zaatakujesz problem, sprawdz kto jestes, gdzie jestes i co cie otacza. "
            "whoami, date, uname — twoje narzedzia rozpoznawcze."
        ),
        "title": "Rozpoznanie terenu",
        "xp": 15,
        "theory": [
            {"cmd": "whoami",       "what": "Kim jestem? Wypisuje nazwe uzytkownika",      "notes": f"Twoj: {USERNAME}  Wazne gdy uzywasz sudo lub ssh na inny serwer"},
            {"cmd": "date",         "what": "Aktualna data i czas",                        "notes": "date '+%Y-%m-%d' = tylko data  date '+%H:%M' = tylko godzina  Zmien format dowolnie"},
            {"cmd": "cal",          "what": "Kalendarz miesiezny",                         "notes": "cal 2026 = caly rok  cal 3 2026 = marzec 2026"},
            {"cmd": "uname -a",     "what": "Info o systemie (OS, kernel, architektura)",  "notes": "-a = all. Szukaj 'arm64' = Apple Silicon, 'x86_64' = Intel"},
            {"cmd": "echo 'tekst'", "what": "Wypisz tekst na ekran",                       "notes": "echo $HOME = wartosc zmiennej srodowiskowej. $ZMIENNA = odczyt wartosci"},
            {"cmd": "history",      "what": "Historia ostatnich komend",                   "notes": "history | grep git = tylko komendy zawierajace 'git'. Przydatne gdy nie pamietasz skladni"},
            {"cmd": "man ls",       "what": "Manual (dokumentacja) komendy",               "notes": "/ = szukaj frazy  n = nastepny wynik  q = wyjscie. To pelna dokumentacja, nie help"},
        ],
        "boss": {
            "title": "CWICZENIE 1.2 — Wywiad",
            "description": "Stary szpieg w tawernie daje ci liste pytan wywiadowczych — odpowiedz uzywajac komend terminala:",
            "steps": [
                {"type": "shell", "cmd": "whoami",
                 "hint": f"Wypisuje nazwe uzytkownika — powinno byc: {USERNAME}"},
                {"type": "shell", "cmd": "date",
                 "hint": "Pokazuje dzisiejszy dzien tygodnia i godzine"},
                {"type": "shell", "cmd": "uname -a",
                 "hint": "Pokazuje system i architekture (arm64 = Apple Silicon)"},
                {"type": "shell", "cmd": "history",
                 "hint": "Lista ostatnich komend — historia twoich dzialan"},
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
            {"cmd": "Tab",         "what": "AUTOUZUPELNIANIE — najwazniejszy skrot",  "notes": "Dwa razy Tab = pokaz wszystkie mozliwosci. Uzywaj przy kazdej sciezce i nazwie komendy"},
            {"cmd": "Ctrl+C",      "what": "Przerwij biezaca komende",                "notes": "Wysyla sygnal SIGINT do procesu. Ratuje gdy komenda sie zawieszla"},
            {"cmd": "Ctrl+R",      "what": "Szukaj wstecz w historii komend",         "notes": "Wpisz fragment, ENTER = wykonaj, Ctrl+R znowu = nastepny wynik, Esc = anuluj"},
            {"cmd": "Ctrl+L",      "what": "Wyczysc ekran",                           "notes": "To samo co clear — ale nie kasuje historii, tylko przewija"},
            {"cmd": "Ctrl+A",      "what": "Skocz na poczatek linii",                 "notes": "A jak poczAtek. Pomocne gdy napisales dlugie polecenie i chcesz dodac np. sudo na poczatku"},
            {"cmd": "Ctrl+E",      "what": "Skocz na koniec linii",                   "notes": "E jak End. Tandem z Ctrl+A — skakaj miedzy koncem a poczatkiem"},
            {"cmd": "Ctrl+W",      "what": "Usun slowo w lewo",                       "notes": "Szybsze niz trzymanie Backspace. Usuwa od kursora do poprzedniej spacji"},
            {"cmd": "Ctrl+U",      "what": "Usun cala linie od kursora w lewo",       "notes": "Ctrl+K usuwa od kursora w prawo. Razem = czysta linia"},
            {"cmd": "!!",          "what": "Powtorz ostatnia komende",                "notes": "Najczesciej: sudo !! gdy ostatnia komenda odrzucona przez brak uprawnien"},
            {"cmd": "strzalka UP", "what": "Poprzednia komenda w historii",           "notes": "DOWN = nastepna. Trzymaj UP zeby przegladac historieFaster niz Ctrl+R dla niedawnych komend"},
        ],
        "boss": {
            "title": "BOSS FIGHT 1.3 — Mistrz Skrotow",
            "description": (
                "Straznik Wioski blokuje brame. Wymaga dowodu ze opanowales skroty i nawigacje. "
                "Trzy zycia — mysl zanim nacisniesz Enter:"
            ),
            "steps": [
                {"type": "info",
                 "text": (
                     "Przed walka — przypomnij sobie skroty:\n"
                     "  Ctrl+A / Ctrl+E  — poczatek / koniec linii\n"
                     "  Ctrl+R           — szukaj w historii\n"
                     "  Ctrl+C           — przerwij biezacy proces\n"
                     "  Tab              — autouzupelnianie\n"
                     "  !!               — powtorz ostatnia komende\n\n"
                     "Pamietaj: w boss fight masz 3 zycia wspolne dla wszystkich krokow."
                 )},
                {"type": "shell", "cmd": "echo 'test Ctrl+A i Ctrl+E'",
                 "hint": "Wpisz komende, uzyj Ctrl+A zeby skoczyc na poczatek, Ctrl+E na koniec"},
                {"type": "shell", "cmd": "history | tail -5",
                 "hint": "Pokaz ostatnie 5 komend z historii — | przekazuje output do nastepnej komendy"},
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
            {"cmd": "mkdir -p a/b/c",     "what": "Stworz zagniezdzone katalogi",          "notes": "-p = parents: tworzy wszystkie brakujace katalogi po drodze. Bez -p blad gdy a/ nie istnieje"},
            {"cmd": "cp zrodlo cel",      "what": "Kopiuj plik",                           "notes": "Jesli cel istnieje — nadpisuje BEZ pytania! cp -i = pytaj przed nadpisaniem"},
            {"cmd": "cp -r folder kopia", "what": "Kopiuj caly katalog",                   "notes": "-r = recursive: wchodzi w podkatalogi i kopiuje wszystko. Bez -r blad na katalogach"},
            {"cmd": "mv stary nowy",      "what": "Przenies lub zmien nazwe",              "notes": "Ta sama komenda robi obie rzeczy. Jesli cel jest w innym katalogu = przeniesienie"},
            {"cmd": "rm plik",            "what": "USUN plik (NIEODWRACALNE!)",            "notes": "Brak Kosza — rm usuwa na zawsze. Ctrl+Z nie pomoze. Uzyj -i zeby pytalo przed usunieciem"},
            {"cmd": "rm -r folder",       "what": "USUN katalog z zawartoscia",            "notes": "-r = recursive: wchodzi i usuwa wszystko. -rf = bez pytan. rm -rf / to koniec systemu!"},
            {"cmd": "rmdir folder",       "what": "Usun PUSTY katalog",                    "notes": "Odmowi jesli nie pusty — bezpieczniejsza alternatywa dla rm -r"},
        ],
        "boss": {
            "title": "CWICZENIE 2.1 — Budowniczy i Niszczyciel",
            "description": "Duch Lasu daje ci zadanie: zbuduj strukture projektu, sprawdz ja i posprzataj po sobie:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}/{{src/utils,docs,tests}}",
                 "hint": "-p = parents  {{a,b}} = brace expansion: tworzy kilka katalogow naraz"},
                {"type": "shell", "cmd": f"touch {QP}/src/main.sh",
                 "hint": "touch = stworz pusty plik  .sh = rozszerzenie skryptu bash"},
                {"type": "shell", "cmd": f"touch {QP}/src/utils/helpers.sh",
                 "hint": "plik funkcji pomocniczych w podkatalogu"},
                {"type": "shell", "cmd": f"touch {QP}/docs/README.md",
                 "hint": "dokumentacja  .md = markdown (jezyk formatowania tekstu)"},
                {"type": "shell", "cmd": f"touch {QP}/tests/test_main.sh",
                 "hint": "plik testow"},
                {"type": "shell", "cmd": f"ls -R {QP}",
                 "hint": "-R = recursive: pokazuje zawartosc wszystkich podkatalogow"},
                {"type": "shell", "cmd": f"rm -r {QP}",
                 "hint": "-r = recursive: usuwa katalog razem z cala zawartoscia NIEODWRACALNIE"},
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
        "world_flavor": (
            "Las skrywa wiele tajemnic zapisanych w plikach. "
            "Nie musisz czytac wszystkiego — wystarczy zajrzec na poczatek lub koniec, policzyc linie. "
            "cat nie jest odpowiedzia na wszystko: duzy plik zaflooduje terminal — uzyj less."
        ),
        "title": "Czytanie plikow",
        "xp": 20,
        "theory": [
            {"cmd": "cat plik",        "what": "Pokaz cala zawartosc pliku",           "notes": "Uzyj tylko dla malych plikow (do ~50 linii). Na duzych — less"},
            {"cmd": "less plik",       "what": "Przegladarka plikow",                  "notes": "Strzalki / PageUp/Down — przewijanie  /szukaj — szukaj  n/N — nastepny/poprzedni  q — wyjscie"},
            {"cmd": "head -n 10 plik", "what": "Pierwsze 10 linii",                   "notes": "-n = ile linii. Domyslnie 10. head -1 plik = tylko pierwsza linia (np. naglowek CSV)"},
            {"cmd": "tail -n 10 plik", "what": "Ostatnie 10 linii",                   "notes": "-n = ile linii. tail -1 = ostatnia linia. Bez -n = ostatnie 10"},
            {"cmd": "tail -f plik",    "what": "Sledz plik na zywo",                  "notes": "-f = follow. Nowe linie pojawiaja sie automatycznie. Ctrl+C zeby zatrzymac"},
            {"cmd": "wc -l plik",      "what": "Policz linie",                        "notes": "wc bez flag = linie slowa bajty naraz. -l = lines  -w = words  -c = chars/bytes"},
            {"cmd": "wc -w plik",      "what": "Policz slowa",                        "notes": "Slowo = ciag znakow oddzielony spacjami. -c = bajty (uwaga: UTF-8 znak != bajt)"},
            {"cmd": "diff plik1 plik2","what": "Porownaj dwa pliki",                  "notes": "< = linia tylko w pierwszym pliku  > = tylko w drugim  Linie te same = brak wyniku"},
        ],
        "boss": {
            "title": "CWICZENIE 2.2 — Czytacz",
            "description": "Bibliotekarz Lasu daje ci zwoj z 100 liniami — przeanalizuj go bez otwierania edytora:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "stworz folder na pliki"},
                {"type": "shell", "cmd": f"seq 1 100 > {QP}/numbers.txt",
                 "hint": "seq 1 100 = generuj liczby od 1 do 100  > = zapisz do pliku (nadpisuje jesli istnieje)"},
                {"type": "shell", "cmd": f"wc -l {QP}/numbers.txt",
                 "hint": "Policz ile linii ma plik — powinno byc 100"},
                {"type": "shell", "cmd": f"head -n 5 {QP}/numbers.txt",
                 "hint": "Pierwsze 5 linii — sprawdz ze plik zaczyna sie od 1"},
                {"type": "shell", "cmd": f"tail -n 3 {QP}/numbers.txt",
                 "hint": "Ostatnie 3 linie — sprawdz ze plik konczy sie na 100"},
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
        "world_flavor": (
            "Tropiciel wie, ze nie wystarczy chodzic po lesie — trzeba umiec w nim szukac. "
            "find szuka plikow po nazwie, rozmiarze, dacie modyfikacji. "
            "grep szuka tekstu wewnatrz plikow. To dwa rozne narzedzia — oba bezcenne."
        ),
        "title": "Wyszukiwanie",
        "xp": 25,
        "theory": [
            {"cmd": "find . -name '*.txt'",  "what": "Znajdz pliki po nazwie",            "notes": ". = szukaj tutaj i w podkatalogach  * = dowolny ciag znakow  Cudzyslowy chronia * przed shellem"},
            {"cmd": "find . -type d",        "what": "Znajdz tylko katalogi",             "notes": "-type f = pliki  -type l = linki symboliczne  -type d = katalogi"},
            {"cmd": "find . -size +1M",      "what": "Znajdz pliki wieksze niz 1MB",      "notes": "+1M = wieksze  -1M = mniejsze  Jednostki: k (KB), M (MB), G (GB)"},
            {"cmd": "grep 'tekst' plik",     "what": "Szukaj tekstu w pliku",             "notes": "Wypisuje CALE linie zawierajace wzorzec. Szybsze niz less + /szukaj"},
            {"cmd": "grep -r 'tekst' .",     "what": "Szukaj rekurencyjnie w katalogu",   "notes": "-r = recursive: przeszukuj wszystkie podkatalogi. Wynik: sciezka:nr_linii:tresc"},
            {"cmd": "grep -i 'tekst' plik",  "what": "Szukaj (ignoruj wielkosc liter)",   "notes": "-i = ignore case: 'Error' znajdzie ERROR, error, Error. Czesto -ri laczymy"},
            {"cmd": "grep -n 'tekst' plik",  "what": "Szukaj z numerami linii",           "notes": "-n = numery linii przy wynikach. Przydatne do otwarcia edytora na konkretnej linii"},
            {"cmd": "which python3",         "what": "Gdzie jest zainstalowany program?", "notes": "Pokazuje pelna sciezke: /usr/bin/python3. Gdy masz kilka wersji — sprawdz ktora jest aktywna"},
        ],
        "boss": {
            "title": "BOSS FIGHT 2.3 — Tropiciel",
            "description": (
                "Straznik Lasu, stary tropiciel, wystawia cie na probe. "
                "Stworz projekt z trescia, znajdz pliki i przeszukaj je. "
                "Trzy zycia — uwazaj na skladnie:"
            ),
            "steps": [
                {"type": "info",
                 "text": (
                     "Tropiciel mowi: 'Roznica miedzy find a grep:\n"
                     "  find  — szuka PLIKOW po nazwie, rozmiarze, dacie\n"
                     "  grep  — szuka TEKSTU wewnatrz plikow\n\n"
                     "Wildcards w find owijaj w cudzyslowy: find . -name '*.sh'\n"
                     "Bo bez cudzysolow shell sam rozwinylby *.sh zanim find to zobaczy."
                 )},
                {"type": "shell", "cmd": f"mkdir -p {QP}/{{src/utils,docs,tests}}",
                 "hint": "stworz strukture katalogow"},
                {"type": "shell",
                 "cmd": f"echo $'TODO: fix bug\\nDONE: add feature\\nTODO: write tests' > {QP}/src/main.sh",
                 "hint": "$'...' = skladnia zsh dla \\n (nowa linia wewnatrz stringa)"},
                {"type": "shell",
                 "cmd": f"echo $'# Helper functions\\nTODO: implement helpers' > {QP}/src/utils/helpers.sh",
                 "hint": "drugi plik z trescia"},
                {"type": "shell", "cmd": f"find {QP} -name '*.sh'",
                 "hint": "Znajdz wszystkie pliki .sh w projekcie — cudzyslow wokol '*.sh' jest wazny"},
                {"type": "shell", "cmd": f"grep -r 'TODO' {QP}",
                 "hint": "-r = przeszukaj wszystkie podkatalogi rekurencyjnie"},
                {"type": "shell", "cmd": f"grep -r 'TODO' {QP} | wc -l",
                 "hint": "| wc -l = policz ile linii wynikow zwrocil grep — ile TODO pozostalo"},
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
        "world_flavor": (
            "Kopalnia ukrywa skarby gleboko — trzeba laczyc narzedzia jak wagoniki, "
            "kazdy przenoszacy output poprzedniego do wejscia nastepnego. "
            "Pipe | to filozofia Unixa: kazdy program robi JEDNA rzecz dobrze, ty je laczysz."
        ),
        "title": "Pipe — laczenie komend",
        "xp": 25,
        "theory": [
            {"cmd": "ls -la | less",                 "what": "Ogromna lista → przewijalna",        "notes": "| = przekaz stdout lewej komendy jako stdin prawej. Nie tworzy pliku posredniego"},
            {"cmd": "ls -la | wc -l",                "what": "Ile plikow jest w katalogu?",        "notes": "wc -l liczy linie outputu ls. Minus 1 (naglowek 'total') = liczba plikow"},
            {"cmd": "ls -la | grep '.txt'",          "what": "Tylko pliki .txt z listy",           "notes": "grep filtruje linie — wypisuje tylko te zawierajace wzorzec"},
            {"cmd": "ls -la | sort -k5 -n",          "what": "Posortuj po rozmiarze",              "notes": "-k5 = sortuj po 5. kolumnie (rozmiar w ls -la)  -n = numerycznie (nie alfabetycznie)"},
            {"cmd": "history | grep 'cd' | tail -5", "what": "Ostatnie 5 komend z cd",            "notes": "Lancuch 3 komend! history → filtruj grep → ostatnie 5 tail"},
            {"cmd": "ps aux | grep chrome | wc -l",  "what": "Ile procesow chrome dziala?",       "notes": "Wynik zawiera tez sam grep — odejmij 1 od wyniku"},
        ],
        "boss": {
            "title": "CWICZENIE 3.1 — Lacznik",
            "description": "Gornik Potokow uczy cie laczyc komendy. Polacz je pipe'em:",
            "steps": [
                {"type": "shell", "cmd": "ls -la ~ | wc -l",
                 "hint": "Ile plikow/katalogow jest w twoim home? ls -la wypisuje kazdy w linii, wc -l liczy"},
                {"type": "shell", "cmd": "ls -la ~ | sort -k5 -rn | head -5",
                 "hint": "5 najwiekszych elementow w home: -r = odwrotnie  -n = numerycznie  head -5 = pierwsze 5"},
                {"type": "shell", "cmd": "history | grep 'cd' | wc -l",
                 "hint": "Ile razy uzywales komendy cd? Trzy komendy w lancuchu"},
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
            {"cmd": ">",   "what": "Zapisz stdout do pliku (NADPISUJE!)",  "notes": "Tworzy plik jesli nie istnieje. Jesli istnieje — niszczy zawartosc bez pytania. >> = bezpieczniejszy"},
            {"cmd": ">>",  "what": "Dopisz do pliku",                      "notes": "Nie niszczy istniejacych danych — dolicza na koniec. Tworzy plik jesli nie istnieje"},
            {"cmd": "<",   "what": "Wczytaj z pliku jako stdin",           "notes": "sort < lista.txt to samo co sort lista.txt — ale < dziala na kazda komende ktora czyta stdin"},
            {"cmd": "2>",  "what": "Przekieruj stderr (bledy)",            "notes": "2>/dev/null = ignoruj bledy (np. 'Permission denied' przy find). /dev/null = wirtualny kosz"},
            {"cmd": "&>",  "what": "Przekieruj stdout I stderr razem",     "notes": "Skrot dla > plik 2>&1. Wszystko (normalne + bledy) trafia do jednego pliku"},
            {"cmd": "tee", "what": "Wyswietl I zapisz jednoczesnie",       "notes": "Jak rozgaleznik Y — dane ida i na ekran i do pliku. Np. komenda | tee log.txt | grep Error"},
        ],
        "boss": {
            "title": "CWICZENIE 3.2 — Przekierowania",
            "description": "Mistrz Przekierowan probuje twoja wiedze o strumieniach danych:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "stworz folder"},
                {"type": "shell", "cmd": f"ls -la ~ > {QP}/listing.txt",
                 "hint": "> = zapisz stdout do pliku (nadpisuje jesli istnieje)"},
                {"type": "shell", "cmd": f"echo '# Moja lista' >> {QP}/listing.txt",
                 "hint": ">> = dopisz na koniec (nie nadpisuje istniejacych danych)"},
                {"type": "shell", "cmd": f"wc -l < {QP}/listing.txt",
                 "hint": "< = uzyj pliku jako stdin komendy — wc dostaje zawartosc pliku"},
                {"type": "shell", "cmd": "find / -name '*.conf' 2>/dev/null | head -5",
                 "hint": "2>/dev/null = ignoruj bledy braku dostepu do katalogow systemowych"},
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
        "world_flavor": (
            "Na dnie kopalni kryja sie najpotezniejsze narzedzia. "
            "sort, uniq, cut, sed, awk — w reku mistrza tworza jednolinijkowe programy "
            "zdolne przeanalizowac gigabajtowe logi w sekunde."
        ),
        "title": "Potezne narzedzia tekstowe",
        "xp": 30,
        "theory": [
            {"cmd": "sort",              "what": "Sortuj alfabetycznie",                  "notes": "-n = numerycznie (10 > 9, nie jak tekst: '9' > '10')  -r = odwrotnie  -rn = od najwiekszego"},
            {"cmd": "uniq",              "what": "Usun sasiadujace duplikaty",             "notes": "ZAWSZE poprzedz sort! uniq nie widzi duplikatow ktore nie sasiaduja ze soba"},
            {"cmd": "uniq -c",           "what": "Policz wystapienia",                    "notes": "-c = count: dodaje licznik przed kazdym wierszem. Razem: sort | uniq -c | sort -rn"},
            {"cmd": "cut -d: -f1",       "what": "Wytnij kolumne",                        "notes": "-d = delimiter (separator pola)  -f1 = pierwsza kolumna. cut -d: -f1 /etc/passwd = nazwy uzytkownikow"},
            {"cmd": "tr 'a-z' 'A-Z'",   "what": "Zamien znaki (male na duze)",           "notes": "Tylko z pipe — nie przyjmuje pliku bezposrednio. tr -d '\\n' usuwa znaki nowej linii"},
            {"cmd": "sed 's/old/new/g'", "what": "Znajdz i zamien tekst",                 "notes": "s = substitute  g = global (wszystkie w linii)  Bez g = tylko pierwsze w kazdej linii"},
            {"cmd": "awk '{print $1}'",  "what": "Wypisz pierwsza kolumne",               "notes": "$1 = pierwsza kolumna  $NF = ostatnia  $0 = cala linia  -F: = separator :  Potezniejsze niz cut"},
            {"cmd": "xargs",             "what": "Zamien stdin na argumenty",             "notes": "find . -name '*.tmp' | xargs rm = usuwa znalezione pliki. Bez xargs rm chcialby opcje, nie argumenty"},
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
                 "hint": "przygotuj folder"},
                {"type": "shell",
                 "cmd": f"printf '192.168.1.1 GET /index.html 200\\n10.0.0.5 GET /about.html 200\\n192.168.1.1 POST /login 401\\n10.0.0.5 GET /dashboard 200\\n172.16.0.1 GET /index.html 404\\n10.0.0.5 GET /api/data 500\\n' > {QP}/access.log",
                 "hint": "printf tworzy plik logu z 6 wpisami — format: IP METODA SCIEZKA KOD"},
                {"type": "shell", "cmd": f"cut -d' ' -f1 {QP}/access.log | sort | uniq -c | sort -rn",
                 "hint": "Ktore IP ma najwiecej requestow? cut bierze 1. pole, sort sortuje, uniq -c liczy, sort -rn = od najwiekszego"},
                {"type": "shell", "cmd": f"grep -E ' [45][0-9]{{2}}$' {QP}/access.log",
                 "hint": "Bledy 4xx i 5xx: -E = extended regex  [45] = 4 lub 5  [0-9]{{2}} = dwie cyfry  $ = koniec linii"},
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
        "world_flavor": (
            "Na dnie Wiezy Edytora nauczysz sie ze nie zawsze trzeba wchodzic do srodka. "
            "Czesto mozna zmodyfikowac plik z zewnatrz jednym poleceniem. "
            "echo, sed, printf — szybsze niz otwieranie edytora gdy zmiana jest mala."
        ),
        "title": "Edycja bez edytora",
        "xp": 15,
        "theory": [
            {"cmd": "echo 'tekst' > plik.txt",       "what": "Stworz plik z trescia (nadpisuje)",  "notes": "> nadpisuje — jesli plik istnieje, poprzednia zawartosc znika. >> dopisuje na koniec"},
            {"cmd": "echo 'wiecej' >> plik.txt",      "what": "Dopisz na koniec pliku",             "notes": "Bezpieczne — nie niszczy istniejacych danych. Tworzy plik jesli nie istnieje"},
            {"cmd": "cat > plik.txt",                 "what": "Wpisuj z klawiatury do pliku",       "notes": "Wpisz tekst, kazda linia Enter. Ctrl+D = koniec (EOF = End Of File) — zapisuje"},
            {"cmd": "sed -i 's/stare/nowe/g' plik",  "what": "Zamien tekst w pliku (in-place)",    "notes": "-i = in-place: modyfikuje sam plik (nie stdout). Na macOS wymagane: sed -i '' 's/...' plik"},
            {"cmd": "sed -n '5,10p' plik",            "what": "Wypisz linie 5-10",                  "notes": "-n = nie wypisuj domyslnie  p = print dla zakresu  Alternatywa: head -10 | tail -6"},
            {"cmd": "printf 'linia1\\nlinia2\\n'",    "what": "Wypisz tekst z interpretacja \\n",  "notes": "printf rozumie \\n jako nowa linia. echo bez -e nie interpretuje \\n w wielu shellach"},
        ],
        "boss": {
            "title": "CWICZENIE 4.1 — Edycja bez edytora",
            "description": "Czlowiek bez edytora na dolnym poziomie Wiezy — manipuluj plikami bez otwierania czegolwiek:",
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "stworz folder"},
                {"type": "shell", "cmd": f"printf 'imie: {USERNAME}\\nhost: {HOSTNAME}\\ndata: 2026\\n' > {QP}/info.txt",
                 "hint": "printf z \\n tworzy wieloliniowy plik od razu"},
                {"type": "shell", "cmd": f"cat {QP}/info.txt",
                 "hint": "sprawdz zawartosc pliku — powinny byc 3 linie"},
                {"type": "shell", "cmd": f"echo 'system: macOS' >> {QP}/info.txt",
                 "hint": ">> = dopisz na koniec bez nadpisywania"},
                {"type": "shell", "cmd": f"sed -i '' 's/2026/$(date +%Y)/g' {QP}/info.txt",
                 "hint": "sed -i '' na macOS (pusty string po -i = brak backupu)  s/stare/nowe/g = zamien"},
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
        "world_flavor": (
            "Pierwsze pietro Wiezy: nano. Prosty, przyjazny, ze skrotami widocznymi na dole. "
            "^ oznacza Ctrl. Idealne dla poczatkujacych i szybkich poprawek. "
            "Nie musisz go kochac — wystarczy ze umiesz wyjsc i zapisac."
        ),
        "title": "Nano — latwiejszy start",
        "xp": 15,
        "theory": [
            {"cmd": "nano plik.txt", "what": "Otworz plik (stworzy jesli nie istnieje)", "notes": "Skroty widoczne na dole ekranu. ^ = Ctrl, M- = Alt"},
            {"cmd": "Ctrl+O",        "what": "Zapisz (O jak Output/Write Out)",          "notes": "Enter potwierdza nazwe pliku. Mozna zmienic nazwe przy zapisie"},
            {"cmd": "Ctrl+X",        "what": "Wyjdz",                                   "notes": "Jesli sa niezapisane zmiany — zapyta: Y = tak, N = nie, Ctrl+C = anuluj"},
            {"cmd": "Ctrl+W",        "what": "Szukaj tekstu (W jak Where Is)",          "notes": "Enter = nastepny wynik. Ctrl+W znowu = szukaj dalej"},
            {"cmd": "Ctrl+K",        "what": "Wytnij cala linie",                       "notes": "Zaznacz kilka linii Ctrl+K kilka razy — trafias do bufora"},
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
        "world_flavor": (
            "Na szczycie Wiezy mieszka Vim — legendarny edytor z 1976 roku, uzywany przez miliony do dzis. "
            "Trudny na poczatku, ale po opanowaniu szybszy od kazdego innego. "
            "Jego sekret: tryby. Normal to podstawa, Insert to pisanie, :komenda to akcje."
        ),
        "title": "Vim — bron legendarna",
        "xp": 40,
        "theory": [
            {"cmd": "i",       "what": "Wejdz w INSERT mode — tu mozesz pisac",        "notes": "Po otwarciu Vima JESTES w NORMAL mode i NIE mozesz pisac! i = insert przed kursorem, a = za"},
            {"cmd": "ESC",     "what": "Wroc do NORMAL mode — zawsze bezpieczny",      "notes": "Nie wiesz w jakim trybie jestes? Nacisnij ESC kilka razy — zawsze wraca do NORMAL"},
            {"cmd": ":w",      "what": "Zapisz plik",                                  "notes": "w = write. Musi byc w NORMAL mode, nie INSERT. Jesli plik nie ma nazwy: :w nazwa.txt"},
            {"cmd": ":q",      "what": "Wyjdz",                                        "notes": "Blad jesli sa niezapisane zmiany. :wq = zapisz i wyjdz  :q! = wyjdz bez zapisu (na sile)"},
            {"cmd": ":wq",     "what": "Zapisz i wyjdz",                               "notes": "Najczesciej uzywane. Alternatywa: ZZ w NORMAL mode (szybciej)"},
            {"cmd": ":q!",     "what": "Wyjdz BEZ zapisu",                             "notes": "! = na sile, ignoruj niezapisane zmiany. Awaryjna ucieczka gdy cos sie posypalo"},
            {"cmd": "h j k l", "what": "Nawigacja: lewo dol gora prawo",               "notes": "Jak strzalki ale rece nie opuszczaja home row. j = dol (ksztalt litery), k = gora"},
            {"cmd": "gg / G",  "what": "Poczatek / koniec pliku",                      "notes": "gg = goto first line  G = goto last line  5G = skocz do linii 5"},
            {"cmd": "/tekst",  "what": "Szukaj w dol",                                 "notes": "n = nastepny wynik  N = poprzedni  ? = szukaj w gore. Szukanie zawija sie przez plik"},
            {"cmd": "dd",      "what": "Usun (wytnij) cala linie",                     "notes": "3dd = usun 3 linie. d = delete, zawsze cofa do bufora (mozna wklejac przez p)"},
            {"cmd": "yy / p",  "what": "Kopiuj linie / wklej ponizej",                 "notes": "y = yank (kopiuj do bufora)  p = paste ponizej kursora  P = powyzej"},
            {"cmd": "u",       "what": "Cofnij (undo)",                                "notes": "Ctrl+R = ponow (redo). Vim ma nielimitowane undo w tej samej sesji"},
        ],
        "boss": {
            "title": "BOSS FIGHT 4.3 — Wiezmistrz Edytora",
            "description": (
                "Wiezmistrz siedzi w gabinecie na szczycie i wskazuje na terminal: "
                "'Nie ma skrotow do nauki Vima. Jest tylko vimtutor.' "
                "Trzy zycia — ale tutaj liczysz sie tylko ty i samouczek:"
            ),
            "steps": [
                {"type": "info",
                 "text": (
                     "Uruchom: vimtutor\n\n"
                     "vimtutor to interaktywny samouczek wbudowany w Vima.\n"
                     "Tworzy tymczasowy plik — nie musisz nic czyscic po zakonczeniu.\n"
                     "Czas: ok. 30 minut.\n\n"
                     "Najwazniejsze zyciowe lekcje z vimtutor:\n"
                     "  :q!  — wyjdz bez zapisu (uciekasz od Vima)\n"
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
            {"cmd": "whoami",         "what": "Aktualna nazwa uzytkownika",            "notes": f"Twoj: {USERNAME}  Wazne przy SSH na serwery — sprawdz czy jestes tym uzytkownikiem co chcesz"},
            {"cmd": "id",             "what": "UID, GID i grupy uzytkownika",          "notes": "UID=0 to root (administrator). GID = group ID. Grupy decyduja o dostepie do zasob"},
            {"cmd": "groups",         "what": "Do jakich grup naleze?",               "notes": "Czlonek grupy 'admin' = mozesz uzywac sudo. 'wheel' = to samo na niektorych systemach"},
            {"cmd": "sudo komenda",   "what": "Uruchom komende jako root",            "notes": "Superuser Do. Pyta o twoje haslo (nie roota). Pamietac przez 5 minut — nie wpisuj hasla za kazdym razem"},
            {"cmd": "sudo -l",        "what": "Jakie komendy moge uruchamiac sudo?",  "notes": "-l = list. Pokazuje co mozesz robic bez ograniczen lub z haslem"},
            {"cmd": "su - uzytkownik","what": "Przelacz sie na innego uzytkownika",   "notes": "su = switch user. - = zaladuj jego profil shellowy (.zshrc etc). Bez - = tylko zmiana uzytkownika"},
            {"cmd": "last",           "what": "Historia logowan do systemu",          "notes": "Kiedy i skad sie logowali uzytkownicy. Przydatne przy audycie bezpieczenstwa"},
        ],
        "boss": {
            "title": "CWICZENIE 5.1 — Wywiad o uzytkownikach",
            "description": "Kapitan Twierdzy sprawdza czy znasz system uprawnien — odpowiedz na pytania wywiadowcze:",
            "steps": [
                {"type": "shell", "cmd": "id",
                 "hint": f"Wypisuje UID uzytkownika {USERNAME}, GID i wszystkie grupy do ktorych nalezysz"},
                {"type": "shell", "cmd": "groups",
                 "hint": "Pokaz do jakich grup nalezysz — szukaj 'admin' lub 'wheel'"},
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
        "world_flavor": (
            "Dziewiec liter ktore decyduja o wszystkim: rwxrwxrwx. "
            "r = czytaj, w = pisz, x = wykonuj. Trzy grupy: wlasciciel, jego grupa, wszyscy inni. "
            "chmod zmienia te prawa — chmod 755 to klasyczne uprawnienia dla programow."
        ),
        "title": "Uprawnienia plikow",
        "xp": 25,
        "theory": [
            {"cmd": "ls -la",           "what": "Pokaz uprawnienia plikow",             "notes": "Format: -rwxr-xr-- = typ|wlasciciel|grupa|inni. Typ: - plik, d katalog, l link"},
            {"cmd": "chmod 755 plik",   "what": "Ustaw uprawnienia liczbowo",            "notes": "r=4 w=2 x=1. 7=rwx 5=r-x 4=r--. 755 = wlasciciel wszystko, reszta czyta i wykonuje"},
            {"cmd": "chmod 644 plik",   "what": "Typowe uprawnienia dla plikow",        "notes": "644 = rw-r--r-- : wlasciciel czyta+pisze, reszta tylko czyta. Standard dla plikow konfiguracji"},
            {"cmd": "chmod +x plik",    "what": "Dodaj prawo wykonywania",              "notes": "+x = dla wszystkich  u+x = tylko wlasciciel  g+x = tylko grupa  o-x = odbierz innym"},
            {"cmd": "chmod u+w plik",   "what": "Dodaj pisanie dla wlasciciela",        "notes": "u = user (wlasciciel)  g = group  o = others  a = all. Symbolicznie jest czytelniejsze niz liczby"},
            {"cmd": "sudo chown u:g p", "what": "Zmien wlasciciela i grupe",            "notes": "Wymaga sudo. chown user:group plik. Bez :group = zmien tylko wlasciciela"},
        ],
        "boss": {
            "title": "CWICZENIE 5.2 — Straznik Uprawnien",
            "description": "Straznik Twierdzy pokazuje ci plik i kaduze sprawdzic i zmienic jego uprawnienia:",
            "steps": [
                {"type": "shell", "cmd": f"touch {HOME}/quest-perm.sh",
                 "hint": "stworz plik testowy"},
                {"type": "shell", "cmd": f"ls -la {HOME}/quest-perm.sh",
                 "hint": "sprawdz uprawnienia — domyslnie rw-r--r-- (644) — wlasciciel czyta+pisze, reszta czyta"},
                {"type": "shell", "cmd": f"chmod +x {HOME}/quest-perm.sh",
                 "hint": "+x = dodaj prawo wykonywania dla wszystkich — plik staje sie programem"},
                {"type": "shell", "cmd": f"chmod 600 {HOME}/quest-perm.sh",
                 "hint": "600 = rw------- : tylko ty mozesz czytac i pisac, nikt inny nie ma dostepu"},
                {"type": "shell", "cmd": f"ls -la {HOME}/quest-perm.sh",
                 "hint": "potwierdz zmiane uprawnien — powinno byc rw-------"},
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
        "world_flavor": (
            "Kazdy profesjonalny wojownik personalizuje swoja zbroje. "
            "Zmienne srodowiskowe to twoja konfiguracja sesji — PATH mowi gdzie szukac programow. "
            "Aliasy to skroty do ulubionych komend, ~/.zshrc to twoj osobisty grimuar."
        ),
        "title": "Zmienne i aliasy",
        "xp": 20,
        "theory": [
            {"cmd": "echo $HOME",        "what": f"Twoj katalog domowy ({HOME})",       "notes": "$HOME, $USER, $PATH to zmienne systemowe dostepne zawsze. Zdefiniowane przy logowaniu"},
            {"cmd": "echo $PATH",        "what": "Gdzie system szuka programow",        "notes": "Lista katalogow oddzielona :. Gdy piszesz 'git', shell szuka pliku 'git' we wszystkich tych miejscach"},
            {"cmd": "echo $USER",        "what": f"Twoja nazwa uzytkownika ({USERNAME})","notes": "$USER = whoami ale szybciej (bez uruchamiania procesu — to tylko odczyt zmiennej)"},
            {"cmd": "export VAR='val'",  "what": "Ustaw zmienna dla tej sesji",         "notes": "Bez export = tylko w biezacym shellu. Export = dostepna tez dla programow uruchamianych z tego shella"},
            {"cmd": "source ~/.zshrc",   "what": "Przeladuj konfiguracje bez restartu", "notes": "Po dodaniu aliasu do .zshrc musisz source zeby zaczal dzialac w biezacej sesji"},
            {"cmd": "alias ll='ls -laG'","what": "Stworz skrot do komendy",            "notes": "-G = kolory na macOS. Alias istnieje tylko w tej sesji — zeby byl staly, dodaj do ~/.zshrc"},
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
                     "PATH to sciezka wyszukiwania programow — jesli dodasz nowy katalog do PATH,\n"
                     "mozesz uruchamiac skrypty z niego bezposrednio po nazwie.\n\n"
                     "Alias to skrot — np. alias ll='ls -laG' pozwala pisac 'll' zamiast 'ls -laG'.\n"
                     "Aliasy zyja tylko w sesji chyba ze zapiszesz je do ~/.zshrc."
                 )},
                {"type": "shell", "cmd": "echo $PATH | tr ':' '\\n'",
                 "hint": "Pokaz PATH czytelnie — tr ':' '\\n' zamienia : na nowe linie, jeden katalog w linii"},
                {"type": "shell", "cmd": "alias ll='ls -laG'",
                 "hint": "Stworz tymczasowy alias ll  -l = szczegoly  -a = ukryte  -G = kolory na macOS"},
                {"type": "shell", "cmd": "ll ~",
                 "hint": "Przetestuj alias — powinien dzialac jak 'ls -laG ~'"},
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
            "Labirynt Procesow to miasto nikdy nie spiacych demonow. "
            "Kazdy uruchomiony program to demon z unikalnym ID (PID). "
            "Dzisiaj nie walczysz — obserwujesz. ps i top to twoje oczy w tym chaosie."
        ),
        "title": "Obserwacja procesow",
        "xp": 15,
        "theory": [
            {"cmd": "ps",             "what": "Procesy biezacej sesji terminala",       "notes": "Bez argumentow — tylko procesy twojego terminala. Malo uzyteczne samo w sobie"},
            {"cmd": "ps aux",         "what": "WSZYSTKIE procesy systemu",              "notes": "a = wszyscy uzytkownicy  u = format czytelny (user, cpu, mem, cmd)  x = procesy bez terminala"},
            {"cmd": f"ps aux | grep {USERNAME}", "what": "Procesy konkretnego uzytkownika", "notes": f"Podmien {USERNAME} na dowolna nazwe. Wynik zawiera tez sam grep — nie licz go"},
            {"cmd": "top -o cpu",     "what": "Monitor na zywo — sortuj po CPU",       "notes": "Odswierza co sekunde. q = wyjdz  -o cpu = kolumna sortowania  -o mem = sortuj po pamieci"},
            {"cmd": "uptime",         "what": "Czas pracy systemu + obciazenie",        "notes": "Load avg: srednie z 1, 5 i 15 minut. Na 4-rdzeniowym CPU: 4.0 = 100% obciazenie"},
            {"cmd": "echo $$",        "what": "PID biezacego procesu shella",           "notes": "$$ = zmienna specjalna. $! = PID ostatnio uruchomionego w tle procesu"},
        ],
        "boss": {
            "title": "CWICZENIE 6.1 — Obserwator",
            "description": "Przewodnik po Labiryncie uczy cie obserwowac bez interwencji. Przyjrzyj sie procesom systemu:",
            "steps": [
                {"type": "shell", "cmd": "uptime",
                 "hint": "Sprawdz jak dlugo system dziala i srednie obciazenie CPU z ostatnich 1/5/15 minut"},
                {"type": "shell", "cmd": "ps aux | wc -l",
                 "hint": "Policz ile procesow dziala w systemie (pierwsza linia to naglowek — odejmij 1)"},
                {"type": "shell", "cmd": f"ps aux | grep {USERNAME}",
                 "hint": f"Znajdz wszystkie procesy uzytkownika {USERNAME} — twoje programy"},
                {"type": "shell", "cmd": "echo $$",
                 "hint": "Wypisz PID biezacego shella — to numer identyfikacyjny tego terminala"},
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
            {"cmd": "Ctrl+Z",         "what": "Zawies biezacy proces",                 "notes": "Zatrzymuje (nie zabija) proces — mozna wznowic przez bg lub fg"},
            {"cmd": "bg / fg",        "what": "Wznow w tle / przywroc na pierwszy plan","notes": "bg %1 = wznow job 1 w tle (nie zatrzymany)  fg %1 = przywroc na foreground"},
            {"cmd": "jobs -l",        "what": "Lista procesow w tle z PID",            "notes": "-l = long (pokaz PID). Numer joba (%1) rozny od PID"},
            {"cmd": "kill PID",       "what": "Grzeczna prosba o zakonczenie",         "notes": "Wysyla SIGTERM (15) — proces dostaje szanse posprzatac i zakonczyc. Moze ignorowac"},
            {"cmd": "kill -9 PID",    "what": "Natychmiastowe zabicie",                "notes": "-9 = SIGKILL. Jadro systemu zabija natychmiast — proces nie moze zignorowac. Ostatecznosc"},
            {"cmd": "kill %1",        "what": "Zabij pierwszy job z listy jobs",       "notes": "%1 = numer joba z 'jobs', nie PID. Wygodniejsze niz szukanie PID"},
            {"cmd": "lsof -i :8080",  "what": "Co uzywa portu 8080?",                 "notes": "Gdy 'port is already in use' — lsof -i :PORT pokazuje ktory proces zajmuje port"},
        ],
        "boss": {
            "title": "BOSS FIGHT 6.2 — Pogromca Procesow",
            "description": (
                "Wielki Demon Labiryntu wymaga dowodu mestwa — uruchom demona, znajdz go i wyeliminuj. "
                "Trzy zycia — uwazaj na roznice miedzy numerem joba a PID:"
            ),
            "steps": [
                {"type": "info",
                 "text": (
                     "Roznica miedzy numerem joba a PID:\n"
                     "  jobs -l  wypisuje: [1] 12345 Running   sleep 300\n"
                     "           [1] = numer joba (lokalne id w tej sesji)\n"
                     "           12345 = PID (globalny id procesu w systemie)\n\n"
                     "  kill %1  zabija po numerze joba (szybciej)\n"
                     "  kill 12345 zabija po PID\n\n"
                     "sleep 300 = usnij na 300 sekund — idealny demon testowy."
                 )},
                {"type": "shell", "cmd": "sleep 300 &",
                 "hint": "& = uruchom w tle. Shell od razu wraca do promptu. Zobaczysz [1] i PID"},
                {"type": "shell", "cmd": "jobs -l",
                 "hint": "Pokaz liste procesow w tle z PID — -l dodaje kolumne z numerem PID"},
                {"type": "shell", "cmd": "kill %1",
                 "hint": "%1 = pierwszy job z listy jobs (wygodniejsze niz szukanie PID)"},
                {"type": "shell", "cmd": "jobs",
                 "hint": "Lista powinna byc pusta lub pokazywac '[1] Terminated' — demon zostal zabity"},
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
            {"cmd": "ZMIENNA='wartosc'",        "what": "Przypisz wartosc (brak spacji przy =!)",  "notes": "BLAD: ZMIENNA = 'x' (shell mysli ze to komenda 'ZMIENNA')  DOBRZE: ZMIENNA='x'"},
            {"cmd": "echo $ZMIENNA",             "what": "Odczytaj wartosc zmiennej",              "notes": "$ = odwolanie. 'echo $ZMIENNA' w podwojnych cudzyslow interpretuje zmienna"},
            {"cmd": "echo ${ZMIENNA:-domyslna}", "what": "Wartosc domyslna jesli pusta",           "notes": ":- = jesli pusta lub niezdefiniowana, uzyj wartosci po :- zamiast pustego stringa"},
            {"cmd": "echo $(komenda)",           "what": "Wstaw wynik komendy (command subst.)",   "notes": f"np. echo \"Dzis: $(date +%A)\". $() = uruchom komende i wstaw jej output"},
            {"cmd": "echo $((5 * 7))",           "what": "Obliczenia arytmetyczne",                "notes": "(( )) = kontekst matematyczny. Dziala tylko z liczbami calkowitymi. bc dla zmiennoprzecinkowych"},
            {"cmd": "read -p 'Imie: ' IMIE",    "what": "Pobierz input od uzytkownika",           "notes": "-p = prompt (wyswietl pytanie przed czekaniem na input). Wynik trafia do zmiennej IMIE"},
            {"cmd": "unset ZMIENNA",             "what": "Usun zmienna",                           "notes": "Po unset, echo $ZMIENNA = pusty ciag (nie blad). Przydatne do sprzatania w skryptach"},
        ],
        "boss": {
            "title": "CWICZENIE 7.1 — Zmienne",
            "description": "Kowal probuje twoje klocki — cwicz zmienne i substytucje:",
            "steps": [
                {"type": "shell", "cmd": f"IMIE='{USERNAME}' && echo \"Witaj, $IMIE!\"",
                 "hint": "Przypisz zmienna i wypisz z substytucja. && = wykonaj drugie tylko jesli pierwsze OK"},
                {"type": "shell", "cmd": "echo $((3 * 14))",
                 "hint": "Oblicz 3 * 14 uzywajac arytmetyki powloki (( ))"},
                {"type": "shell", "cmd": "echo \"Teraz jest $(date +%H:%M) na ${HOSTNAME:-komputerze}\"",
                 "hint": "$(date +%H:%M) = wstaw aktualny czas  ${HOSTNAME:-komputerze} = zmienna lub default"},
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
            {"cmd": "#!/bin/bash",       "what": "Shebang — pierwsza linia skryptu",   "notes": "Mowi systemowi jakiego interpretera uzyc. #!/bin/zsh dla zsh. Musi byc w linii 1"},
            {"cmd": "NAME='Zenon'",      "what": "Zmienna",                             "notes": "Brak spacji przy =! $NAME = odczyt wartosci. Cudzyslowy chronią spacje w wartości"},
            {"cmd": "echo \"$NAME\"",    "what": "Wypisz zmienna",                     "notes": "Podwojne cudzyslowy interpretuja zmienne i $() — pojedyncze traktuja jako literaly"},
            {"cmd": "$0 $1 $#",          "what": "Argumenty skryptu",                  "notes": "$0 = nazwa skryptu  $1 = pierwszy argument  $# = liczba argumentow  $@ = wszystkie"},
            {"cmd": "if [ -f $1 ]",      "what": "Sprawdz czy plik istnieje",          "notes": "-f = zwykly plik  -d = katalog  -z = pusty string  -n = niepusty string  -e = cokolwiek"},
            {"cmd": "for i in 1 2 3",    "what": "Petla for",                          "notes": "for i in $(seq 1 10) = petla 1-10. do = poczatek ciala  done = koniec petli"},
            {"cmd": "$(( count + 1 ))",  "what": "Obliczenia arytmetyczne",            "notes": "$((wyrazenie)) = oblicz i zamien na wynik. count=$((count+1)) = inkrementacja zmiennej"},
            {"cmd": "chmod +x skrypt.sh","what": "Nadaj prawo wykonywania",            "notes": "Tylko raz! Potem uruchamiac: ./skrypt.sh lub pelna sciezka. Bez ./ shell nie znajdzie go"},
        ],
        "boss": {
            "title": "BOSS FIGHT 7.2 — Kowal Skryptow",
            "description": (
                "Mistrz Kuzni wymaga odlewu pierwszej broni. "
                "Napisz skrypt, nadaj mu prawa, uruchom. Trzy zycia:"
            ),
            "steps": [
                {"type": "shell", "cmd": f"mkdir -p {QP}",
                 "hint": "stworz folder na skrypt"},
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
                     "Zapisz: Ctrl+O + Enter, wyjdz: Ctrl+X\n\n"
                     "Linia po linii:\n"
                     "  #!/bin/bash        — interpreter\n"
                     "  ${1:-'Nieznajomy'} — argument 1 lub default\n"
                     "  $(whoami)          — command substitution w stringu"
                 )},
                {"type": "shell", "cmd": f"chmod +x {QP}/hello.sh",
                 "hint": "nadaj prawo wykonywania — bez tego shell odmowi uruchomienia"},
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
        "world_flavor": (
            "Swiatynia Sieci skrywa tajemnice polaczen miedzy maszynami. "
            "Zanim zaczniesz atakowac zdalne serwery, opanuj diagnostyke: "
            "czy jest polaczenie? Jakie IP? Jaka latencja? ping, ifconfig, host — narzedzia zwiadowcy."
        ),
        "title": "Diagnostyka sieci",
        "xp": 15,
        "theory": [
            {"cmd": "ping -c 3 1.1.1.1",   "what": "Sprawdz polaczenie (3 pakiety)",     "notes": "1.1.1.1 = Cloudflare DNS, zawsze online. -c = count. time = latencja w ms, ttl = hop count"},
            {"cmd": "hostname",             "what": "Nazwa twojego komputera",             "notes": f"Twoj: {HOSTNAME}. hostname -f = pelna kwalifikowana nazwa (FQDN)"},
            {"cmd": "ifconfig | grep inet", "what": "Adresy IP interfejsow sieciowych",   "notes": "inet = IPv4  inet6 = IPv6  lo0 = localhost (127.0.0.1)  en0 = WiFi na Mac"},
            {"cmd": "curl -I URL",          "what": "Pobierz tylko naglowki HTTP",         "notes": "-I = HEAD request: sprawdz status i naglowki bez pobierania body. Szybsze niz GET"},
            {"cmd": "netstat -nr",          "what": "Tablica routingu",                    "notes": "-n = numerycznie (nie rozwiazuj nazw)  -r = routing. Wiersz 0.0.0.0 = domyslna brama"},
            {"cmd": "host domena",          "what": "Zamien domene na IP (DNS lookup)",    "notes": "host google.com = IP Googla. nslookup = bardziej szczegolowy zamiennik"},
        ],
        "boss": {
            "title": "CWICZENIE 8.1 — Diagnostyka",
            "description": "Kapłan Swiatyni uczy cie diagnostyki zanim wpusci glebiej. Sprawdz stan swojej sieci:",
            "steps": [
                {"type": "shell", "cmd": "ping -c 3 1.1.1.1",
                 "hint": "Wyslij 3 pakiety do 1.1.1.1 (Cloudflare DNS). -c 3 = zakoncz po 3 pakietach automatycznie"},
                {"type": "shell", "cmd": "hostname",
                 "hint": f"Sprawdz nazwe komputera — powinno byc: {HOSTNAME}"},
                {"type": "shell", "cmd": "ifconfig | grep 'inet '",
                 "hint": "'inet ' ze spacja na koncu = tylko IPv4, nie lapie inet6"},
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
            {"cmd": "curl -s URL",         "what": "Pobierz dane bez paska postepu",     "notes": "-s = silent: brak paska postepu i statystyk. Idealne w skryptach gdy chcesz tylko dane"},
            {"cmd": "curl -o plik URL",    "what": "Pobierz i zapisz do pliku",          "notes": "-o = output: podaj nazwe pliku. -O (wielka) = uzyj nazwy z URL"},
            {"cmd": "networkQuality",      "what": "Test predkosci internetu (macOS 12+)","notes": "Wbudowane narzedzie macOS do pomiaru upload/download. Alternatywa: speedtest-cli przez brew"},
            {"cmd": "ssh user@serwer",     "what": "Polacz sie z serwerem SSH",          "notes": "Domyslny port: 22. Pierwsze polaczenie pyta o fingerprint — wpisz 'yes' zeby zapisac"},
            {"cmd": "ssh -p 2222 u@s",     "what": "Polacz sie na innym porcie",         "notes": "-p = port. Wiele serwerow zmienia port z 22 na inny dla bezpieczenstwa"},
            {"cmd": "scp plik u@s:/path",  "what": "Kopiuj plik na serwer",             "notes": "scp = secure copy, ten sam protokol co SSH. scp u@s:/path/plik . = sciagnij z serwera"},
            {"cmd": "ssh-keygen -t ed25519","what": "Generuj klucz SSH",                "notes": "ed25519 = nowoczesny, szybki, bezpieczny algorytm. Generuje pare: klucz prywatny + .pub"},
        ],
        "boss": {
            "title": "BOSS FIGHT 8.2 — Sieciowy Mag",
            "description": (
                "Wielki Kaplán Swiatyni wymaga dowodu opanowania sieci. "
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
                 "hint": "Pokaz swoje publiczne IP — -s = silent, bez paska postepu"},
                {"type": "shell", "cmd": "ping -c 4 google.com",
                 "hint": "-c 4 = wyslij tylko 4 pakiety i zakoncz automatycznie (bez -c pinguje wiecznie)"},
                {"type": "shell", "cmd": "curl -s https://api.github.com | head -5",
                 "hint": "Pobierz dane z publicznego API GitHub i pokaz tylko 5 linii (JSON)"},
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
            {"cmd": "git init",           "what": "Stworz nowe repo (.git folder)",     "notes": "Tworzy ukryty folder .git z cala historia. Nie dotykaj .git recznie"},
            {"cmd": "git status",         "what": "Co sie zmienilo?",                   "notes": "Uzywaj czesto! Pokazuje: niesledzone pliki, zmodyfikowane, gotowe do commita (stage)"},
            {"cmd": "git add plik.txt",   "what": "Dodaj plik do stage",                "notes": "Stage = obszar przygotowany do commita. Jak lista zakupow przed realizacja"},
            {"cmd": "git add .",          "what": "Dodaj WSZYSTKIE zmiany do stage",    "notes": ". = biezacy katalog i podkatalogi. Uwazaj — dodaje tez nieumyslne zmiany"},
            {"cmd": "git commit -m 'msg'","what": "Zapisz stage jako commit",           "notes": "-m = krotki opis zmian. Dobry opis: 'fix: null pointer in auth' nie 'fix bug'"},
            {"cmd": "git log --oneline",  "what": "Historia commitow",                  "notes": "--oneline = 1 linia na commit. --graph = drzewo ASCII. --all = wszystkie branche"},
            {"cmd": "git diff",           "what": "Zmiany ktore NIE sa w stage",        "notes": "--staged = zmiany ktore SA juz w stage. git diff HEAD = wszystkie od ostatniego commita"},
        ],
        "boss": {
            "title": "CWICZENIE 9.1 — Git Basics",
            "description": "Stroz Otchlani prowadzi cie przez pelny cykl Gita — init, add, commit:",
            "steps": [
                {"type": "shell", "cmd": f"git init {QP}",
                 "hint": "zainicjuj repo git w folderze quest-project — tworzy .git/"},
                {"type": "shell", "cmd": f"echo 'Hello Git z {HOSTNAME}' > {QP}/plik.txt",
                 "hint": "stworz plik z trescia — bedziesz go commitowac"},
                {"type": "shell", "cmd": f"git -C {QP} status",
                 "hint": "-C = zmien katalog do {QP}. Plik powinien byc jako 'untracked files'"},
                {"type": "shell", "cmd": f"git -C {QP} add plik.txt",
                 "hint": "dodaj plik do stage — przenosi z 'untracked' do 'changes to be committed'"},
                {"type": "shell", "cmd": f"git -C {QP} commit -m 'Initial commit'",
                 "hint": "zapisz commit z wiadomoscia — stage zostaje zamrozony jako punkt w historii"},
                {"type": "shell", "cmd": f"git -C {QP} log --oneline",
                 "hint": "sprawdz historie — powinien byc jeden commit z hashem i wiadomoscia"},
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
        "world_flavor": (
            "Branch to rownolegly swiat — pracujesz na feature bez psuciai main. "
            "Gdy feature gotowy, merge laczy swiat powrotem. "
            "Konflikty to starcia miedzy wersjami — Git pyta kto ma racje."
        ),
        "title": "Branche i merge",
        "xp": 30,
        "theory": [
            {"cmd": "git branch",          "what": "Pokaz liste branchy",               "notes": "* = aktualny branch. -a = pokaz tez zdalne. -d feature = usun (tylko zmergowany)"},
            {"cmd": "git branch feature",  "what": "Stworz nowy branch",               "notes": "Nie przelacza sie automatycznie — jestes dalej na tym samym branchu"},
            {"cmd": "git checkout feature","what": "Przelacz sie na branch",            "notes": "Nowoczesna alternatywa: git switch feature. HEAD wskazuje teraz na feature"},
            {"cmd": "git checkout -b feat","what": "Stworz i przelacz w jednym",       "notes": "-b = branch: skrot z dwoch komend: git branch + git checkout. Czesciej uzywane"},
            {"cmd": "git merge feature",   "what": "Polacz branch z aktualnym",         "notes": "Bedac na main: git merge feature. Jesli fast-forward mozliwy — brak commit merge"},
            {"cmd": "git branch -d feat",  "what": "Usun branch",                      "notes": "-d = tylko jesli juz zmergowany (bezpieczne)  -D = na sile nawet bez merge"},
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
                 "hint": "stworz repo"},
                {"type": "shell", "cmd": f"echo 'main' > {QP}/plik.txt && git -C {QP} add . && git -C {QP} commit -m 'init'",
                 "hint": "stworz pierwszy commit na main (trzy komendy lancuchem &&)"},
                {"type": "shell", "cmd": f"git -C {QP} checkout -b feature",
                 "hint": "-b = stworz i przelacz na nowy branch feature"},
                {"type": "shell", "cmd": f"echo 'feature' >> {QP}/plik.txt && git -C {QP} add . && git -C {QP} commit -m 'add feature'",
                 "hint": "dodaj zmiane i commituj na feature branch — historia feature rozni sie od main"},
                {"type": "shell", "cmd": f"git -C {QP} checkout main",
                 "hint": "wroc na main — plik.txt ma tylko 'main', bo feature jest na oddzielnym branchu"},
                {"type": "shell", "cmd": f"git -C {QP} merge feature",
                 "hint": "zmerguj feature do main — plik.txt bedzie mial obie linie"},
                {"type": "shell", "cmd": f"git -C {QP} log --oneline --graph",
                 "hint": "--graph = drzewo branchy w ASCII — widac gdzie branch i gdzie merge"},
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
        "world_flavor": (
            "Stanales przed Tronem. Ostatnie sekrety nie sa trudne — sa eleganckie. "
            "Brace expansion, process substitution, find -exec — narzedzia ktore skracaja 10 linii do jednej. "
            "Arcymistrz nie uderza wiecej niz trzeba."
        ),
        "title": "Zaawansowane techniki",
        "xp": 40,
        "theory": [
            {"cmd": "mkdir -p proj/{src,tests}/{v1,v2}", "what": "Brace expansion: 4 katalogi naraz",  "notes": "{a,b} = lista (src i tests)  zagniezdzone {v1,v2} = kazdy z v1 i v2. Bash/zsh rozwijaja to PRZED wykonaniem"},
            {"cmd": "touch plik{1..10}.txt",             "what": "Stworz 10 plikow jednym poleceniem","notes": "{1..10} = sekwencja od 1 do 10. {a..z} = alfabet. {01..10} = z zerowaniem"},
            {"cmd": "echo $(date +%H:%M)",               "what": "Wstaw wynik komendy",               "notes": "$() = command substitution: uruchom i wstaw output. Zagniezdzone: $(echo $(date))"},
            {"cmd": "diff <(ls dir1) <(ls dir2)",        "what": "Porownaj outputy dwoch komend",     "notes": "<() = process substitution: output komendy jak plik tymczasowy. Diff widzi 'dwa pliki'"},
            {"cmd": "find . -mtime +30 -exec rm {} \\;", "what": "Znajdz i usun pliki starsze niz 30 dni", "notes": "-mtime +30 = zmodyfikowane >30 dni temu  -exec = wykonaj komende dla kazdego  {} = miejsce na znaleziony plik  \\; = koniec -exec"},
            {"cmd": "cmd1 & cmd2 & wait",                "what": "Uruchom rownolegle i czekaj",       "notes": "& po kazdej = uruchom w tle  wait = poczekaj az wszystkie procesy w tle sie skoncza"},
            {"cmd": "awk -F: '{print $1}' /etc/passwd",  "what": "Wypisz pierwsza kolumne z : jako sep.", "notes": "-F: = separator pol  $1 = pierwsza kolumna  $NF = ostatnia  NR = numer wiersza"},
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
                     "  {}  = miejsce dla znalezionego pliku\n"
                     "  \\; = koniec -exec (srednik musi byc poprzedzony \\ )"
                 )},
                {"type": "shell", "cmd": f"mkdir -p {HOME}/projekt/{{src,tests,docs}}/{{v1,v2}}",
                 "hint": "tworzy 6 katalogow naraz: src/v1, src/v2, tests/v1, tests/v2, docs/v1, docs/v2"},
                {"type": "shell", "cmd": f"ls -R {HOME}/projekt",
                 "hint": "sprawdz pelna strukture (-R = recursive) — powinno byc 6 katalogow"},
                {"type": "shell", "cmd": f"touch {HOME}/projekt/plik{{1..5}}.txt",
                 "hint": "{{1..5}} = sekwencja: tworzy plik1.txt plik2.txt ... plik5.txt naraz"},
                {"type": "shell", "cmd": f"find {HOME}/projekt -name '*.txt' | wc -l",
                 "hint": "policz ile plikow .txt zostalo stworzonych — powinno byc 5"},
                {"type": "shell", "cmd": f"rm -r {HOME}/projekt",
                 "hint": "posprzataj — ostatni raz!"},
                {"type": "confirm",
                 "prompt": "Gratulacje Arcymistrzu! Czy ukonczyłes Terminal Quest?"},
            ],
        },
    },
]
