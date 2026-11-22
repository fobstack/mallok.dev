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
  // Home hero: drifting thread particles. Purple and teal points that link
  // with fine lines when close and lean away from the pointer. Off under
  // reduced motion; paused when the hero is off screen or the tab is hidden.
  var hero = document.querySelector('.hero-home');
  if (hero && !reduce.matches && window.HTMLCanvasElement) {
    var canvas = document.createElement('canvas');
    canvas.className = 'hero-particles';
    canvas.setAttribute('aria-hidden', 'true');
    hero.insertBefore(canvas, hero.firstChild);
    var ctx = canvas.getContext('2d');
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var w = 0, h = 0, dots = [], running = false, onScreen = true, frame = 0;
    var pointer = {x: -1e4, y: -1e4};
    var LINK = 120, PUSH = 110, PAD = 14;
    // Text boxes (hero-relative) where no line is drawn, so copy stays clean.
    var quiet = [];
    var measure = function () {
      var o = hero.getBoundingClientRect();
      quiet = [];
      hero.querySelectorAll(
        '.hero-copy h1, .hero-copy .lede, .hero-copy .badge, ' +
        '.hero-copy .actions, .hero-copy .cmd, .hero-copy .cmd-hint'
      ).forEach(function (el) {
        var r = el.getBoundingClientRect();
        quiet.push([r.left - o.left - PAD, r.top - o.top - PAD,
                    r.right - o.left + PAD, r.bottom - o.top + PAD]);
      });
    };
    // Checks points along the segment so a line cannot clip a text corner.
    var crosses = function (a, b) {
      for (var t = 0.25; t < 1; t += 0.25) {
        if (inQuiet(a.x + (b.x - a.x) * t, a.y + (b.y - a.y) * t)) return true;
      }
      return false;
    };
    var inQuiet = function (x, y) {
      for (var q = 0; q < quiet.length; q++) {
        var b = quiet[q];
        if (x > b[0] && x < b[2] && y > b[1] && y < b[3]) return true;
      }
      return false;
    };

    var size = function () {
      var r = hero.getBoundingClientRect();
      w = r.width;
      h = r.height;
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var n = Math.min(70, Math.round((w * h) / 16000));
      while (dots.length < n) {
        dots.push({
          x: Math.random() * w, y: Math.random() * h,
          vx: (Math.random() - 0.5) * 0.3, vy: (Math.random() - 0.5) * 0.3,
          r: 1 + Math.random() * 1.6, teal: Math.random() < 0.22
        });
      }
      dots.length = n;
      measure();
    };

    var draw = function () {
      if (!running) return;
      var light = root.dataset.theme === 'light';
      var purple = light ? '126,34,206' : '168,85,247';
      var teal = light ? '13,148,136' : '45,212,191';
      var lineA = light ? 0.22 : 0.28;
      ctx.clearRect(0, 0, w, h);
      for (var i = 0; i < dots.length; i++) {
        var d = dots[i];
        var dx = d.x - pointer.x, dy = d.y - pointer.y;
        var dist = Math.hypot(dx, dy);
        if (dist < PUSH && dist > 0.1) {
          var f = (1 - dist / PUSH) * 0.6;
          d.x += (dx / dist) * f;
          d.y += (dy / dist) * f;
        }
        d.x += d.vx;
        d.y += d.vy;
        if (d.x < -10) d.x = w + 10; else if (d.x > w + 10) d.x = -10;
        if (d.y < -10) d.y = h + 10; else if (d.y > h + 10) d.y = -10;
      }
      for (i = 0; i < dots.length; i++) dots[i].q = inQuiet(dots[i].x, dots[i].y);
      for (i = 0; i < dots.length; i++) {
        d = dots[i];
        for (var j = i + 1; j < dots.length; j++) {
          var e = dots[j];
          var l = Math.hypot(d.x - e.x, d.y - e.y);
          if (l < LINK && !d.q && !e.q && !crosses(d, e)) {
            ctx.strokeStyle = 'rgba(' + purple + ',' + (lineA * (1 - l / LINK)).toFixed(3) + ')';
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(d.x, d.y);
            ctx.lineTo(e.x, e.y);
            ctx.stroke();
          }
        }
        ctx.fillStyle = 'rgba(' + (d.teal ? teal : purple) + ',' + (light ? 0.55 : 0.75) + ')';
        ctx.beginPath();
        ctx.arc(d.x, d.y, d.r, 0, 6.2832);
        ctx.fill();
      }
      frame = requestAnimationFrame(draw);
    };

    var update = function () {
      var go = onScreen && !document.hidden && !reduce.matches;
      if (go && !running) {
        running = true;
        frame = requestAnimationFrame(draw);
      } else if (!go && running) {
        running = false;
        cancelAnimationFrame(frame);
      }
    };

    size();
    new ResizeObserver(size).observe(hero);
    new IntersectionObserver(function (entries) {
      onScreen = entries[0].isIntersecting;
      update();
    }).observe(hero);
    document.addEventListener('visibilitychange', update);
    reduce.addEventListener('change', function () {
      update();
      if (reduce.matches) ctx.clearRect(0, 0, w, h);
    });
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      pointer.x = e.clientX - r.left;
      pointer.y = e.clientY - r.top;
    });
    hero.addEventListener('pointerleave', function () {
      pointer.x = pointer.y = -1e4;
    });
    update();
  }
})();
