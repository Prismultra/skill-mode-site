// Skill Mode site: dark mode, menu button, the home page's game select, forms, screenshot viewer.
(function () {
  // ---- dark mode: follows the device unless the visitor picked one with the
  // header button (remembered in localStorage as 'sm-theme'). The <head>
  // applies a saved pick before the page paints, so there's no flash.
  var root = document.documentElement;
  var media = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  var themeBtn = document.querySelector('.theme-toggle');
  var isDark = function () {
    var picked = root.getAttribute('data-theme');
    if (picked) return picked === 'dark';
    return !!(media && media.matches);
  };
  var paint = function () {
    var dark = isDark();
    root.classList.toggle('is-dark', dark);
    if (themeBtn) {
      themeBtn.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
      themeBtn.setAttribute('title', dark ? 'Light mode' : 'Dark mode');
    }
  };
  paint();
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var next = isDark() ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('sm-theme', next); } catch (e) {}
      paint();
    });
  }
  if (media) {
    var onChange = function () { paint(); };
    if (media.addEventListener) media.addEventListener('change', onChange);
    else if (media.addListener) media.addListener(onChange);
  }

  // ---- phone menu
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // ---- game select (home): pointing at or tabbing to a game shows its art,
  // colour, blurb and buttons. Each game is an <li data-…> in .select-list.
  var select = document.querySelector('.select');
  if (select) {
    var items = Array.prototype.slice.call(select.querySelectorAll('.select-item'));
    var arts = Array.prototype.slice.call(select.querySelectorAll('.select-art > *'));
    var blurb = select.querySelector('.select-blurb');
    var primary = select.querySelector('.select-primary');
    var secondary = select.querySelector('.select-secondary');
    var show = function (item) {
      items.forEach(function (i) { i.classList.toggle('is-on', i === item); });
      arts.forEach(function (a) { a.classList.toggle('on', a.getAttribute('data-for') === item.id); });
      select.style.setProperty('--accent', item.getAttribute('data-accent'));
      select.style.setProperty('--accent-ink', item.getAttribute('data-accent-ink'));
      blurb.textContent = item.getAttribute('data-blurb');
      var p = item.getAttribute('data-primary');
      var s = item.getAttribute('data-secondary');
      primary.hidden = !p;
      secondary.hidden = !s;
      if (p) { primary.href = p; primary.querySelector('span').textContent = item.getAttribute('data-primary-label'); }
      // Leaving the site (Steam) gets the outward-arrow icon; pages here don't.
      var external = !!item.getAttribute('data-primary-ext');
      var ext = primary.querySelector('.ext');
      if (ext) ext.hidden = !external;
      if (external) primary.setAttribute('rel', 'noopener'); else primary.removeAttribute('rel');
      if (s) { secondary.href = s; secondary.textContent = item.getAttribute('data-secondary-label'); }
    };
    items.forEach(function (item) {
      var link = item.querySelector('a');
      item.addEventListener('mouseenter', function () { show(item); });
      link.addEventListener('focus', function () { show(item); });
    });
    show(items[0]);
  }

  // ---- forms: sent with Formspree in the background, answered in place.
  // Without JavaScript they still post to Formspree normally.
  Array.prototype.forEach.call(document.querySelectorAll('form[data-ajax]'), function (form) {
    var note = form.querySelector('.form-note');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var button = form.querySelector('button[type=submit]');
      button.disabled = true;
      note.textContent = 'Sending…';
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
        .then(function (r) {
          if (!r.ok) throw new Error('bad');
          form.reset();
          note.textContent = form.getAttribute('data-done');
        })
        .catch(function () {
          note.textContent = "That didn't go through. Try again, or email skillmodeinfo@gmail.com.";
        })
        .then(function () { button.disabled = false; });
    });
  });

  // ---- screenshot viewer
  var box = document.querySelector('.lightbox');
  if (box) {
    var shots = Array.prototype.slice.call(document.querySelectorAll('.shots button'));
    var big = box.querySelector('img');
    var at = 0;
    var last = null;
    var open = function (i) {
      at = (i + shots.length) % shots.length;
      var img = shots[at].querySelector('img');
      big.src = shots[at].getAttribute('data-full');
      big.alt = img.alt;
    };
    shots.forEach(function (b, i) {
      b.addEventListener('click', function () {
        last = b;
        open(i);
        box.classList.add('open');
        box.querySelector('.close').focus();
      });
    });
    var close = function () { box.classList.remove('open'); if (last) last.focus(); };
    box.querySelector('.close').addEventListener('click', close);
    box.querySelector('.prev').addEventListener('click', function () { open(at - 1); });
    box.querySelector('.next').addEventListener('click', function () { open(at + 1); });
    box.addEventListener('click', function (e) { if (e.target === box) close(); });
    document.addEventListener('keydown', function (e) {
      if (!box.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') open(at - 1);
      if (e.key === 'ArrowRight') open(at + 1);
    });
  }
})();
