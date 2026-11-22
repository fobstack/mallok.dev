// Theme toggle and header menus. The site works without this file: it stays
// in dark mode and the menus open and close as plain <details> elements.
(function () {
  var root = document.documentElement;
  var meta = document.querySelector('meta[name=theme-color]');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');

  function apply(theme) {
    root.dataset.theme = theme;
    if (meta) meta.content = theme === 'light' ? '#FBFAFC' : '#0D0B14';
    try {
      localStorage.setItem('mallok-theme', theme);
    } catch (e) {}
    document.querySelectorAll('.theme-toggle').forEach(function (b) {
      b.setAttribute('aria-label', b.dataset[theme === 'dark' ? 'labelLight' : 'labelDark']);
    });
  }

  function toggle(button) {
    var next = root.dataset.theme === 'light' ? 'dark' : 'light';
    if (reduce.matches) return apply(next);
    if (!document.startViewTransition) {
      // Fallback: cross-fade colours instead of the circular reveal.
      root.classList.add('theme-fading');
      apply(next);
      setTimeout(function () {
        root.classList.remove('theme-fading');
      }, 450);
      return;
    }
    // Circular reveal from the button, using the View Transitions API.
    var r = button.getBoundingClientRect();
    var x = r.left + r.width / 2;
    var y = r.top + r.height / 2;
    var radius = Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y));
    var t = document.startViewTransition(function () {
      apply(next);
    });
    t.ready.then(function () {
      root.animate(
        {clipPath: ['circle(0px at ' + x + 'px ' + y + 'px)',
                    'circle(' + radius + 'px at ' + x + 'px ' + y + 'px)']},
        {duration: 560, easing: 'cubic-bezier(.4,0,.2,1)',
         pseudoElement: '::view-transition-new(root)'}
      );
    });
  }

  document.querySelectorAll('.theme-toggle').forEach(function (b) {
    b.setAttribute('aria-label', b.dataset[root.dataset.theme === 'light' ? 'labelDark' : 'labelLight']);
    b.addEventListener('click', function () {
      toggle(b);
    });
  });

  // Close header menus on outside click and Escape; only one open at a time.
  var menus = document.querySelectorAll('.lang-menu, .nav-mobile');
  menus.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open) return;
      menus.forEach(function (o) {
        if (o !== d) o.open = false;
      });
    });
  });
  document.addEventListener('click', function (e) {
    menus.forEach(function (d) {
      if (d.open && !d.contains(e.target)) d.open = false;
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    menus.forEach(function (d) {
      if (d.open) {
        d.open = false;
        d.querySelector('summary').focus();
      }
    });
  });
})();
