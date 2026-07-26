const tabs = Array.from(document.querySelectorAll('.tab'));
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
