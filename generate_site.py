from pathlib import Path
from html import escape
import json
import re

SKILLS_DIR = Path('./book-skills')
OUT_DIR = Path('/Users/dizhensmacair/Documents/Claude/Projects/temp-website-generation-20260717')
MAP_PATH = OUT_DIR / 'skill_book_map.json'


def load_skill_book_map() -> dict[str, str]:
    if MAP_PATH.exists():
        with MAP_PATH.open('r', encoding='utf-8') as fh:
            return json.load(fh)
    return {}


def get_display_name(folder_name: str, book_map: dict[str, str]) -> str:
    return book_map.get(folder_name, folder_name)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r'[^a-z0-9]+', '-', value)
    return value.strip('-')


def render_inline(text: str) -> str:
    text = escape(text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    return text


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    output = []
    i = 0

    def flush_list(list_buffer):
        if list_buffer:
            output.append('<ul>' + ''.join(f'<li>{item}</li>' for item in list_buffer) + '</ul>')
        return []

    def flush_quote(quote_buffer):
        if quote_buffer:
            output.append('<blockquote>' + ''.join(f'<p>{render_inline(item)}</p>' for item in quote_buffer) + '</blockquote>')
        return []

    while i < len(lines):
        line = lines[i].rstrip()

        if line.startswith('```'):
            code_buffer = []
            i += 1
            while i < len(lines) and not lines[i].rstrip().startswith('```'):
                code_buffer.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            output.append('<pre><code>' + escape('\n'.join(code_buffer)) + '</code></pre>')
            continue

        if '|' in line and i + 1 < len(lines):
            sep_line = lines[i + 1].strip()
            if re.match(r'^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?$', sep_line):
                table_lines = [line]
                j = i + 2
                while j < len(lines) and '|' in lines[j].strip():
                    table_lines.append(lines[j].rstrip())
                    j += 1

                rows = []
                for row in table_lines:
                    cells = [cell.strip() for cell in row.strip().strip('|').split('|')]
                    rows.append(cells)

                headers = rows[0]
                body_rows = rows[1:]
                html_rows = []
                html_rows.append('<thead><tr>' + ''.join(f'<th>{render_inline(cell)}</th>' for cell in headers) + '</tr></thead>')
                tbody_html = ''.join(
                    '<tr>' + ''.join(f'<td>{render_inline(cell)}</td>' for cell in row) + '</tr>'
                    for row in body_rows
                )
                output.append(f'<table><thead><tr>{"".join(f"<th>{render_inline(cell)}</th>" for cell in headers)}</tr></thead><tbody>{tbody_html}</tbody></table>')
                i = j
                continue

        if line.startswith('# '):
            output.append(f'<h2>{render_inline(line[2:])}</h2>')
        elif line.startswith('## '):
            output.append(f'<h3>{render_inline(line[3:])}</h3>')
        elif line.startswith('### '):
            output.append(f'<h4>{render_inline(line[4:])}</h4>')
        elif line.startswith('> '):
            quote_buffer = [line[2:]]
            i += 1
            while i < len(lines) and lines[i].startswith('> '):
                quote_buffer.append(lines[i][2:])
                i += 1
            output.append('<blockquote>' + ''.join(f'<p>{render_inline(item)}</p>' for item in quote_buffer) + '</blockquote>')
            continue
        elif line.startswith('- '):
            list_buffer = [render_inline(line[2:])]
            i += 1
            while i < len(lines) and lines[i].startswith('- '):
                list_buffer.append(render_inline(lines[i][2:]))
                i += 1
            output.append('<ul>' + ''.join(f'<li>{item}</li>' for item in list_buffer) + '</ul>')
            continue
        elif line.strip() == '':
            output.append('<div class="spacer"></div>')
        else:
            if line.strip():
                output.append(f'<p>{render_inline(line)}</p>')

        i += 1

    return ''.join(output)


book_map = load_skill_book_map()
allowed_files = {'cheatsheet.md', 'glossary.md', 'patterns.md'}
folders = sorted([p for p in SKILLS_DIR.iterdir() if p.is_dir() and p.name != 'book-to-skill'])
sections = []
for folder in folders:
    display_name = get_display_name(folder.name, book_map)
    files = sorted([
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in {'.md', '.markdown'} and p.name.lower() in allowed_files
    ])
    file_options = ''.join(
        f"<option value='{slugify(file.name)}' {'selected' if idx == 0 else ''}>{escape(file.name)}</option>"
        for idx, file in enumerate(files)
    )
    file_cards = []
    for file in files:
        markdown = file.read_text(encoding='utf-8', errors='ignore')
        file_cards.append(
            f"<article class='file-card' data-preview-file='{slugify(file.name)}' {'hidden' if file != files[0] else ''}>"
            f"<div class='file-card-header'><h3>{escape(file.name)}</h3></div>"
            f"<div class='markdown-body'>{markdown_to_html(markdown)}</div>"
            f"</article>"
        )
    sections.append(
        f"<section id='{slugify(folder.name)}' class='tab-panel' {'hidden' if folder != folders[0] else ''}>"
        f"<div class='panel-header'><h2>{escape(display_name)}</h2><span>{len(files)} markdown file(s)</span></div>"
        f"<div class='toolbar'><label for='select-{slugify(folder.name)}'>Choose markdown file</label><select id='select-{slugify(folder.name)}' class='file-select'>{file_options}</select></div>"
        + ''.join(file_cards)
        + '</section>'
    )

nav_items = ''.join(
    f"<button class='tab {'active' if idx == 0 else ''}' data-tab='{slugify(folder.name)}'>{escape(get_display_name(folder.name, book_map))}</button>"
    for idx, folder in enumerate(folders)
)

index_html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Skills Markdown Browser</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body data-theme="day">
  <div class="page">
    <header class="topbar">
      <div>
        <p class="eyebrow">Book Explorer</p>
        <h1>Summary and Insights</h1>
      </div>
      <div class="topbar-actions">
        <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Toggle theme">☀️</button>
      </div>
    </header>

    <nav class="tabs" aria-label="Skills folders">
      {nav_items}
    </nav>

    <main>
      {''.join(sections)}
    </main>
  </div>

  <script src="app.js"></script>
</body>
</html>
'''

styles_css = '''* { box-sizing: border-box; }
:root {
  --bg: #f6f8fa;
  --text: #24292f;
  --muted: #57606a;
  --panel: #ffffff;
  --border: #d0d7de;
  --subtle: #f6f8fa;
  --accent: #0969da;
  --code-bg: #0d1117;
  --code-text: #f6f8fa;
}
body[data-theme="night"] {
  --bg: #0d1117;
  --text: #e6edf3;
  --muted: #8b949e;
  --panel: #161b22;
  --border: #30363d;
  --subtle: #161b22;
  --accent: #58a6ff;
  --code-bg: #010409;
  --code-text: #e6edf3;
}
body {
  margin: 0;
  font-family: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg);
  color: var(--text);
}
.page {
  max-width: 1280px;
  margin: 0 auto;
  padding: 32px 20px 64px;
}
.topbar {
  display: flex;
  justify-content: space-between;
  align-items: end;
  gap: 16px;
  margin-bottom: 24px;
}
.topbar-actions {
  display: flex;
  align-items: center;
  gap: 14px;
}
.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 11px;
  color: var(--muted);
  margin: 0 0 8px;
}
h1,
h2,
h3,
h4 { margin: 0 0 12px; }
h1 { font-size: 2rem; }
h2 { font-size: 1.5rem; }
h3 { font-size: 1.2rem; }
.meta { color: var(--muted); font-size: 14px; }
.theme-toggle {
  border: 1px solid var(--border);
  background: var(--panel);
  color: var(--text);
  border-radius: 999px;
  width: 42px;
  height: 42px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 18px;
}
.tabs {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}
.tab {
  border: 1px solid var(--border);
  background: var(--panel);
  color: var(--text);
  padding: 10px 14px;
  border-radius: 999px;
  cursor: pointer;
  font-size: 14px;
}
.tab.active {
  background: var(--text);
  color: var(--bg);
  border-color: var(--text);
}
.tab-panel {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 22px;
}
.panel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 18px;
}
.panel-header span {
  color: var(--muted);
  font-size: 13px;
}
.toolbar {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 18px;
}
.toolbar label {
  font-weight: 600;
}
.file-select {
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 8px 10px;
  font-size: 14px;
  min-width: 260px;
  background: var(--panel);
  color: var(--text);
}
.file-card {
  border-top: 1px solid var(--border);
  padding: 18px 0;
}
.file-card:first-of-type { border-top: none; }
.file-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.markdown-body {
  line-height: 1.7;
  font-size: 15px;
  color: var(--text);
}
.markdown-body > :first-child { margin-top: 0; }
.markdown-body h2,
.markdown-body h3,
.markdown-body h4 {
  margin-top: 24px;
  margin-bottom: 12px;
  border-bottom: 1px solid var(--border);
  padding-bottom: 6px;
}
.markdown-body p,
.markdown-body li {
  margin: 0 0 10px;
}
.markdown-body ul,
.markdown-body ol {
  padding-left: 22px;
}
.markdown-body a {
  color: var(--accent);
  text-decoration: none;
}
.markdown-body a:hover { text-decoration: underline; }
.markdown-body blockquote {
  margin: 0 0 12px;
  padding: 10px 14px;
  border-left: 3px solid var(--border);
  background: var(--subtle);
}
.markdown-body pre {
  background: var(--code-bg);
  color: var(--code-text);
  padding: 14px;
  border-radius: 10px;
  overflow-x: auto;
  margin: 12px 0;
}
.markdown-body code {
  font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
  font-size: 0.93em;
  background: rgba(175, 184, 193, 0.2);
  padding: 0.15em 0.3em;
  border-radius: 6px;
}
.markdown-body pre code {
  background: transparent;
  padding: 0;
}
.markdown-body table {
  width: 100%;
  border-collapse: collapse;
  overflow: hidden;
  margin: 16px 0;
  border: 1px solid var(--border);
  border-radius: 8px;
}
.markdown-body th,
.markdown-body td {
  border: 1px solid var(--border);
  padding: 10px 12px;
  text-align: left;
  vertical-align: top;
}
.markdown-body th {
  background: var(--subtle);
}
.markdown-body strong { font-weight: 700; }
.markdown-body em { font-style: italic; }
.spacer { height: 8px; }
[hidden] { display: none; }
@media (max-width: 720px) {
  .topbar, .panel-header, .toolbar, .topbar-actions { flex-direction: column; align-items: flex-start; }
  .file-select { min-width: 100%; }
}
'''

app_js = '''const tabs = Array.from(document.querySelectorAll('.tab'));
const panels = Array.from(document.querySelectorAll('.tab-panel'));
const themeToggle = document.getElementById('theme-toggle');

const setTheme = (theme) => {
  document.body.dataset.theme = theme;
  themeToggle.textContent = theme === 'night' ? '☀️' : '🌙';
  localStorage.setItem('skills-theme', theme);
};

const savedTheme = localStorage.getItem('skills-theme') || 'day';
setTheme(savedTheme);

themeToggle.addEventListener('click', () => {
  const nextTheme = document.body.dataset.theme === 'night' ? 'day' : 'night';
  setTheme(nextTheme);
});

tabs.forEach((tab) => {
  tab.addEventListener('click', () => {
    const target = tab.dataset.tab;
    tabs.forEach((btn) => btn.classList.toggle('active', btn === tab));
    panels.forEach((panel) => {
      panel.hidden = panel.id !== target;
    });
  });
});

document.querySelectorAll('.file-select').forEach((select) => {
  const panel = select.closest('.tab-panel');
  const previews = Array.from(panel.querySelectorAll('.file-card'));

  select.addEventListener('change', () => {
    const value = select.value;
    previews.forEach((card) => {
      card.hidden = card.dataset.previewFile !== value;
    });
  });
});
'''

(OUT_DIR / 'index.html').write_text(index_html, encoding='utf-8')
(OUT_DIR / 'styles.css').write_text(styles_css, encoding='utf-8')
(OUT_DIR / 'app.js').write_text(app_js, encoding='utf-8')

print(f'Generated site for {len(folders)} folders and {sum(len([p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in {".md", ".markdown"}]) for folder in folders)} markdown files.')
