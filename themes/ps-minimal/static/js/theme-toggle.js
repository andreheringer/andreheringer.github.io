(function () {
  var btn = document.querySelector('.theme-toggle');
  if (!btn) return;
  btn.addEventListener('click', function () {
    var root = document.documentElement;
    var wasDark = root.classList.contains('theme-dark');
    root.classList.remove('theme-dark', 'theme-light');
    root.classList.add(wasDark ? 'theme-light' : 'theme-dark');
    try { localStorage.setItem('theme', wasDark ? 'light' : 'dark'); } catch (e) {}
  });
})();
