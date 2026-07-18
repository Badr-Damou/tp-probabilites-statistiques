const fs = require('fs');
const path = require('path');
const MarkdownIt = require('markdown-it');
const katex = require('katex');

const root = __dirname;
const sourcePath = path.join(root, 'rapport.md');
const outputDir = path.join(root, 'output', 'pdf');
const htmlPath = path.join(outputDir, 'rapport_evaluation_probabilites.html');

fs.mkdirSync(outputDir, { recursive: true });

let source = fs.readFileSync(sourcePath, 'utf8').replace(/^\uFEFF/, '');

function field(label, fallback = '') {
  const escaped = label.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const match = source.match(new RegExp(`\\*\\*${escaped} :\\*\\*\\s*(.+)`));
  if (!match) return fallback;
  const value = match[1].trim();
  return /^\.{3,}$/.test(value) ? fallback : value;
}

const student = field('Etudiant', 'Badr DAMOU');
const teacher = field('Enseignant', 'Hasan KARJOUN');
const year = field('Annee universitaire', '2025-2026');
const university = field('Universite', '');
const moduleName = field('Module', 'Probabilites et Statistiques');

// The PDF uses a designed cover instead of exposing the Markdown cover fields.
source = source.replace(/^# Rapport[^\n]*\n+[\s\S]*?^---\s*$/m, '');

const figures = {
  '`figures/probleme2_histogramme_binomiale.png`':
    '![Distribution simulee du nombre de reconnaissances correctes](../../figures/probleme2_histogramme_binomiale.png)',
  '`figures/probleme2_approximation_normale.png`':
    '![Comparaison de la loi binomiale et de son approximation normale](../../figures/probleme2_approximation_normale.png)',
  '`figures/probleme3_regression_lineaire.png`':
    '![Regression lineaire de la population mondiale et prediction pour 2050](../../figures/probleme3_regression_lineaire.png)',
  '`figures/probleme4_histogramme_abeilles.png`':
    '![Distribution des longueurs des abeilles](../../figures/probleme4_histogramme_abeilles.png)',
};
for (const [marker, image] of Object.entries(figures)) source = source.split(marker).join(image);

const md = new MarkdownIt({ html: false, linkify: true, typographer: false });

md.inline.ruler.before('escape', 'inline_math', (state, silent) => {
  if (state.src[state.pos] !== '$' || state.src[state.pos + 1] === '$') return false;
  const end = state.src.indexOf('$', state.pos + 1);
  if (end < 0) return false;
  if (!silent) {
    const token = state.push('inline_math', 'math', 0);
    token.content = state.src.slice(state.pos + 1, end);
  }
  state.pos = end + 1;
  return true;
});
md.renderer.rules.inline_math = (tokens, idx) => {
  try { return katex.renderToString(tokens[idx].content, { throwOnError: false }); }
  catch { return `<code>${md.utils.escapeHtml(tokens[idx].content)}</code>`; }
};

md.block.ruler.before('fence', 'display_math', (state, startLine, endLine, silent) => {
  const start = state.bMarks[startLine] + state.tShift[startLine];
  const line = state.src.slice(start, state.eMarks[startLine]).trim();
  if (line !== '\\[') return false;
  let next = startLine + 1;
  while (next < endLine) {
    const pos = state.bMarks[next] + state.tShift[next];
    if (state.src.slice(pos, state.eMarks[next]).trim() === '\\]') break;
    next++;
  }
  if (next >= endLine) return false;
  if (!silent) {
    const token = state.push('display_math', 'math', 0);
    token.block = true;
    token.content = state.getLines(startLine + 1, next, 0, false).trim();
    token.map = [startLine, next + 1];
  }
  state.line = next + 1;
  return true;
});
md.renderer.rules.display_math = (tokens, idx) => {
  try { return katex.renderToString(tokens[idx].content, { displayMode: true, throwOnError: false }); }
  catch { return `<pre>${md.utils.escapeHtml(tokens[idx].content)}</pre>`; }
};

const body = md.render(source);
const universityLine = university ? `<p class="university">${university}</p>` : '';

const html = `<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><title>Evaluation - ${student}</title>
<style>${fs.readFileSync(require.resolve('katex/dist/katex.min.css'), 'utf8')}
@page { size: A4; margin: 17mm 17mm 18mm; }
* { box-sizing: border-box; }
html { font-family: "Aptos", "Segoe UI", Arial, sans-serif; color: #172033; font-size: 10.5pt; line-height: 1.52; }
body { margin: 0; }
.cover { height: 260mm; display: flex; flex-direction: column; justify-content: space-between; page-break-after: always; padding: 17mm 9mm 12mm; border-top: 8px solid #1f4e79; }
.cover-top { color: #405269; text-transform: uppercase; letter-spacing: .08em; font-size: 10pt; }
.cover-top p { margin: 4px 0; }
.cover-main { border-left: 5px solid #2f75b5; padding: 10mm 0 10mm 11mm; }
.cover h1 { margin: 0 0 8mm; font-size: 30pt; line-height: 1.1; color: #17365d; }
.cover .subtitle { margin: 0; font-size: 16pt; line-height: 1.4; color: #385d7a; }
.identity { width: 100%; border-collapse: collapse; font-size: 12pt; }
.identity td { padding: 4mm 2mm; border-bottom: 1px solid #c8d4df; }
.identity td:first-child { width: 38%; color: #536b80; font-weight: 600; }
h2 { color: #17365d; font-size: 20pt; border-bottom: 2px solid #5b9bd5; padding-bottom: 3mm; margin: 12mm 0 5mm; page-break-after: avoid; }
h2:not(:first-child) { page-break-before: always; }
h3 { color: #1f4e79; font-size: 14pt; margin: 8mm 0 3mm; page-break-after: avoid; }
h4 { color: #385d7a; font-size: 11.5pt; margin: 6mm 0 2mm; page-break-after: avoid; }
p { margin: 0 0 3.5mm; text-align: justify; orphans: 3; widows: 3; }
ul, ol { margin: 2mm 0 4mm 6mm; padding-left: 5mm; }
li { margin: 1mm 0; }
table { width: 100%; border-collapse: collapse; margin: 5mm 0 6mm; font-size: 9.3pt; page-break-inside: avoid; }
thead { display: table-header-group; }
th { background: #1f4e79; color: white; text-align: left; padding: 2.4mm; }
td { padding: 2.2mm 2.4mm; border-bottom: 1px solid #d8e1e8; }
tbody tr:nth-child(even) { background: #f2f6f9; }
th:not(:first-child), td:not(:first-child) { text-align: right; }
.katex-display { margin: 4mm 0; padding: 2.5mm; background: #f6f8fb; border-left: 3px solid #5b9bd5; overflow: hidden; page-break-inside: avoid; }
.katex { font-size: 1.03em; }
figure { margin: 6mm auto; page-break-inside: avoid; text-align: center; }
img { display: block; max-width: 92%; max-height: 125mm; margin: 5mm auto 2mm; object-fit: contain; }
p:has(> img) { text-align: center; color: #536b80; font-size: 9pt; font-style: italic; page-break-inside: avoid; }
code { color: #8a2d3c; background: #f5f1f2; padding: .2mm 1mm; border-radius: 2px; }
hr { border: 0; border-top: 1px solid #becbd6; margin: 9mm 0; }
strong { color: #17365d; }
</style></head><body>
<section class="cover">
  <div class="cover-top">${universityLine}<p>${moduleName}</p><p>Année universitaire ${year}</p></div>
  <div class="cover-main"><h1>Rapport d'évaluation</h1><p class="subtitle">Probabilités, lois usuelles,<br>régression linéaire et estimation</p></div>
  <table class="identity"><tr><td>Étudiant</td><td>${student}</td></tr><tr><td>Enseignant</td><td>${teacher}</td></tr><tr><td>Module</td><td>${moduleName}</td></tr><tr><td>Année universitaire</td><td>${year}</td></tr></table>
</section>
<main>${body}</main>
</body></html>`;

fs.writeFileSync(htmlPath, html, 'utf8');
console.log(htmlPath);
