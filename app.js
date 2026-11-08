const themeToggle = document.getElementById('theme-toggle');
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
