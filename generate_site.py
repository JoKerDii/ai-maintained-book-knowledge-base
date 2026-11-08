"""Generate the static Book Explorer site.

The site has two top-level tabs:
  * "Summary and Insights" - cheatsheet/glossary/patterns from ./book-skills
  * "Guided Reading"       - quiz / arguments-and-evidence from ./reading-helper

Inside each tab there is one sub-tab per book and a dropdown per file.
Run via ./refresh_site.sh (or `python3 generate_site.py`).
"""

from __future__ import annotations

from pathlib import Path
from html import escape
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
SKILLS_DIR = ROOT / 'book-skills'
READING_HELPER_DIR = ROOT / 'reading-helper'
OUT_DIR = ROOT
MAP_PATH = ROOT / 'skill_book_map.json'

# Files shown in the "Summary and Insights" tab, in display order.
SKILL_FILES = ['cheatsheet.md', 'glossary.md', 'patterns.md']

# Reading-helper document types, in display order: file suffix -> label.
READING_HELPER_DOCS = [
    ('quiz', 'Quiz'),
    ('arguments-and-evidence', 'Arguments & Evidence'),
]


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #

def load_skill_book_map() -> dict[str, str]:
    if MAP_PATH.exists():
        return json.loads(MAP_PATH.read_text(encoding='utf-8'))
    return {}


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r'[^a-z0-9]+', '-', value)
    return value.strip('-')


def prettify_key(key: str) -> str:
    return key.replace('-', ' ').strip().title()


def title_from_skill_md(folder: Path) -> str | None:
    """First level-1 heading of SKILL.md, which is the book title."""
    skill_md = folder / 'SKILL.md'
    if not skill_md.exists():
        return None
    for line in skill_md.read_text(encoding='utf-8', errors='ignore').splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    return None


def title_from_reading_helper(path: Path) -> str | None:
    """Reading-helper files open with `# <Short> Quiz Book` then `*Full Title* by Author`."""
    lines = path.read_text(encoding='utf-8', errors='ignore').splitlines()[:6]
    for line in lines:
        match = re.match(r'^\*([^*]+)\*\s+by\s+', line.strip())
        if match:
            return match.group(1).strip()
    for line in lines:
        if line.startswith('# '):
            return re.sub(r'\s+(Quiz Book|Quiz)$', '', line[2:].strip())
    return None


# --------------------------------------------------------------------------- #
# markdown
# --------------------------------------------------------------------------- #

def render_inline(text: str) -> str:
    text = escape(text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    return text


HEADINGS = [('#### ', 'h5'), ('### ', 'h4'), ('## ', 'h3'), ('# ', 'h2')]


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    output: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        # fenced code block
        if stripped.startswith('```'):
            code_buffer = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_buffer.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            output.append('<pre><code>' + escape('\n'.join(code_buffer)) + '</code></pre>')
            continue

        # thematic break
        if re.fullmatch(r'(-{3,}|\*{3,}|_{3,})', stripped):
            output.append('<hr />')
            i += 1
            continue

        # table
        if '|' in line and i + 1 < len(lines):
            sep_line = lines[i + 1].strip()
            if re.match(r'^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?$', sep_line):
                table_lines = [line]
                j = i + 2
                while j < len(lines) and '|' in lines[j].strip():
                    table_lines.append(lines[j].rstrip())
                    j += 1
                rows = [
                    [cell.strip() for cell in row.strip().strip('|').split('|')]
                    for row in table_lines
                ]
                headers, body_rows = rows[0], rows[1:]
                head_html = ''.join(f'<th>{render_inline(cell)}</th>' for cell in headers)
                body_html = ''.join(
                    '<tr>' + ''.join(f'<td>{render_inline(cell)}</td>' for cell in row) + '</tr>'
                    for row in body_rows
                )
                output.append(
                    f'<table><thead><tr>{head_html}</tr></thead><tbody>{body_html}</tbody></table>'
                )
                i = j
                continue

        # headings
        heading_html = None
        for prefix, tag in HEADINGS:
            if line.startswith(prefix):
                heading_html = f'<{tag}>{render_inline(line[len(prefix):])}</{tag}>'
                break
        if heading_html:
            output.append(heading_html)
            i += 1
            continue

        # blockquote
        if stripped.startswith('>'):
            quote_buffer = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                quote_buffer.append(lines[i].strip().lstrip('>').strip())
                i += 1
            output.append(
                '<blockquote>'
                + ''.join(f'<p>{render_inline(item)}</p>' for item in quote_buffer)
                + '</blockquote>'
            )
            continue

        # unordered list
        if re.match(r'^\s*[-*+]\s+', line):
            items = []
            while i < len(lines) and re.match(r'^\s*[-*+]\s+', lines[i]):
                items.append(render_inline(re.sub(r'^\s*[-*+]\s+', '', lines[i].rstrip())))
                i += 1
            output.append('<ul>' + ''.join(f'<li>{item}</li>' for item in items) + '</ul>')
            continue

        # ordered list
        if re.match(r'^\s*\d+[.)]\s+', line):
            items = []
            while i < len(lines) and re.match(r'^\s*\d+[.)]\s+', lines[i]):
                items.append(render_inline(re.sub(r'^\s*\d+[.)]\s+', '', lines[i].rstrip())))
                i += 1
            output.append('<ol>' + ''.join(f'<li>{item}</li>' for item in items) + '</ol>')
            continue

        if not stripped:
            output.append('<div class="spacer"></div>')
        else:
            output.append(f'<p>{render_inline(line)}</p>')
        i += 1

    return ''.join(output)


# --------------------------------------------------------------------------- #
# content collection
# --------------------------------------------------------------------------- #

def collect_skill_books(book_map: dict[str, str]) -> list[dict]:
    """One entry per ./book-skills folder that has at least one shown file."""
    if not SKILLS_DIR.is_dir():
        return []
    books = []
    for folder in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and p.name != 'book-to-skill'):
        files = [folder / name for name in SKILL_FILES if (folder / name).is_file()]
        if not files:
            continue
        title = book_map.get(folder.name) or title_from_skill_md(folder) or prettify_key(folder.name)
        books.append({
            'key': folder.name,
            'title': title,
            'files': [{'label': f.name, 'path': f} for f in files],
        })
    return sorted(books, key=lambda b: b['title'].lower())


def collect_reading_helper_books(book_map: dict[str, str]) -> list[dict]:
    """Group ./reading-helper markdown files by book key (filename minus doc suffix)."""
    if not READING_HELPER_DIR.is_dir():
        return []
    grouped: dict[str, dict[str, Path]] = {}
    for path in sorted(READING_HELPER_DIR.glob('*.md')) + sorted(READING_HELPER_DIR.glob('*.markdown')):
        stem = path.stem
        for suffix, label in READING_HELPER_DOCS:
            if stem.endswith(f'-{suffix}'):
                grouped.setdefault(stem[: -len(suffix) - 1], {})[label] = path
                break
        else:
            grouped.setdefault(stem, {})[prettify_key(stem)] = path

    books = []
    for key, docs in grouped.items():
        ordered_labels = [label for _, label in READING_HELPER_DOCS if label in docs]
        ordered_labels += [label for label in docs if label not in ordered_labels]
        files = [{'label': label, 'path': docs[label]} for label in ordered_labels]
        title = (
            book_map.get(key)
            or title_from_reading_helper(files[0]['path'])
            or prettify_key(key)
        )
        books.append({'key': key, 'title': title, 'files': files})
    return sorted(books, key=lambda b: b['title'].lower())


# --------------------------------------------------------------------------- #
# rendering
# --------------------------------------------------------------------------- #

def render_view(view_slug: str, view_title: str, books: list[dict], empty_message: str, active: bool) -> str:
    if not books:
        body = f"<section class='tab-panel empty-state'><p class='meta'>{escape(empty_message)}</p></section>"
        return (
            f"<section class='view' id='{view_slug}' data-title='{escape(view_title)}'"
            f"{'' if active else ' hidden'}>{body}</section>"
        )

    nav_items = []
    panels = []
    for idx, book in enumerate(books):
        panel_id = f"{view_slug}--{slugify(book['key'])}"
        select_id = f"select-{panel_id}"
        is_first = idx == 0

        nav_items.append(
            f"<button class='tab{' active' if is_first else ''}' type='button' role='tab' "
            f"aria-selected='{'true' if is_first else 'false'}' data-tab='{panel_id}'>"
            f"{escape(book['title'])}</button>"
        )

        options = ''.join(
            f"<option value='{slugify(f['label'])}'{' selected' if f_idx == 0 else ''}>"
            f"{escape(f['label'])}</option>"
            for f_idx, f in enumerate(book['files'])
        )

        cards = []
        for f_idx, f in enumerate(book['files']):
            markdown = f['path'].read_text(encoding='utf-8', errors='ignore')
            cards.append(
                f"<article class='file-card' data-preview-file='{slugify(f['label'])}'"
                f"{'' if f_idx == 0 else ' hidden'}>"
                f"<div class='file-card-header'><h3>{escape(f['label'])}</h3></div>"
                f"<div class='markdown-body'>{markdown_to_html(markdown)}</div>"
                f"</article>"
            )

        count = len(book['files'])
        panels.append(
            f"<section id='{panel_id}' class='tab-panel' role='tabpanel'{'' if is_first else ' hidden'}>"
            f"<div class='panel-header'><h2>{escape(book['title'])}</h2>"
            f"<span>{count} markdown file{'s' if count != 1 else ''}</span></div>"
            f"<div class='toolbar'><label for='{select_id}'>Choose markdown file</label>"
            f"<select id='{select_id}' class='file-select'>{options}</select></div>"
            + ''.join(cards)
            + '</section>'
        )

    return (
        f"<section class='view' id='{view_slug}' data-title='{escape(view_title)}'"
        f"{'' if active else ' hidden'}>"
        f"<nav class='tabs' role='tablist' aria-label='{escape(view_title)} books'>"
        + ''.join(nav_items)
        + '</nav>'
        + ''.join(panels)
        + '</section>'
    )


STYLES_CSS = '''* { box-sizing: border-box; }
:root {
  --bg: #f6f8fa;
  --text: #24292f;
  --muted: #57606a;
  --panel: #ffffff;
  --border: #d0d7de;
  --subtle: #f6f8fa;
  --accent: #0969da;
  --accent-text: #ffffff;
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
  --accent-text: #0d1117;
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
h4,
h5 { margin: 0 0 12px; }
h1 { font-size: 2rem; }
h2 { font-size: 1.5rem; }
h3 { font-size: 1.2rem; }
h5 { font-size: 1rem; }
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
.view-tabs {
  display: inline-flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-bottom: 22px;
  padding: 6px;
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 999px;
  max-width: 100%;
}
.view-tab {
  border: none;
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  padding: 10px 20px;
  border-radius: 999px;
  cursor: pointer;
}
.view-tab:hover { color: var(--text); }
.view-tab.active {
  background: var(--accent);
  color: var(--accent-text);
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
.markdown-body h4,
.markdown-body h5 {
  margin-top: 24px;
  margin-bottom: 12px;
  border-bottom: 1px solid var(--border);
  padding-bottom: 6px;
}
.markdown-body h5 { border-bottom: none; padding-bottom: 0; }
.markdown-body p,
.markdown-body li {
  margin: 0 0 10px;
}
.markdown-body ul,
.markdown-body ol {
  padding-left: 22px;
}
.markdown-body hr {
  border: none;
  border-top: 1px solid var(--border);
  margin: 22px 0;
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
  .view-tabs { width: 100%; justify-content: center; }
}
'''

APP_JS = '''const themeToggle = document.getElementById('theme-toggle');
const pageTitle = document.getElementById('page-title');
const views = Array.from(document.querySelectorAll('.view'));
const viewTabs = Array.from(document.querySelectorAll('.view-tab'));

/* ---------- theme ---------- */
const setTheme = (theme) => {
  document.body.dataset.theme = theme;
  themeToggle.textContent = theme === 'night' ? '☀️' : '🌙';
  localStorage.setItem('skills-theme', theme);
};

setTheme(localStorage.getItem('skills-theme') || 'day');

themeToggle.addEventListener('click', () => {
  setTheme(document.body.dataset.theme === 'night' ? 'day' : 'night');
});

/* ---------- top-level views (Summary and Insights / Guided Reading) ---------- */
const setView = (viewId) => {
  const target = views.find((view) => view.id === viewId) || views[0];
  if (!target) return;

  views.forEach((view) => {
    view.hidden = view !== target;
  });
  viewTabs.forEach((btn) => {
    const isActive = btn.dataset.view === target.id;
    btn.classList.toggle('active', isActive);
    btn.setAttribute('aria-selected', isActive ? 'true' : 'false');
  });
  if (pageTitle && target.dataset.title) {
    pageTitle.textContent = target.dataset.title;
    document.title = target.dataset.title + ' · Book Explorer';
  }
  localStorage.setItem('skills-view', target.id);
};

viewTabs.forEach((btn) => {
  btn.addEventListener('click', () => setView(btn.dataset.view));
});

setView(localStorage.getItem('skills-view') || (views[0] && views[0].id));

/* ---------- book tabs, scoped to their own view ---------- */
views.forEach((view) => {
  const tabs = Array.from(view.querySelectorAll('.tab'));
  const panels = Array.from(view.querySelectorAll('.tab-panel'));

  tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
      tabs.forEach((btn) => {
        const isActive = btn === tab;
        btn.classList.toggle('active', isActive);
        btn.setAttribute('aria-selected', isActive ? 'true' : 'false');
      });
      panels.forEach((panel) => {
        panel.hidden = panel.id !== tab.dataset.tab;
      });
    });
  });
});

/* ---------- file dropdowns ---------- */
document.querySelectorAll('.file-select').forEach((select) => {
  const panel = select.closest('.tab-panel');
  const previews = Array.from(panel.querySelectorAll('.file-card'));

  select.addEventListener('change', () => {
    previews.forEach((card) => {
      card.hidden = card.dataset.previewFile !== select.value;
    });
  });
});
'''


def asset_version(content: str) -> str:
    """Short content hash, appended to asset URLs so browsers never serve a stale copy."""
    return hashlib.md5(content.encode('utf-8')).hexdigest()[:8]


def main() -> None:
    css_version = asset_version(STYLES_CSS)
    js_version = asset_version(APP_JS)
    book_map = load_skill_book_map()
    skill_books = collect_skill_books(book_map)
    reading_books = collect_reading_helper_books(book_map)

    views = [
        {
            'slug': 'view-summary-and-insights',
            'title': 'Summary and Insights',
            'books': skill_books,
            'empty': 'No book skill folders with cheatsheet, glossary, or patterns files were found.',
        },
        {
            'slug': 'view-guided-reading',
            'title': 'Guided Reading',
            'books': reading_books,
            'empty': 'No markdown files were found in the reading-helper folder.',
        },
    ]

    view_nav = ''.join(
        f"<button class='view-tab{' active' if idx == 0 else ''}' type='button' role='tab' "
        f"aria-selected='{'true' if idx == 0 else 'false'}' data-view='{view['slug']}'>"
        f"{escape(view['title'])}</button>"
        for idx, view in enumerate(views)
    )
    view_html = ''.join(
        render_view(view['slug'], view['title'], view['books'], view['empty'], active=(idx == 0))
        for idx, view in enumerate(views)
    )

    index_html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Book Explorer</title>
  <link rel="stylesheet" href="styles.css?v={css_version}" />
</head>
<body data-theme="day">
  <div class="page">
    <header class="topbar">
      <div>
        <p class="eyebrow">Book Explorer</p>
        <h1 id="page-title">Summary and Insights</h1>
      </div>
      <div class="topbar-actions">
        <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Toggle theme">☀️</button>
      </div>
    </header>

    <nav class="view-tabs" role="tablist" aria-label="Sections">
      {view_nav}
    </nav>

    <main>
      {view_html}
    </main>
  </div>

  <script src="app.js?v={js_version}"></script>
</body>
</html>
'''

    (OUT_DIR / 'index.html').write_text(index_html, encoding='utf-8')
    (OUT_DIR / 'styles.css').write_text(STYLES_CSS, encoding='utf-8')
    (OUT_DIR / 'app.js').write_text(APP_JS, encoding='utf-8')

    skill_file_count = sum(len(b['files']) for b in skill_books)
    reading_file_count = sum(len(b['files']) for b in reading_books)
    print(
        f'Summary and Insights: {len(skill_books)} books / {skill_file_count} markdown files\n'
        f'Guided Reading:       {len(reading_books)} books / {reading_file_count} markdown files\n'
        f'Wrote index.html, styles.css, app.js to {OUT_DIR}'
    )


if __name__ == '__main__':
    main()
