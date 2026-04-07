// Terminal Quest — konfiguracja języka / language configuration
// Musi być załadowany przed quests.js / Must be loaded before quests.js

const LANG = localStorage.getItem('tq_lang') || 'pl';

// English world passwords (in addition to Polish ones)
const WORLD_PASSWORDS_EN = {
  1: 'village', 2: 'forest',    3: 'mines',    4: 'tower',
  5: 'fortress',6: 'labyrinth', 7: 'forge',    8: 'temple',
  9: 'abyss',  10: 'throne',
};

// UI string table
const UI = {
  // Welcome
  subtitle:       LANG==='en' ? 'RPG game teaching terminal skills'     : 'Gra RPG ucząca obsługi terminala',
  pressEnter:     LANG==='en' ? '[ Press Enter ]'                       : '[ Naciśnij Enter ]',
  namePrompt:     LANG==='en' ? 'What is your name, warrior?'           : 'Jak masz na imię, wojowniku?',
  nameLabel:      LANG==='en' ? 'name $'                                : 'imię $',
  returning:      LANG==='en' ? 'Welcome back,'                         : 'Witaj z powrotem,',
  // Theory table headers
  thCmd:          LANG==='en' ? 'Command'                               : 'Komenda',
  thWhat:         LANG==='en' ? 'What it does'                          : 'Co robi',
  thNotes:        LANG==='en' ? 'Notes'                                 : 'Uwagi',
  // Labels
  labelWorld:     LANG==='en' ? 'WORLD'                                 : 'ŚWIAT',
  labelTheory:    LANG==='en' ? '── THEORY ──'                          : '── TEORIA ──',
  labelBossTag:   LANG==='en' ? '[BOSS FIGHT]'                          : '[BOSS FIGHT]',
  labelInfo:      LANG==='en' ? 'INFO'                                  : 'INFO',
  labelHint:      LANG==='en' ? 'HINT'                                  : 'PODPOWIEDŹ',
  labelLevel:     LANG==='en' ? 'Level'                                 : 'Poziom',
  labelBossMenu:  LANG==='en' ? '[BOSS]'                                : '[BOSS]',
  // Step feedback
  correct:        LANG==='en' ? '✓ Correct!'                            : '✓ Poprawnie!',
  wrongExercise:  LANG==='en' ? '✗ Incorrect. Try again.'               : '✗ Niepoprawnie. Spróbuj jeszcze raz.',
  hintTip:        LANG==='en' ? '/hint = hint'                          : '/hint = podpowiedź',
  wrongBoss:      LANG==='en' ? '✗ Wrong!'                              : '✗ Błąd!',
  gameOver:       LANG==='en' ? '✗ GAME OVER — no lives left.'          : '✗ GAME OVER — brak żyć.',
  answerWas:      LANG==='en' ? 'Answer:'                               : 'Odpowiedź:',
  restartMsg:     LANG==='en' ? '/restart — restart boss fight    /menu — return to menu'
                              : '/restart — zacznij boss fight od nowa    /menu — wróć do menu',
  restartLabel:   LANG==='en' ? '⟳ RESTART'                            : '⟳ RESTART',
  noSkipBoss:     LANG==='en' ? 'Cannot skip a step in Boss Fight!'     : 'Nie można pominąć kroku w Boss Fight!',
  skippedCmd:     LANG==='en' ? 'Skipped. Command:'                     : 'Pominięto. Komenda:',
  // Prompts
  continuePrompt: LANG==='en' ? '[ Enter = next ]'                      : '[ Enter = dalej ]',
  answerPrompt:   LANG==='en' ? 'answer $'                              : 'odpowiedź $',
  confirmYesHint: LANG==='en' ? '[y / yes — confirm]'                   : '[t / y / tak / yes — potwierdź]',
  confirmBack:    LANG==='en' ? 'Come back when ready and type y.'      : 'Wróć gdy będziesz gotowy i wpisz t lub y.',
  confirmYes:     LANG==='en' ? ['y','yes']                             : ['t','y','tak','yes'],
  great:          LANG==='en' ? '✓ Great!'                              : '✓ Świetnie!',
  // Quest completion
  questDone:      LANG==='en' ? '★ QUEST COMPLETED'                     : '★ QUEST UKOŃCZONY',
  xpGained:       LANG==='en' ? 'XP gained!  Total:'                   : 'XP zdobyte!  Łącznie:',
  levelUp:        LANG==='en' ? '🎉 LEVEL UP TO'                        : '🎉 AWANS NA POZIOM',
  rankLabel:      LANG==='en' ? 'Rank:'                                 : 'Ranga:',
  worldDone:      LANG==='en' ? 'COMPLETED!  Unlocked:'                 : 'UKOŃCZONY!  Odblokowano:',
  worldLabel2:    LANG==='en' ? 'World'                                 : 'Świat',
  alreadyDone:    LANG==='en' ? 'Quest already completed. XP not added again.'
                              : 'Quest już ukończony. XP nie są dodawane ponownie.',
  enterMenu:      LANG==='en' ? '[ Enter = menu ]'                      : '[ Enter = menu ]',
  // World map
  mapTitle:       LANG==='en' ? '══ WORLD MAP ═══════════════════════════════════════════'
                              : '══ MAPA ŚWIATA ═══════════════════════════════════════════',
  mapLocked:      LANG==='en' ? '🔒 LOCKED'                             : '🔒 ZABLOKOWANY',
  mapCompleted:   LANG==='en' ? '✓ COMPLETED'                           : '✓ UKOŃCZONY',
  mapPasswords:   LANG==='en' ? 'Passwords: /pass village  /pass forest  /pass mines  etc.'
                              : 'Hasła: /pass wioska  /pass las  /pass kopalnia  itd.',
  // Menu
  menuCmds:       LANG==='en' ? '  /map  /help  /pass <password>  /reset  /lang'
                              : '  /map  /help  /pass <hasło>  /reset  /lang',
  menuUnavail:    LANG==='en' ? 'Quest unavailable. Complete the previous one or unlock the world with a password.'
                              : 'Quest niedostępny. Ukończ poprzedni lub odblokuj świat hasłem.',
  menuUnknown:    LANG==='en' ? 'Unknown quest:'                        : 'Nieznany quest:',
  // Password
  pwOk:           LANG==='en' ? 'unlocked!'                             : 'odblokowany!',
  pwBad:          LANG==='en' ? '✗ Unknown password.'                   : '✗ Nieznane hasło.',
  // Reset
  resetWarn:      LANG==='en'
    ? 'WARNING: this will delete all progress! Type <span class="bld">YES</span> to confirm.'
    : 'UWAGA: to usunie cały postęp! Wpisz <span class="bld">TAK</span> aby potwierdzić.',
  resetWord:      LANG==='en' ? 'yes'                                   : 'tak',
  resetCancelled: LANG==='en' ? 'Reset cancelled.'                      : 'Reset anulowany.',
  // Help
  helpTitle:      LANG==='en' ? 'HELP'                                  : 'POMOC',
  helpBody:       LANG==='en'
    ? `<span class="c">/hint</span>         — hint for current step<br>`+
      `<span class="c">/skip</span>         — skip step (exercises only)<br>`+
      `<span class="c">/map</span>          — world map<br>`+
      `<span class="c">/menu</span>         — return to menu<br>`+
      `<span class="c">/pass password</span> — unlock world<br>`+
      `<span class="c">/lang</span>         — switch language (PL↔EN)<br>`+
      `<span class="c">/reset</span>        — reset progress`
    : `<span class="c">/hint</span>        — podpowiedź dla bieżącego kroku<br>`+
      `<span class="c">/skip</span>        — pomiń krok (tylko ćwiczenia)<br>`+
      `<span class="c">/map</span>         — mapa świata<br>`+
      `<span class="c">/menu</span>        — wróć do menu<br>`+
      `<span class="c">/pass hasło</span>  — odblokuj świat<br>`+
      `<span class="c">/lang</span>        — przełącz język (PL↔EN)<br>`+
      `<span class="c">/reset</span>       — resetuj postęp`,
  // Language switch
  langSwitching:  LANG==='en' ? 'Switching to Polish…'     : 'Switching to English…',
  // Misc labels
  stepLabel:      LANG==='en' ? 'Step'                     : 'Krok',
  livesLabel:     LANG==='en' ? 'Lives:'                   : 'Życia:',
  questsDone:     LANG==='en' ? 'quests completed'         : 'questów ukończonych',
  labelQuests:    LANG==='en' ? 'quests'                   : 'questów',
  defaultName:    LANG==='en' ? 'hero'                     : 'gracz',
};
