// Terminal Quest — browser game engine

// ── DOM refs ──────────────────────────────────────────────────────────────────
const outputEl  = document.getElementById('output');
const promptEl  = document.getElementById('prompt');
const inputEl   = document.getElementById('cmd-input');

// ── State ─────────────────────────────────────────────────────────────────────
const G = {
  questIdx:        0,
  stepIdx:         0,
  lives:           3,
  xp:              0,
  completedQuests: [],   // quest ids
  unlockedWorlds:  [0],
  inputHandler:    null,
};

// ── Persistence ───────────────────────────────────────────────────────────────
function saveGame() {
  localStorage.setItem('tq_save', JSON.stringify({
    xp:              G.xp,
    completedQuests: G.completedQuests,
    unlockedWorlds:  G.unlockedWorlds,
  }));
}

function loadGame() {
  const raw = localStorage.getItem('tq_save');
  if (!raw) return;
  try {
    const d = JSON.parse(raw);
    G.xp              = d.xp              || 0;
    G.completedQuests = d.completedQuests  || [];
    G.unlockedWorlds  = d.unlockedWorlds   || [0];
  } catch (_) {}
}

// ── XP / Rank ─────────────────────────────────────────────────────────────────
function getLevel() { return Math.floor(G.xp / XP_PER_LEVEL) + 1; }

function getRank() {
  const lv = getLevel();
  for (const [thr, name, title] of RANKS) {
    if (lv <= thr) return { name, title };
  }
  const last = RANKS[RANKS.length - 1];
  return { name: last[1], title: last[2] };
}

// ── UI helpers ────────────────────────────────────────────────────────────────
function esc(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function line(html) {
  const d = document.createElement('div');
  d.innerHTML = html;
  outputEl.appendChild(d);
  outputEl.scrollTop = outputEl.scrollHeight;
}

function blank() { line('&nbsp;'); }

function sep() {
  line('<span class="sep">────────────────────────────────────────────────────────</span>');
}

function pre(text) {
  return `<pre class="cmd-out" style="margin:0;font-family:inherit">${esc(text)}</pre>`;
}

function panel(color, title, bodyHtml) {
  return `<div class="panel p-${color}" style="margin:4px 0">` +
         `<div class="panel-hd">${title}</div>` +
         `<div class="panel-bd">${bodyHtml}</div></div>`;
}

function theoryTable(rows) {
  const trs = rows.map(r =>
    `<tr><td class="tc">${esc(r.cmd)}</td>` +
    `<td class="tw">${esc(r.what)}</td>` +
    `<td class="tn">${esc(r.notes)}</td></tr>`
  ).join('');
  return `<table class="tbl"><thead><tr>` +
    `<th>${UI.thCmd}</th><th>${UI.thWhat}</th><th>${UI.thNotes}</th>` +
    `</tr></thead><tbody>${trs}</tbody></table>`;
}

function statsBar() {
  const rank = getRank();
  return `<span class="g bld">${esc(USERNAME)}</span>` +
    `  <span class="d">│</span>  <span class="c">${UI.labelLevel} ${getLevel()}</span>` +
    `  <span class="d">│</span>  <span class="y">${G.xp} XP</span>` +
    `  <span class="d">│</span>  <span class="m">${esc(rank.name)}</span>`;
}

function setPrompt(html) { promptEl.innerHTML = html; }

function shellPrompt() {
  setPrompt(`<span class="g">${esc(USERNAME)}@terminal-quest</span><span class="d">:~$</span>&nbsp;`);
}

function livesHtml() {
  return '❤️ '.repeat(G.lives).trim() + ' ' + '🖤'.repeat(3 - G.lives);
}

// ── Normalize ─────────────────────────────────────────────────────────────────
function normalizeCmd(cmd) {
  return cmd.trim()
    .replace(/\s+/g, ' ')
    .split(' ')
    .map(tok => /^-[a-zA-Z]{2,}$/.test(tok)
      ? '-' + tok.slice(1).split('').sort().join('')
      : tok)
    .join(' ');
}

function cmdMatches(userInput, expected) {
  return normalizeCmd(userInput) === normalizeCmd(expected);
}

function normalizeQuiz(ans) {
  return ans.trim().toLowerCase()
    .replace(/\s+/g, '')
    .replace(/[–−]/g, '+');
}

// ── World / Quest availability ────────────────────────────────────────────────
function isWorldUnlocked(w) {
  if (w === 0) return true;
  if (G.unlockedWorlds.includes(w)) return true;
  return QUESTS.filter(q => q.world === w - 1)
               .every(q => G.completedQuests.includes(q.id));
}

function isQuestAvailable(quest) {
  if (!isWorldUnlocked(quest.world)) return false;
  const wq = QUESTS.filter(q => q.world === quest.world);
  const idx = wq.findIndex(q => q.id === quest.id);
  return idx === 0 || G.completedQuests.includes(wq[idx - 1].id);
}

function applyPassword(pw) {
  const entry = Object.entries(WORLD_PASSWORDS)
    .find(([, p]) => p === pw.trim().toLowerCase());
  if (!entry) return null;
  const w = parseInt(entry[0]);
  if (!G.unlockedWorlds.includes(w)) { G.unlockedWorlds.push(w); saveGame(); }
  return w;
}

// ── Language switch ───────────────────────────────────────────────────────────
function switchLang() {
  line(`<span class="y">${UI.langSwitching}</span>`);
  localStorage.setItem('tq_lang', LANG === 'en' ? 'pl' : 'en');
  setTimeout(() => window.location.reload(), 800);
}

// ── Input pipeline ────────────────────────────────────────────────────────────
inputEl.addEventListener('keydown', e => {
  if (e.key !== 'Enter') return;
  const val = inputEl.value;
  inputEl.value = '';
  dispatchInput(val);
});

function dispatchInput(val) {
  // Echo
  const promptTxt = promptEl.textContent.replace(/\u00a0/g, ' ');
  line(`<span class="echo-in">${esc(promptTxt)}</span><span class="c">${esc(val)}</span>`);

  // Global overrides
  if (val === '/map')   { showWorldMap(); return; }
  if (val === '/help')  { showHelp(); return; }
  if (val === '/menu')  { showMenu(); return; }
  if (val === '/lang')  { switchLang(); return; }
  if (val === '/reset') { confirmReset(); return; }
  if (val.startsWith('/pass ')) {
    const w = applyPassword(val.slice(6));
    if (w !== null) line(`<span class="g">✓ ${UI.labelWorld} ${w} (${esc(WORLD_NAMES[w])}) ${UI.pwOk}</span>`);
    else            line(`<span class="r">${UI.pwBad}</span>`);
    return;
  }

  if (G.inputHandler) G.inputHandler(val);
}

// ── Welcome ───────────────────────────────────────────────────────────────────
function showWelcome() {
  outputEl.innerHTML = '';
  line(`<span class="g bld">  ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     </span>`);
  line(`<span class="c bld">     ██║   ██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     </span>`);
  line(`<span class="g bld">     ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     </span>`);
  line(`<span class="c bld">     ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     </span>`);
  line(`<span class="g bld">     ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗</span>`);
  line(`<span class="c bld">     ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝</span>`);
  line(`<span class="y bld">                    Q U E S T  — ${UI.subtitle}</span>`);
  sep();
  blank();

  const savedName = localStorage.getItem('tq_username');
  if (savedName) {
    loadGame();
    line(`${UI.returning} <span class="g bld">${esc(savedName)}</span>!`);
    line(`<span class="d">${UI.labelLevel} ${getLevel()}  |  ${G.xp} XP  |  ${G.completedQuests.length} ${UI.questsDone}</span>`);
    blank();
    setPrompt(`<span class="g">${UI.pressEnter}</span> `);
    G.inputHandler = () => showMenu();
  } else {
    line(UI.namePrompt);
    blank();
    setPrompt(`<span class="g">${UI.nameLabel}</span> `);
    G.inputHandler = val => {
      const name = val.trim() || UI.defaultName;
      localStorage.setItem('tq_username', name);
      window.location.reload();
    };
  }
}

// ── Main Menu ─────────────────────────────────────────────────────────────────
function showMenu() {
  outputEl.innerHTML = '';
  line(statsBar());
  sep();
  blank();

  const worlds = {};
  for (const q of QUESTS) {
    if (!worlds[q.world]) worlds[q.world] = [];
    worlds[q.world].push(q);
  }

  for (const w of Object.keys(worlds).map(Number).sort((a, b) => a - b)) {
    const unlocked = isWorldUnlocked(w);
    const wColor   = unlocked ? 'c' : 'd';
    line(`<span class="${wColor} bld">${UI.labelWorld} ${w}: ${esc(WORLD_NAMES[w])}${unlocked ? '' : '  🔒'}</span>`);

    for (const q of worlds[w]) {
      const done  = G.completedQuests.includes(q.id);
      const avail = isQuestAvailable(q);
      const boss  = q.is_boss ? ` <span class="r">${UI.labelBossMenu}</span>` : '';
      const xpTag = ` <span class="y">[+${q.xp} XP]</span>`;

      if (done)        line(`  <span class="g">✓</span> <span class="d">${q.id} — ${esc(q.title)}</span>`);
      else if (avail)  line(`  <span class="y">▶</span> <span class="c bld">${q.id}</span> — ${esc(q.title)}${boss}${xpTag}`);
      else             line(`  <span class="d">  ${q.id} — ${esc(q.title)}</span>`);
    }
    blank();
  }

  line(`<span class="d">${UI.menuCmds}</span>`);
  sep();
  shellPrompt();

  G.inputHandler = val => {
    val = val.trim();
    if (!val) return;
    const quest = QUESTS.find(q => q.id === val);
    if (!quest) { line(`<span class="r">${UI.menuUnknown} ${esc(val)}</span>`); return; }
    if (!isQuestAvailable(quest)) {
      line(`<span class="r">${UI.menuUnavail}</span>`);
      return;
    }
    startQuest(QUESTS.indexOf(quest));
  };
}

// ── World map ─────────────────────────────────────────────────────────────────
function showWorldMap() {
  outputEl.innerHTML = '';
  line(`<span class="c bld">${UI.mapTitle}</span>`);
  blank();
  for (let w = 0; w <= 10; w++) {
    const unlocked = isWorldUnlocked(w);
    const wq       = QUESTS.filter(q => q.world === w);
    const done     = wq.filter(q => G.completedQuests.includes(q.id)).length;
    const total    = wq.length;
    let   status, col;
    if (!unlocked)          { status = UI.mapLocked;                                    col = 'd'; }
    else if (done === total){ status = `${UI.mapCompleted} (${done}/${total})`;         col = 'g'; }
    else                    { status = `▶ ${done}/${total} ${UI.labelQuests}`;          col = 'y'; }
    line(`  <span class="${col}">${UI.worldLabel2} ${w}: ${esc(WORLD_NAMES[w])}</span>  <span class="d">${status}</span>`);
  }
  blank();
  line(`<span class="d">${UI.mapPasswords}</span>`);
  sep();
  setPrompt(`<span class="g">${UI.enterMenu}</span> `);
  G.inputHandler = () => showMenu();
}

// ── Help ──────────────────────────────────────────────────────────────────────
function showHelp() {
  line(panel('blue', UI.helpTitle, UI.helpBody));
}

// ── Reset ─────────────────────────────────────────────────────────────────────
function confirmReset() {
  line(`<span class="r">${UI.resetWarn}</span>`);
  const prev = G.inputHandler;
  G.inputHandler = val => {
    if (val.trim().toLowerCase() === UI.resetWord) {
      localStorage.removeItem('tq_save');
      localStorage.removeItem('tq_username');
      window.location.reload();
    } else {
      line(`<span class="d">${UI.resetCancelled}</span>`);
      G.inputHandler = prev;
    }
  };
}

// ── Quest ─────────────────────────────────────────────────────────────────────
function startQuest(idx) {
  G.questIdx = idx;
  G.stepIdx  = 0;
  G.lives    = 3;

  const q = QUESTS[idx];
  outputEl.innerHTML = '';

  // Header
  sep();
  line(`<span class="c bld">${UI.labelWorld} ${q.world}: ${esc(q.world_name)}</span>`);
  line(`<span class="bld">Quest ${q.id} — ${esc(q.title)}</span>` +
       `  <span class="y">+${q.xp} XP</span>` +
       (q.is_boss ? `  <span class="r bld">${UI.labelBossTag}</span>` : ''));
  sep();
  blank();

  // Flavor
  line(`<span class="d ita">${esc(q.world_flavor)}</span>`);
  blank();

  // Theory
  line(`<span class="c bld">${UI.labelTheory}──────────────────────────────────────────</span>`);
  blank();
  const tbl = document.createElement('div');
  tbl.innerHTML = theoryTable(q.theory);
  outputEl.appendChild(tbl);
  blank();

  // Boss panel
  const bColor = q.is_boss ? 'red' : 'cyan';
  const bossDiv = document.createElement('div');
  bossDiv.innerHTML = panel(bColor, q.boss.title,
    `<span class="d">${esc(q.boss.description)}</span>`);
  outputEl.appendChild(bossDiv);
  blank();

  if (q.is_boss) {
    line(`<span>${UI.livesLabel} ${livesHtml()}</span>`);
    blank();
  }

  runNextStep();
}

// ── Step runner ───────────────────────────────────────────────────────────────
function runNextStep() {
  const q     = QUESTS[G.questIdx];
  const steps = q.boss.steps;
  if (G.stepIdx >= steps.length) { finishQuest(); return; }

  const step  = steps[G.stepIdx];
  const total = steps.length;
  line(`<span class="d">[${UI.stepLabel} ${G.stepIdx + 1}/${total}]</span>`);

  switch (step.type) {
    case 'info':    runInfo(step);               break;
    case 'confirm': runConfirm(step);            break;
    case 'shell':   runShell(step, q.is_boss);   break;
    case 'quiz':    runQuiz(step, q.is_boss);    break;
  }
}

// ── Info ──────────────────────────────────────────────────────────────────────
function runInfo(step) {
  const d = document.createElement('div');
  d.innerHTML = panel('blue', UI.labelInfo,
    `<pre style="margin:0;white-space:pre-wrap;font-family:inherit">${esc(step.text)}</pre>`);
  outputEl.appendChild(d);
  setPrompt(`<span class="d">${UI.continuePrompt}</span> `);
  G.inputHandler = () => { G.stepIdx++; runNextStep(); };
}

// ── Confirm ───────────────────────────────────────────────────────────────────
function runConfirm(step) {
  line(`<span class="y">❓ ${esc(step.prompt)}</span>`);
  line(`<span class="d">  ${UI.confirmYesHint}</span>`);
  shellPrompt();
  G.inputHandler = val => {
    const v = val.trim().toLowerCase();
    if (UI.confirmYes.includes(v)) {
      line(`<span class="g">${UI.great}</span>`);
      G.stepIdx++;
      setTimeout(runNextStep, 400);
    } else {
      line(`<span class="y">${UI.confirmBack}</span>`);
    }
  };
}

// ── Shell step ────────────────────────────────────────────────────────────────
function runShell(step, isBoss) {
  shellPrompt();
  G.inputHandler = val => {
    if (val === '/hint') {
      const d = document.createElement('div');
      d.innerHTML = panel('yellow', UI.labelHint, esc(step.hint || step.cmd));
      outputEl.appendChild(d);
      return;
    }
    if (val === '/skip') {
      if (isBoss) {
        line(`<span class="r">${UI.noSkipBoss}</span>`);
      } else {
        line(`<span class="y">${UI.skippedCmd} <span class="c">${esc(step.cmd)}</span></span>`);
        if (step.output) {
          const d = document.createElement('div');
          d.innerHTML = pre(step.output);
          outputEl.appendChild(d);
        }
        G.stepIdx++;
        setTimeout(runNextStep, 300);
      }
      return;
    }

    if (cmdMatches(val, step.cmd)) {
      if (step.output) {
        const d = document.createElement('div');
        d.innerHTML = pre(step.output);
        outputEl.appendChild(d);
      }
      line(`<span class="g">${UI.correct}</span>`);
      G.stepIdx++;
      setTimeout(runNextStep, 400);
    } else {
      handleWrong(isBoss, step.cmd);
    }
  };
}

// ── Quiz step ─────────────────────────────────────────────────────────────────
function runQuiz(step, isBoss) {
  line(`<span class="y bld">❓ ${esc(step.question)}</span>`);
  setPrompt(`<span class="m">${UI.answerPrompt}</span> `);
  G.inputHandler = val => {
    if (val === '/hint') {
      const d = document.createElement('div');
      d.innerHTML = panel('yellow', UI.labelHint, esc(step.hint));
      outputEl.appendChild(d);
      return;
    }
    const norm    = normalizeQuiz(val);
    const correct = step.answers.some(a => normalizeQuiz(a) === norm);
    if (correct) {
      line(`<span class="g">${UI.correct}</span>  <span class="d">(${esc(step.answers[0])})</span>`);
      G.stepIdx++;
      setTimeout(runNextStep, 400);
    } else {
      handleWrong(isBoss, step.answers[0]);
    }
  };
}

// ── Wrong answer ──────────────────────────────────────────────────────────────
function handleWrong(isBoss, correctAns) {
  if (!isBoss) {
    line(`<span class="r">${UI.wrongExercise}  <span class="d">(${UI.hintTip})</span></span>`);
    return;
  }
  G.lives--;
  if (G.lives > 0) {
    line(`<span class="r">${UI.wrongBoss}</span>  ` + livesHtml());
  } else {
    line(`<span class="r bld">${UI.gameOver}</span>`);
    line(`<span class="d">${UI.answerWas} <span class="c">${esc(correctAns)}</span></span>`);
    blank();
    line(`<span class="y">${UI.restartMsg}</span>`);
    setPrompt('<span class="g">$</span> ');
    G.inputHandler = val => {
      if (val.trim() === '/restart') restartBoss();
      // /menu handled globally
    };
  }
}

// ── Boss restart ──────────────────────────────────────────────────────────────
function restartBoss() {
  G.stepIdx = 0;
  G.lives   = 3;
  const q = QUESTS[G.questIdx];
  outputEl.innerHTML = '';
  line(`<span class="r bld">${UI.restartLabel}: ${esc(q.boss.title)}</span>`);
  blank();
  line(`<span>${UI.livesLabel} ${livesHtml()}</span>`);
  blank();
  runNextStep();
}

// ── Finish quest ──────────────────────────────────────────────────────────────
function finishQuest() {
  const q    = QUESTS[G.questIdx];
  const new_ = !G.completedQuests.includes(q.id);

  blank();
  sep();
  if (new_) {
    const oldLv = getLevel();
    G.completedQuests.push(q.id);
    G.xp += q.xp;
    saveGame();
    const newLv = getLevel();

    line(`<span class="g bld">${UI.questDone}: ${esc(q.title)}</span>`);
    line(`<span class="y">+${q.xp} ${UI.xpGained} ${G.xp} XP</span>`);

    if (newLv > oldLv) {
      blank();
      line(`<span class="m bld">${UI.levelUp} ${newLv}!  ${UI.rankLabel} ${esc(getRank().name)}</span>`);
    }

    // World complete?
    const wq = QUESTS.filter(q2 => q2.world === q.world);
    if (wq.every(q2 => G.completedQuests.includes(q2.id))) {
      const next = q.world + 1;
      if (WORLD_NAMES[next]) {
        blank();
        line(`<span class="c bld">✨ ${UI.labelWorld} ${q.world} ${UI.worldDone} ${UI.worldLabel2} ${next} — ${esc(WORLD_NAMES[next])}</span>`);
      }
    }
  } else {
    line(`<span class="g">${UI.alreadyDone}</span>`);
  }

  sep();
  blank();
  setPrompt(`<span class="g">${UI.enterMenu}</span> `);
  G.inputHandler = () => showMenu();
}

// ── Boot ──────────────────────────────────────────────────────────────────────
loadGame();
showWelcome();
inputEl.focus();
