// Terminal Quest — English quest translations
// Loaded after quests.js, before game.js

if (LANG === 'en') {

  // ── World names ───────────────────────────────────────────────────────────────
  Object.assign(WORLD_NAMES, {
    0:  'macOS Setup',
    1:  'Starting Village',
    2:  'File Forest',
    3:  'Pipeline Mine',
    4:  'Editor Tower',
    5:  'Permission Fortress',
    6:  'Process Labyrinth',
    7:  'Script Forge',
    8:  'Network Temple',
    9:  'Git Abyss',
    10: "Arcmaster's Throne",
  });

  // ── Ranks ─────────────────────────────────────────────────────────────────────
  const _RANKS_EN = [
    ['Shell Novice',        'Lost in the Shell'],
    ['Console Wanderer',    'File Seeker'],
    ['Pipeline Lord',       'Command Linker'],
    ['Edit Mage',           'Vim Tamed'],
    ['Gate Guardian',       'Permissions Lord'],
    ['Process Slayer',      'Zombie Killer'],
    ['Script Smith',        'Automation Maker'],
    ['Network Mage',        'SSH Traveler'],
    ['Repository Lord',     'Git Master'],
    ['TERMINAL ARCMASTER',  'Console Legend'],
  ];
  _RANKS_EN.forEach(([name, title], i) => { RANKS[i][1] = name; RANKS[i][2] = title; });

  // ── World passwords (English passwords active) ────────────────────────────────
  Object.assign(WORLD_PASSWORDS, WORLD_PASSWORDS_EN);

  // ── Merge helper ──────────────────────────────────────────────────────────────
  function _applyEN(quest, en) {
    if (en.world_flavor !== undefined) quest.world_flavor      = en.world_flavor;
    if (en.title        !== undefined) quest.title             = en.title;
    if (en.boss_title   !== undefined) quest.boss.title        = en.boss_title;
    if (en.boss_desc    !== undefined) quest.boss.description  = en.boss_desc;
    if (en.theory) {
      en.theory.forEach((t, i) => {
        if (!t || !quest.theory[i]) return;
        Object.assign(quest.theory[i], t);
      });
    }
    if (en.steps) {
      en.steps.forEach((s, i) => {
        if (!s || !quest.boss.steps[i]) return;
        Object.assign(quest.boss.steps[i], s);
      });
    }
  }

  // ── Quest translations ────────────────────────────────────────────────────────
  const _EN = {

  // ═══════════════════════════════════════════════════
  // WORLD 0
  // ═══════════════════════════════════════════════════
  '0.1': {
    world_flavor: "Every great warrior checks their equipment before battle. Homebrew is your personal armorer — it installs any tool with a single word. Without it, you can't go anywhere.",
    title: 'Homebrew — package manager',
    boss_title: 'EXERCISE 0.1 — Equipment',
    boss_desc: 'The gate guardian checks your equipment before letting you into the Village. Prove you have what it takes:',
    theory: [
      {cmd: 'brew install name',      what: 'Install a program',            notes: 'e.g. brew install git — Homebrew finds the package in its registry and installs it'},
      {cmd: 'brew uninstall name',    what: 'Uninstall a program',          notes: "Removes the program and its files, doesn't touch dependencies"},
      {                               what: 'What do I have installed?',    notes: 'List of all packages installed by Homebrew'},
      {                               what: 'Update package list',          notes: "Downloads information about new versions — doesn't install anything yet"},
      {                               what: 'Update all packages',          notes: 'After brew update, upgrade actually downloads new versions'},
      {                               what: 'Install GUI application',      notes: '--cask = .app applications (iTerm2, VSCode, Firefox) — not CLI tools'},
    ],
    steps: [
      {hint: "You should see 'Homebrew X.Y.Z'"},
      {hint: "You should see 'git version X.Y.Z'"},
    ],
  },

  // ═══════════════════════════════════════════════════
  // WORLD 1
  // ═══════════════════════════════════════════════════
  '1.1': {
    world_flavor: "You wake up in the terminal. The blinking cursor waits like a faithful servant ready to execute commands. Before you venture out, you must learn to move — pwd is your compass, ls is your flashlight, cd is your legs. These three commands are the foundation of everything that comes later.",
    title: 'First steps',
    boss_title: 'EXERCISE 1.1 — Navigator',
    boss_desc: 'The Village guide gives you a test — navigate through 5 known addresses and return home:',
    theory: [
      {                               what: 'Where am I? (Print Working Directory)',   notes: `Always prints the full absolute path, e.g. ${HOME}`},
      {                               what: "What's here? Lists files in directory",   notes: 'Without argument = current directory. Provide path: ls /etc'},
      {                               what: 'Show EVERYTHING with details',            notes: '-l = details (permissions, size, date)  -a = hidden files (names starting with .)'},
      {cmd: 'cd dir',                 what: 'Go to directory (Change Directory)',      notes: 'Relative path: cd Documents  absolute: cd /etc'},
      {                               what: 'Go back one directory up',                notes: '.. = always means parent directory. ../../ = two levels up'},
      {                               what: `Return home (${HOME})`,                  notes: '~ is shortcut to your home directory, works everywhere'},
      {                               what: 'Go back to where I was last',             notes: 'Shell remembers previous location — - is like the Back button'},
      {                               what: 'Clear the screen',                        notes: "Ctrl+L does the same — but history doesn't disappear, just scrolls the screen"},
    ],
    steps: [
      {hint: '/tmp = temporary files, cleaned after restart'},
      {hint: '/var/log = system logs — the system records what happens here'},
      {hint: '/usr/local = this is where Homebrew installs programs'},
      {hint: '/etc = system configuration — text files with settings'},
      {hint: '~/Documents = your Documents folder  ~ = shortcut to home'},
      {hint: 'Return to home directory'},
      {hint: `You should see ${HOME}`},
    ],
  },

  '1.2': {
    world_flavor: "A spy always gathers intelligence before action. Before attacking a problem, check who you are, where you are, and what surrounds you. whoami, date, uname — your reconnaissance tools.",
    title: 'Reconnaissance',
    boss_title: 'EXERCISE 1.2 — Intelligence',
    boss_desc: 'An old spy in the tavern gives you a list of intelligence questions — answer using terminal commands:',
    theory: [
      {                               what: 'Who am I? Prints the username',           notes: `Yours: ${USERNAME}  Important when using sudo or ssh to another server`},
      {                               what: 'Current date and time',                   notes: "date '+%Y-%m-%d' = date only  date '+%H:%M' = time only"},
      {                               what: 'Monthly calendar',                        notes: 'cal 2026 = full year  cal 3 2026 = March 2026'},
      {                               what: 'System info (OS, kernel, architecture)',  notes: "-a = all. Look for 'arm64' = Apple Silicon, 'x86_64' = Intel"},
      {cmd: "echo 'text'",            what: 'Print text to screen',                   notes: 'echo $HOME = value of environment variable'},
      {                               what: 'History of recent commands',              notes: "history | grep git = only commands containing 'git'"},
      {                               what: 'Manual (documentation) for command',      notes: '/ = search  n = next result  q = quit'},
    ],
    steps: [
      {hint: `Prints username — should be: ${USERNAME}`},
      {hint: "Shows today's day of week and time"},
      {hint: 'Shows system and architecture (arm64 = Apple Silicon)'},
      {hint: 'List of recent commands — history of your actions'},
    ],
  },

  '1.3': {
    world_flavor: "A true warrior doesn't fumble in pockets — their fingers go where needed automatically. Keyboard shortcuts are the difference between amateur and professional. One shortcut can save a thousand clicks.",
    title: 'Keyboard shortcuts',
    boss_title: 'BOSS FIGHT 1.3 — Shortcut Master',
    boss_desc: 'The Village Guardian blocks the gate and asks about shortcuts. Prove you know them — three shared lives:',
    theory: [
      {                               what: 'AUTOCOMPLETE — the most important shortcut',   notes: 'Tab twice = show all possibilities'},
      {                               what: 'Interrupt current command',                    notes: 'Sends SIGINT signal to process. Saves you when a command hangs'},
      {                               what: 'Search backwards through command history',     notes: 'Type fragment, ENTER = execute, Ctrl+R again = next result'},
      {                               what: 'Clear the screen',                             notes: "Same as clear — but doesn't delete history"},
      {                               what: 'Jump to beginning of line',                    notes: 'A for stArt. Useful when adding sudo at the beginning of a long command'},
      {                               what: 'Jump to end of line',                          notes: 'E for End. Partner with Ctrl+A'},
      {                               what: 'Delete word to the left',                      notes: 'Faster than holding Backspace'},
      {                               what: 'Delete entire line from cursor leftward',      notes: 'Ctrl+K deletes from cursor rightward'},
      {                               what: 'Repeat last command',                          notes: 'Most often: sudo !! when last command rejected due to missing permissions'},
      {cmd: 'arrow UP',               what: 'Previous command in history',                  notes: 'DOWN = next'},
    ],
    steps: [
      {question: 'What shortcut do you use to INTERRUPT a hung command?',
       hint: 'Sends SIGINT signal — kills what is currently running in terminal'},
      {question: 'What shortcut SEARCHES backwards through command history?',
       hint: 'Opens interactive reverse search'},
      {question: 'What shortcut JUMPS to the BEGINNING of the line?',
       hint: 'A for stArt — moves cursor to the very beginning of the typed command'},
      {question: 'You are typing a long command and want to DELETE the last word. What shortcut?',
       hint: 'Faster than holding Backspace — deletes from cursor to previous space'},
      {question: 'What shortcut JUMPS to the END of the line?',
       hint: 'E for End — partner with Ctrl+A (beginning)'},
      {question: 'What shortcut REPEATS the last executed command without retyping?',
       hint: 'Two exclamation marks — shell history'},
    ],
  },

  // ═══════════════════════════════════════════════════
  // WORLD 2
  // ═══════════════════════════════════════════════════
  '2.1': {
    world_flavor: "You enter the dense File Forest. Everything here is a tree — directories are branches, files are leaves. You can build an entire project with one command or level it to the ground just as quickly. You'll master creation and destruction — no Trash, no warnings.",
    title: 'Creation and destruction',
    boss_title: 'EXERCISE 2.1 — Builder and Destroyer',
    boss_desc: 'The Forest Spirit gives you a task: build a project structure, check it, and clean up after yourself:',
    theory: [
      {cmd: 'touch file.txt',         what: 'Create empty file',                    notes: "If file exists — only updates modification date, doesn't destroy contents"},
      {                               what: 'Create directory',                      notes: 'Error if directory already exists — use -p to avoid this'},
      {                               what: 'Create nested directories',             notes: '-p = parents: creates all missing directories along the way'},
      {cmd: 'cp source dest',         what: 'Copy file',                            notes: 'If dest exists — overwrites WITHOUT asking! cp -i = ask before overwriting'},
      {cmd: 'cp -r folder copy',      what: 'Copy entire directory',                notes: '-r = recursive: enters subdirectories and copies everything'},
      {cmd: 'mv old new',             what: 'Move or rename',                       notes: 'Same command does both things'},
      {cmd: 'rm file',                what: 'DELETE file (IRREVERSIBLE!)',           notes: "No Trash — rm deletes permanently. Ctrl+Z won't help"},
      {                               what: 'DELETE directory with contents',        notes: '-r = recursive: enters and deletes everything. rm -rf / = end of system!'},
      {                               what: 'Delete EMPTY directory',               notes: 'Refuses if not empty — safer alternative to rm -r'},
    ],
    steps: [
      {hint: '-p = parents  {a,b} = brace expansion: creates several directories at once'},
      {hint: 'touch = create empty file  .sh = bash script extension'},
      {hint: 'helper functions file in subdirectory'},
      {hint: 'documentation  .md = markdown'},
      {hint: 'test file'},
      {hint: '-R = recursive: shows contents of all subdirectories'},
      {hint: '-r = recursive: deletes directory with all contents IRREVERSIBLY'},
      {hint: 'no output = success, folder is gone'},
    ],
  },

  '2.2': {
    world_flavor: "The Forest hides many secrets written in files. You don't have to read everything — just peek at the beginning or end, count lines. cat isn't the answer to everything: a large file will flood the terminal — use less.",
    title: 'Reading files',
    boss_title: 'EXERCISE 2.2 — Reader',
    boss_desc: 'The Forest Librarian gives you a scroll with 100 lines — analyze it without opening an editor:',
    theory: [
      {cmd: 'cat file',               what: 'Show entire file contents',            notes: 'Use only for small files (up to ~50 lines). For large ones — less'},
      {cmd: 'less file',              what: 'File viewer/pager',                    notes: 'Arrows / PageUp/Down  /search  n — next  q — quit'},
      {cmd: 'head -n 10 file',        what: 'First 10 lines',                       notes: '-n = how many lines. head -1 file = only first line (e.g. CSV header)'},
      {cmd: 'tail -n 10 file',        what: 'Last 10 lines',                        notes: '-n = how many lines. tail -1 = last line'},
      {cmd: 'tail -f file',           what: 'Watch file live',                      notes: '-f = follow. New lines appear automatically. Ctrl+C to stop'},
      {cmd: 'wc -l file',             what: 'Count lines',                          notes: 'wc without flags = lines words bytes all at once. -l = lines  -w = words  -c = bytes'},
      {cmd: 'wc -w file',             what: 'Count words',                          notes: 'Word = sequence of characters separated by spaces'},
      {cmd: 'diff file1 file2',       what: 'Compare two files',                    notes: '< = line only in first file  > = only in second'},
    ],
    steps: [
      {hint: 'create folder for files'},
      {hint: 'seq 1 100 = generate numbers from 1 to 100  > = save to file'},
      {hint: 'Count how many lines the file has — should be 100'},
      {hint: 'First 5 lines — check that file starts with 1'},
      {hint: 'Last 3 lines — check that file ends with 100'},
      {hint: 'Lines 45-55: head takes first 55, tail takes last 11 of those 55'},
      {hint: 'clean up'},
      {hint: 'no output = success'},
    ],
  },

  '2.3': {
    world_flavor: "The Tracker knows that walking through the forest isn't enough — you must know how to search it. find searches for files by name, size, modification date. grep searches for text inside files. Two different tools — both priceless.",
    title: 'Searching',
    boss_title: 'BOSS FIGHT 2.3 — Tracker',
    boss_desc: 'The Forest Guardian, an old tracker, puts you to the test. Create a project with content, find files, and search them. Three lives:',
    theory: [
      {                               what: 'Find files by name',                    notes: '. = search here and in subdirectories  * = any sequence of characters'},
      {                               what: 'Find only directories',                 notes: '-type f = files  -type l = symbolic links  -type d = directories'},
      {                               what: 'Find files larger than 1MB',            notes: '+1M = larger  -1M = smaller  Units: k, M, G'},
      {cmd: "grep 'text' file",       what: 'Search for text in file',              notes: 'Prints ENTIRE lines containing the pattern'},
      {cmd: "grep -r 'text' .",       what: 'Search recursively in directory',      notes: '-r = recursive: search all subdirectories'},
      {cmd: "grep -i 'text' file",    what: 'Search (case insensitive)',             notes: "-i = ignore case: 'Error' will find ERROR, error, Error"},
      {cmd: "grep -n 'text' file",    what: 'Search with line numbers',             notes: '-n = line numbers next to results'},
      {                               what: 'Where is the program installed?',       notes: 'Shows full path: /usr/bin/python3'},
    ],
    steps: [
      {text: "The Tracker says: 'Difference between find and grep:\n  find  — searches for FILES by name, size, date\n  grep  — searches for TEXT inside files\n\nWrap wildcards in find with quotes: find . -name '*.sh'\nWithout quotes, the shell would expand *.sh before find sees it.'"},
      {hint: 'create directory structure'},
      {hint: "$'...' = zsh syntax for \\n (newline inside string)"},
      {hint: 'second file with content'},
      {hint: 'Find all .sh files in project'},
      {hint: '-r = search all subdirectories recursively'},
      {hint: '| wc -l = count how many lines grep returned'},
      {hint: 'clean up'},
      {hint: 'no output = success'},
    ],
  },

  // ═══════════════════════════════════════════════════
  // WORLD 3
  // ═══════════════════════════════════════════════════
  '3.1': {
    world_flavor: "The mine hides treasures deep inside — you must link tools like wagons, each carrying the output of the previous to the input of the next. Pipe | is the Unix philosophy: each program does ONE thing well, you chain them together.",
    title: 'Pipe — chaining commands',
    boss_title: 'EXERCISE 3.1 — Linker',
    boss_desc: 'The Pipeline Miner teaches you to chain commands. Connect them with pipes:',
    theory: [
      {                               what: 'Huge listing → scrollable',             notes: '| = pass stdout of left command as stdin of right'},
      {                               what: 'How many files are in the directory?',  notes: 'wc -l counts lines of ls output'},
      {                               what: 'Only .txt files from listing',          notes: 'grep filters lines — prints only those containing the pattern'},
      {                               what: 'Sort by size',                          notes: '-k5 = 5th column (size in ls -la)  -n = numerically'},
      {                               what: 'Last 5 commands with cd',              notes: 'Chain of 3 commands! history → filter grep → last 5 tail'},
      {                               what: 'How many chrome processes running?',    notes: 'Result includes grep itself — subtract 1 from result'},
    ],
    steps: [
      {hint: 'How many files/directories are in your home?'},
      {hint: '5 largest elements in home: -r = reverse  -n = numerically'},
      {hint: 'How many times did you use the cd command? Three commands in chain'},
    ],
  },

  '3.2': {
    world_flavor: "Every command has three streams: stdin (input), stdout (output), stderr (errors). Redirections are valves on these streams — you decide where data goes. > overwrites, >> appends, 2> catches errors, /dev/null is a virtual trash.",
    title: 'Redirections',
    boss_title: 'EXERCISE 3.2 — Redirections',
    boss_desc: 'The Redirection Master tests your knowledge of data streams:',
    theory: [
      {                               what: 'Write stdout to file (OVERWRITES!)',    notes: "Creates file if doesn't exist. If exists — destroys contents without asking"},
      {                               what: 'Append to file',                        notes: "Doesn't destroy existing data — adds to the end"},
      {                               what: 'Read from file as stdin',               notes: 'sort < list.txt same as sort list.txt'},
      {                               what: 'Redirect stderr (errors)',              notes: '2>/dev/null = ignore errors. /dev/null = virtual trash'},
      {                               what: 'Redirect stdout AND stderr together',   notes: 'Shortcut for > file 2>&1'},
      {                               what: 'Display AND save simultaneously',       notes: 'Like a Y-splitter — data goes both to screen and to file'},
    ],
    steps: [
      {hint: 'create folder'},
      {hint: '> = write stdout to file (overwrites if exists)'},
      {cmd: `echo '# My list' >> ${QP}/listing.txt`,
       hint: ">> = append to end (doesn't overwrite existing data)"},
      {hint: '< = use file as stdin for command'},
      {hint: '2>/dev/null = ignore errors when no access to system directories'},
      {hint: 'clean up'},
    ],
  },

  '3.3': {
    world_flavor: "The most powerful tools hide at the bottom of the mine. sort, uniq, cut, sed, awk — in a master's hands they create one-liners capable of analyzing gigabytes of logs in a second.",
    title: 'Powerful text tools',
    boss_title: 'BOSS FIGHT 3.3 — The Great Mine Boss: Log Analysis',
    boss_desc: 'The Great Miner challenges you: create a server log and analyze it like a real administrator. Three lives — each command must be precise:',
    theory: [
      {                               what: 'Sort alphabetically',                   notes: '-n = numerically  -r = reverse  -rn = from largest'},
      {                               what: 'Remove adjacent duplicates',            notes: "ALWAYS precede with sort! uniq doesn't see non-adjacent duplicates"},
      {                               what: 'Count occurrences',                     notes: '-c = count: adds counter before each line'},
      {                               what: 'Extract column',                        notes: '-d = delimiter  -f1 = first column'},
      {                               what: 'Replace characters (lowercase to uppercase)', notes: 'Only with pipe — does not accept file directly'},
      {                               what: 'Find and replace text',                 notes: 's = substitute  g = global (all in line)'},
      {                               what: 'Print first column',                    notes: '$1 = first column  $NF = last  -F: = separator :'},
      {                               what: 'Convert stdin to arguments',            notes: "find . -name '*.tmp' | xargs rm"},
    ],
    steps: [
      {text: "Task: analyze HTTP server access logs.\n\nLog format: IP METHOD PATH HTTP_CODE\nYou will look for:\n  1. Which IP sent the most requests\n  2. Which requests ended in an error (4xx and 5xx codes)\n\nKey: cut → sort → uniq -c → sort -rn is the classic counting chain."},
      {hint: 'prepare folder'},
      {hint: 'printf creates log file with 6 entries — format: IP METHOD PATH CODE'},
      {hint: 'Which IP has most requests? cut→sort→uniq -c→sort -rn'},
      {hint: '4xx and 5xx errors: -E = extended regex  [45] = 4 or 5  $ = end of line'},
      {hint: 'clean up'},
    ],
  },

  // ═══════════════════════════════════════════════════
  // WORLD 4
  // ═══════════════════════════════════════════════════
  '4.1': {
    world_flavor: "On the lower level of the Editor Tower you'll learn that you don't always have to go inside. You can often modify a file from the outside with one command. echo, sed, printf — faster than opening an editor when the change is small.",
    title: 'Editing without an editor',
    boss_title: 'EXERCISE 4.1 — Editing Without Editor',
    boss_desc: 'A person without an editor on the lower level of the Tower — manipulate files without opening anything:',
    theory: [
      {cmd: "echo 'text' > file.txt",   what: 'Create file with content (overwrites)',  notes: '> overwrites — if file exists, previous content is gone'},
      {cmd: "echo 'more' >> file.txt",  what: 'Append to end of file',                  notes: "Safe — doesn't destroy existing data"},
      {cmd: 'cat > file.txt',           what: 'Type from keyboard to file',             notes: 'Ctrl+D = end (EOF = End Of File) — saves'},
      {cmd: "sed -i 's/old/new/g' file",what: 'Replace text in file (in-place)',        notes: "-i = in-place: modifies the file itself. On macOS: sed -i '' 's/...' file"},
      {cmd: "sed -n '5,10p' file",      what: 'Print lines 5-10',                      notes: "-n = don't print by default  p = print for range"},
      {cmd: "printf 'line1\\nline2\\n'",what: 'Print text interpreting \\n',            notes: 'printf understands \\n as newline'},
    ],
    steps: [
      {hint: 'create folder'},
      {cmd: `printf 'name: ${USERNAME}\\nhost: ${HOSTNAME}\\ndate: 2026\\n' > ${QP}/info.txt`,
       hint: 'printf with \\n creates a multi-line file at once'},
      {hint: 'check file contents — should be 3 lines',
       output: `name: ${USERNAME}\nhost: ${HOSTNAME}\ndate: 2026`},
      {hint: '>> = append to end without overwriting'},
      {hint: "sed -i '' on macOS (empty string after -i = no backup)"},
      {hint: 'clean up'},
    ],
  },

  '4.2': {
    world_flavor: "First floor of the Tower: nano. Simple, friendly, with shortcuts visible at the bottom. ^ means Ctrl. Ideal for beginners and quick fixes. You don't have to love it — just know how to exit and save.",
    title: 'Nano — easier start',
    boss_title: 'EXERCISE 4.2 — Nano',
    boss_desc: 'The guardian of the first floor gives you a simple test with nano:',
    theory: [
      {cmd: 'nano file.txt',  what: "Open file (creates if doesn't exist)",  notes: 'Shortcuts visible at bottom. ^ = Ctrl'},
      {                       what: 'Save (O for Output/Write Out)',          notes: 'Enter confirms filename'},
      {                       what: 'Exit',                                   notes: 'If unsaved changes — asks: Y = yes, N = no'},
      {                       what: 'Search for text',                        notes: 'Enter = next result'},
      {                       what: 'Cut entire line',                        notes: ''},
      {                       what: 'Paste cut line (UnCut)',                 notes: 'Pair with Ctrl+K — cut and paste = copy line'},
      {                       what: 'Help — full list of shortcuts',          notes: 'Q or Ctrl+X to exit help'},
    ],
    steps: [
      {text: "Open nano: nano ~/quest-nano.txt\nType any text, save with Ctrl+O + Enter, exit with Ctrl+X"},
      {hint: 'Check that file was saved — you should see your text',
       output: "[Your text saved in nano]\n[Nano works correctly!]"},
      {hint: 'clean up'},
    ],
  },

  '4.3': {
    world_flavor: "At the top of the Tower lives Vim — a legendary editor from 1976, used by millions to this day. Difficult at first, but once mastered, faster than any other. Its secret: modes. Normal is the foundation, Insert is for typing, :command is for actions.",
    title: 'Vim — legendary weapon',
    boss_title: 'BOSS FIGHT 4.3 — Tower Master of the Editor',
    boss_desc: "The Tower Master points to the terminal: 'There are no shortcuts to learning Vim. There is only vimtutor.' Three lives:",
    theory: [
      {                       what: 'Enter INSERT mode — here you can type',  notes: 'After opening Vim you ARE in NORMAL mode and CANNOT type!'},
      {                       what: 'Return to NORMAL mode — always safe',    notes: "Don't know which mode? Press ESC several times"},
      {                       what: 'Save file',                              notes: 'Must be in NORMAL mode. If file has no name: :w name.txt'},
      {                       what: 'Exit',                                   notes: 'Error if unsaved changes'},
      {                       what: 'Save and exit',                          notes: 'Most used. Alternative: ZZ in NORMAL mode'},
      {                       what: 'Exit WITHOUT saving',                    notes: '! = force. Emergency escape'},
      {                       what: 'Navigation: left down up right',         notes: "Like arrow keys but hands don't leave home row"},
      {                       what: 'Beginning / end of file',               notes: 'gg = first line  G = last  5G = jump to line 5'},
      {cmd: '/text',          what: 'Search downward',                       notes: 'n = next result  N = previous'},
      {                       what: 'Delete (cut) entire line',              notes: '3dd = delete 3 lines'},
      {                       what: 'Copy line / paste below',               notes: 'y = yank (copy)  p = paste below'},
      {                       what: 'Undo',                                  notes: 'Ctrl+R = redo'},
    ],
    steps: [
      {text: "Run: vimtutor\n\nvimtutor is an interactive tutorial built into Vim.\nIt creates a temporary file — you don't need to clean up when done.\nTime: approx. 30 minutes.\n\nMost important lessons from vimtutor:\n  :q!  — exit without saving\n  :wq  — save and exit\n  i    — enter insert mode\n  ESC  — return to normal mode"},
      {prompt: 'Have you completed vimtutor and know how to exit Vim (:wq and :q!)?'},
    ],
  },

  // ═══════════════════════════════════════════════════
  // WORLD 5
  // ═══════════════════════════════════════════════════
  '5.1': {
    world_flavor: "The Fortress has guardians and keys to every door. In Unix every resource has an owner and access rights. sudo is the key to the royal gates — it grants temporary administrator power. Use with caution.",
    title: 'sudo and users',
    boss_title: 'EXERCISE 5.1 — User Reconnaissance',
    boss_desc: 'The Fortress Captain checks if you understand the permissions system:',
    theory: [
      {                               what: 'Current username',                       notes: `Yours: ${USERNAME}`},
      {                               what: 'UID, GID and user groups',               notes: 'UID=0 is root (administrator)'},
      {                               what: 'What groups do I belong to?',            notes: "Member of 'admin' group = you can use sudo"},
      {cmd: 'sudo command',           what: 'Run command as root',                   notes: 'Superuser Do. Asks for your password'},
      {                               what: 'What commands can I run with sudo?',     notes: '-l = list'},
      {cmd: 'su - user',              what: 'Switch to another user',                notes: 'su = switch user. - = load their shell profile'},
      {                               what: 'Login history to system',               notes: 'When and from where users logged in'},
    ],
    steps: [
      {hint: `Prints UID of user ${USERNAME}, GID and all groups`},
      {hint: "Show what groups you belong to — look for 'admin' or 'wheel'"},
      {hint: 'Check what sudo permissions you have'},
    ],
  },

  '5.2': {
    world_flavor: "Nine letters that decide everything: rwxrwxrwx. r = read, w = write, x = execute. Three groups: owner, their group, everyone else. chmod changes these rights — chmod 755 is the classic permission for programs.",
    title: 'File permissions',
    boss_title: 'EXERCISE 5.2 — Permissions Guardian',
    boss_desc: 'The Fortress Guardian shows you a file and has you check and change its permissions:',
    theory: [
      {                               what: 'Show file permissions',                  notes: 'Format: -rwxr-xr-- = type|owner|group|others'},
      {cmd: 'chmod 755 file',         what: 'Set permissions numerically',           notes: 'r=4 w=2 x=1. 7=rwx 5=r-x 4=r--. 755 = owner everything, rest reads and executes'},
      {cmd: 'chmod 644 file',         what: 'Typical permissions for files',         notes: '644 = rw-r--r-- : owner read+write, rest read only'},
      {cmd: 'chmod +x file',          what: 'Add execute permission',               notes: '+x = for everyone  u+x = owner only'},
      {cmd: 'chmod u+w file',         what: 'Add write for owner',                  notes: 'u = user  g = group  o = others  a = all'},
      {                               what: 'Change owner and group',               notes: 'Requires sudo. chown user:group file'},
    ],
    steps: [
      {hint: 'create test file'},
      {hint: 'check permissions — default is rw-r--r-- (644)'},
      {hint: '+x = add execute permission for everyone'},
      {hint: '600 = rw------- : only you can read and write'},
      {hint: 'confirm permission change — should be rw-------'},
      {hint: 'clean up'},
    ],
  },

  '5.3': {
    world_flavor: "Every professional warrior personalizes their armor. Environment variables are your session configuration — PATH tells where to look for programs. Aliases are shortcuts to favorite commands, ~/.zshrc is your personal grimoire.",
    title: 'Variables and aliases',
    boss_title: 'BOSS FIGHT 5.3 — Shell Configuration',
    boss_desc: 'The Fortress Commander demands personalization — learn about your environment and configure it. Three lives:',
    theory: [
      {                               what: `Your home directory (${HOME})`,         notes: '$HOME, $USER, $PATH are system variables always available'},
      {                               what: 'Where system looks for programs',       notes: 'List of directories separated by :'},
      {                               what: `Your username (${USERNAME})`,           notes: '$USER = whoami but faster (without starting a process)'},
      {                               what: 'Set variable for this session',         notes: 'Without export = only in current shell'},
      {                               what: 'Reload config without restart',         notes: 'After adding alias to .zshrc you must source for it to take effect'},
      {                               what: 'Create shortcut for command',           notes: '-G = colors on macOS. Alias lives only in session — to make it permanent, add to ~/.zshrc'},
    ],
    steps: [
      {text: "Task: explore your environment and create a useful alias.\n\nPATH is the program search path.\nAn alias is a shortcut — ll='ls -laG' lets you type 'll' instead of 'ls -laG'.\nAliases only live for the session unless you save them to ~/.zshrc."},
      {hint: "Show PATH readably — tr ':' '\\n' replaces : with newlines"},
      {hint: 'Create temporary alias ll  -G = colors on macOS'},
      {prompt: "Do you want to save the alias permanently to ~/.zshrc? (echo \"alias ll='ls -laG'\" >> ~/.zshrc)"},
    ],
  },

  // ═══════════════════════════════════════════════════
  // WORLD 6
  // ═══════════════════════════════════════════════════
  '6.1': {
    world_flavor: "The Process Labyrinth is a city of never-sleeping daemons. Every running program is a daemon with a unique ID (PID). Today you don't fight — you observe. ps and top are your eyes in this chaos.",
    title: 'Observing processes',
    boss_title: 'EXERCISE 6.1 — Observer',
    boss_desc: 'The Labyrinth guide teaches you to observe without intervening:',
    theory: [
      {                               what: 'Processes of current terminal session',  notes: 'Without arguments — only your terminal processes'},
      {                               what: 'ALL system processes',                   notes: 'a = all users  u = readable format  x = processes without terminal'},
      {                               what: 'Processes of specific user',             notes: `Replace ${USERNAME} with any name`},
      {                               what: 'Live monitor — sort by CPU',             notes: 'q = quit  -o cpu/mem = sort column'},
      {                               what: 'System uptime + load',                  notes: 'load avg: averages over 1, 5 and 15 minutes'},
      {                               what: 'PID of current shell process',           notes: '$$ = special variable. $! = PID of last background process'},
    ],
    steps: [
      {hint: 'Check how long system has been running and average CPU load'},
      {hint: 'Count how many processes are running in the system'},
      {hint: `Find all processes of user ${USERNAME}`},
      {hint: 'Print PID of current shell'},
    ],
  },

  '6.2': {
    world_flavor: "Time to take things into your own hands. You'll start a daemon, find it, and eliminate it. & sends process to background, jobs shows the list, kill sends a signal. SIGTERM = polite termination request, SIGKILL (-9) = immediate annihilation.",
    title: 'Process management',
    boss_title: 'BOSS FIGHT 6.2 — Process Slayer',
    boss_desc: 'The Great Labyrinth Daemon demands proof of courage — start a daemon, find it, and eliminate it. Three lives:',
    theory: [
      {cmd: 'command &',      what: 'Run in background',                     notes: '& at end — shell immediately returns to prompt. Prints [job_number] PID'},
      {                       what: 'Suspend current process',               notes: "Stops (doesn't kill) — can resume with bg or fg"},
      {                       what: 'Resume in background / bring to foreground', notes: 'bg %1 = resume job 1 in background  fg %1 = bring to foreground'},
      {                       what: 'List background processes with PID',    notes: '-l = long (show PID). Job number (%1) different from PID'},
      {                       what: 'Polite request to terminate',           notes: 'Sends SIGTERM (15) — process can ignore'},
      {                       what: 'Immediate kill',                        notes: '-9 = SIGKILL. Cannot be ignored. Last resort'},
      {                       what: 'Kill first job from jobs list',         notes: "%1 = job number from 'jobs', not PID"},
      {                       what: 'What is using port 8080?',             notes: "When 'port is already in use'"},
    ],
    steps: [
      {text: "Difference between job number and PID:\n  jobs -l  shows: [1] 12345 Running   sleep 300\n           [1]   = job number (local id in this session)\n           12345 = PID (global process id in the system)\n\n  kill %1    kills by job number (faster)\n  kill 12345 kills by PID\n\nsleep 300 = sleep for 300 seconds — ideal test daemon."},
      {hint: '& = run in background. Shell immediately returns to prompt'},
      {hint: 'Show list of background processes with PID — -l adds PID column'},
      {hint: '%1 = first job from jobs list (more convenient than finding PID)'},
      {hint: "List should be empty or show '[1] Terminated'"},
    ],
  },

  // ═══════════════════════════════════════════════════
  // WORLD 7
  // ═══════════════════════════════════════════════════
  '7.1': {
    world_flavor: "In the Script Forge you'll learn how to make the shell think. Variables store data, substitutions insert command results inside strings, (( )) calculates like a calculator. These are the building blocks of automation.",
    title: 'Variables and substitutions',
    boss_title: 'EXERCISE 7.1 — Variables',
    boss_desc: 'The Smith tests your building blocks — practice variables and substitutions:',
    theory: [
      {cmd: "VAR='value'",              what: 'Assign value (no spaces around =!)',   notes: "WRONG: VAR = 'x'  RIGHT: VAR='x'"},
      {cmd: 'echo $VAR',               what: 'Read variable value',                  notes: '$ = reference'},
      {cmd: 'echo ${VAR:-default}',    what: 'Default value if empty',               notes: ':- = if empty or undefined, use value after :-'},
      {cmd: 'echo $(command)',          what: 'Insert command result (command subst.)', notes: 'e.g. echo "Today: $(date +%A)"'},
      {                                what: 'Arithmetic operations',                 notes: '(( )) = math context. Integers only'},
      {cmd: "read -p 'Name: ' NAME",   what: 'Get input from user',                  notes: '-p = prompt (display question before waiting)'},
      {cmd: 'unset VAR',               what: 'Remove variable',                      notes: 'After unset, echo $VAR = empty string'},
    ],
    steps: [
      {cmd: `NAME='${USERNAME}' && echo "Hello, \$NAME!"`,
       hint: 'Assign variable and print with substitution. && = run second only if first OK',
       output: `Hello, ${USERNAME}!`},
      {hint: 'Calculate 3 * 14 using shell arithmetic (( ))'},
      {cmd: 'echo "It is $(date +%H:%M) on ${HOSTNAME:-computer}"',
       hint: '$(date +%H:%M) = insert current time  ${HOSTNAME:-...} = variable or default',
       output: `It is 14:32 on ${HOSTNAME}`},
    ],
  },

  '7.2': {
    world_flavor: "Now you'll forge your first weapon. A script is a text file with commands and logic — written once, it runs a thousand times unattended. The shebang at the top tells the system how to read the file. chmod +x brings it to life.",
    title: 'First script',
    boss_title: 'BOSS FIGHT 7.2 — Script Smith',
    boss_desc: 'The Forge Master demands your first weapon be cast. Write a script, grant it rights, run it. Three lives:',
    theory: [
      {                               what: 'Shebang — first line of script',        notes: 'Tells system which interpreter to use. Must be in line 1'},
      {                               what: 'Variable',                              notes: 'No spaces around =! $NAME = read value'},
      {                               what: 'Print variable',                        notes: 'Double quotes interpret variables and $()'},
      {                               what: 'Script arguments',                      notes: '$0 = script name  $1 = first argument  $# = number of arguments'},
      {                               what: 'Check if file exists',                  notes: '-f = file  -d = directory  -z = empty string  -e = anything'},
      {                               what: 'For loop',                              notes: 'for i in $(seq 1 10) = loop 1-10. done = end of loop'},
      {                               what: 'Arithmetic operations',                 notes: 'count=$((count+1)) = increment variable'},
      {cmd: 'chmod +x script.sh',     what: 'Grant execute permission',             notes: 'Only once! Then run: ./script.sh'},
    ],
    steps: [
      {hint: 'create folder for script'},
      {text: `Write the script in nano: nano ${QP}/hello.sh\n\nType exactly this:\n#!/bin/bash\nNAME=\${1:-'Stranger'}\necho "Hello, \$NAME!"\necho "User: \$(whoami)"\necho "Host: \$(hostname)"\necho "Date: \$(date '+%Y-%m-%d')"\n\nSave: Ctrl+O + Enter, exit: Ctrl+X`},
      {hint: 'grant execute permission — without this shell will refuse to run'},
      {hint: "run without argument — you'll see 'Hello, Stranger!'",
       output: `Hello, Stranger!\nUser: ${USERNAME}\nHost: ${HOSTNAME}\nDate: 2026-04-06`},
      {hint: `run with argument — you'll see 'Hello, ${USERNAME}!'`,
       output: `Hello, ${USERNAME}!\nUser: ${USERNAME}\nHost: ${HOSTNAME}\nDate: 2026-04-06`},
      {hint: 'clean up'},
    ],
  },

  // ═══════════════════════════════════════════════════
  // WORLD 8
  // ═══════════════════════════════════════════════════
  '8.1': {
    world_flavor: "The Network Temple hides the secrets of connections between machines. Before you start attacking remote servers, master diagnostics: is there a connection? What IP? What latency? ping, ifconfig, host — tools of the scout.",
    title: 'Network diagnostics',
    boss_title: 'EXERCISE 8.1 — Diagnostics',
    boss_desc: 'The Temple Priest teaches you diagnostics before letting you go deeper. Check your network status:',
    theory: [
      {                               what: 'Check connection (3 packets)',           notes: '1.1.1.1 = Cloudflare DNS, always online. -c = count. time = latency in ms'},
      {                               what: 'Your computer name',                     notes: `Yours: ${HOSTNAME}`},
      {                               what: 'IP addresses of network interfaces',     notes: 'inet = IPv4  inet6 = IPv6  lo0 = localhost (127.0.0.1)'},
      {                               what: 'Fetch HTTP headers only',               notes: '-I = HEAD request: check status without downloading body'},
      {                               what: 'Routing table',                          notes: '-n = numeric  -r = routing'},
      {                               what: 'Convert domain to IP (DNS lookup)',      notes: 'host google.com = Google IP'},
    ],
    steps: [
      {hint: 'Send 3 packets to 1.1.1.1. -c 3 = stop after 3 packets'},
      {hint: `Check computer name — should be: ${HOSTNAME}`},
      {hint: "'inet ' with space = only IPv4, doesn't catch inet6"},
    ],
  },

  '8.2': {
    world_flavor: "curl is your hand reaching through the internet for data without a browser. SSH is an encrypted tunnel to a remote server — as if you were sitting directly in front of it. SSH keys replace passwords: an ed25519 key generated once authenticates you forever.",
    title: 'curl and SSH',
    boss_title: 'BOSS FIGHT 8.2 — Network Mage',
    boss_desc: 'The High Priest of the Temple demands proof of network mastery. Query services and check connection. Three lives:',
    theory: [
      {                               what: 'Show your public IP',                   notes: 'Queries external service that returns the IP of the incoming request'},
      {                               what: 'Fetch data without progress bar',       notes: '-s = silent. Ideal in scripts when you only want data'},
      {                               what: 'Download and save to file',             notes: '-o = output: provide filename. -O = use filename from URL'},
      {                               what: 'Internet speed test (macOS 12+)',       notes: 'Built-in macOS tool for measuring upload/download'},
      {                               what: 'Connect to SSH server',                 notes: 'Default port: 22'},
      {                               what: 'Connect on different port',             notes: '-p = port'},
      {                               what: 'Copy file to server',                   notes: 'scp = secure copy, same protocol as SSH'},
      {                               what: 'Generate SSH key',                      notes: 'ed25519 = modern algorithm. Generates a pair: private key + .pub'},
    ],
    steps: [
      {text: "curl is a terminal browser. Most important flags:\n  -s  = silent (no progress bar)\n  -I  = HEAD request (headers only)\n  -o  = save to file\n  -L  = follow redirects\n\ncurl returns page content or API — can be piped to grep, jq, head."},
      {hint: 'Show your public IP — -s = silent, no progress bar'},
      {hint: '-c 4 = send only 4 packets and stop automatically'},
      {hint: 'Fetch data from GitHub public API and show only 5 lines'},
    ],
  },

  // ═══════════════════════════════════════════════════
  // WORLD 9
  // ═══════════════════════════════════════════════════
  '9.1': {
    world_flavor: "The Git Abyss is a time matrix — every change is recorded, every commit is a point in history you can return to. git init builds this matrix from scratch. History begins with the first commit.",
    title: 'Git basics',
    boss_title: 'EXERCISE 9.1 — Git Basics',
    boss_desc: 'The Abyss Guardian leads you through the full Git cycle — init, add, commit:',
    theory: [
      {                               what: 'Create new repo (.git folder)',          notes: 'Creates hidden .git folder with entire history'},
      {                               what: 'What changed?',                          notes: 'Use often! Shows: untracked files, modified, staged'},
      {                               what: 'Add file to stage',                      notes: 'Stage = area prepared for commit'},
      {                               what: 'Add ALL changes to stage',              notes: '. = current directory and subdirectories'},
      {                               what: 'Save stage as commit',                   notes: "-m = short description. Good: 'fix: null pointer in auth'"},
      {                               what: 'Commit history',                         notes: '--oneline = 1 line per commit. --graph = ASCII tree'},
      {                               what: 'Changes NOT in stage',                  notes: '--staged = changes already in stage'},
    ],
    steps: [
      {hint: 'initialize git repo in quest-project folder — creates .git/'},
      {cmd: `echo 'Hello Git from ${HOSTNAME}' > ${QP}/plik.txt`,
       hint: 'create file with content'},
      {hint: "check status — file should be listed as 'untracked files'"},
      {hint: 'add file to stage'},
      {hint: 'save commit with message'},
      {hint: 'check history — should be one commit'},
      {hint: 'clean up'},
    ],
  },

  '9.2': {
    world_flavor: "A branch is a parallel world — you work on a feature without breaking main. When the feature is ready, merge joins the world back. Conflicts are clashes between versions — Git asks who is right.",
    title: 'Branches and merge',
    boss_title: 'BOSS FIGHT 9.2 — Branch Master',
    boss_desc: 'The Great Abyss Guardian demands you complete the full branch cycle. Create branch, commit, merge. Three lives:',
    theory: [
      {                               what: 'Show list of branches',                 notes: '* = current branch. -a = show remote ones too'},
      {                               what: 'Create new branch',                     notes: "Doesn't switch automatically"},
      {                               what: 'Switch to branch',                      notes: 'Modern alternative: git switch feature'},
      {                               what: 'Create and switch in one command',      notes: '-b = branch: shortcut for two commands'},
      {                               what: 'Merge branch with current',             notes: 'Being on main: git merge feature'},
      {                               what: 'Delete branch',                         notes: '-d = only if already merged  -D = force'},
    ],
    steps: [
      {text: "Branch workflow:\n  1. Create repo and make first commit on main\n  2. Create feature branch and switch to it\n  3. Make changes and commit on feature\n  4. Go back to main and merge feature\n\nWhy branches?\n  main must always work. Feature branch = you experiment\n  without risk. When ready — merge. If it fails — delete the branch."},
      {hint: 'create repo'},
      {hint: 'create first commit on main (three commands chained with &&)'},
      {hint: '-b = create and switch to new feature branch'},
      {hint: 'add change and commit on feature branch'},
      {hint: 'go back to main'},
      {hint: 'merge feature into main'},
      {hint: '--graph = ASCII branch tree'},
      {hint: 'clean up'},
    ],
  },

  // ═══════════════════════════════════════════════════
  // WORLD 10
  // ═══════════════════════════════════════════════════
  '10.1': {
    world_flavor: "You stand before the Throne. The final secrets are not difficult — they are elegant. Brace expansion, process substitution, find -exec — tools that reduce 10 lines to one. The Arcmaster never strikes more than necessary.",
    title: 'Advanced techniques',
    boss_title: 'FINAL BOSS — Terminal Arcmaster',
    boss_desc: "The Terminal Arcmaster himself rises from the Throne. 'Show me brace expansion and advanced techniques — or remain a novice forever.' Three lives for this ultimate challenge:",
    theory: [
      {                               what: 'Brace expansion: 4 directories at once',      notes: '{a,b} = list  {1..5} = sequence  Bash/zsh expand this BEFORE execution'},
      {cmd: 'touch file{1..10}.txt',  what: 'Create 10 files with one command',           notes: '{01..10} = with padding  {a..z} = alphabet'},
      {                               what: 'Insert command result',                        notes: '$() = command substitution'},
      {                               what: 'Compare outputs of two commands',             notes: '<() = process substitution: command output as temporary file'},
      {                               what: 'Find and delete files older than 30 days',    notes: '-exec = run for each  {} = placeholder for found file  \\; = end of -exec'},
      {                               what: 'Run in parallel and wait',                    notes: '& after each = run in background  wait = wait until all finish'},
      {                               what: 'Print first column with : as separator',      notes: '-F: = separator  $1 = first column  NR = row number'},
    ],
    steps: [
      {text: "Final test — brace expansion and find.\n\nBrace expansion is expanded BEFORE the command runs:\n  mkdir {a,b}/{x,y}  →  mkdir a/x a/y b/x b/y\n  touch file{1..3}   →  touch file1 file2 file3\n\nfind -exec: for each found file, run a command\n  find . -name '*.tmp' -exec rm {} \\;\n  {} = placeholder for the found file\n  \\; = end of -exec (semicolon must be preceded by \\ )"},
      {hint: 'creates 6 directories at once: src/v1, src/v2, tests/v1, tests/v2, docs/v1, docs/v2'},
      {hint: 'check full structure (-R = recursive)'},
      {hint: '{1..5} = sequence: creates file1.txt ... file5.txt at once'},
      {hint: 'count how many .txt files were created — should be 5'},
      {hint: 'clean up — one last time!'},
      {prompt: 'Congratulations Arcmaster! Have you completed Terminal Quest?'},
    ],
  },

  }; // end _EN

  // ── Apply translations ────────────────────────────────────────────────────────
  for (const q of QUESTS) {
    if (_EN[q.id]) _applyEN(q, _EN[q.id]);
    q.world_name = WORLD_NAMES[q.world];
  }

} // end if (LANG === 'en')
