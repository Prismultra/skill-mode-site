"""Builds the Skill Mode static site into ../site (plain HTML for cPanel upload)."""
import os
from html import escape

OUT = os.path.join(os.path.dirname(__file__), '..', 'public')
STEAM = 'https://store.steampowered.com/app/3709600'
YT = 'https://www.youtube.com/@SkillMode-r9s'
EMAIL = 'skillmodeinfo@gmail.com'
NEWS_FORM = 'https://formspree.io/f/xzzrkepg'
CONTACT_FORM = 'https://formspree.io/f/mdkgplnj'
SITE = 'https://skill-mode.com/'

EXT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>'

FONTS = {
    'studio': 'https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Big+Shoulders+Display:wght@700;900&display=swap',
    'boogie': 'https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Big+Shoulders+Display:wght@700;900&family=Bungee&display=swap',
    'kinship': 'https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Big+Shoulders+Display:wght@700;900&family=Unbounded:wght@600;800&display=swap',
    'all': 'https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Big+Shoulders+Display:wght@700;900&family=Bungee&family=Unbounded:wght@600;800&display=swap',
}


def head(title, desc, fonts='studio', image='images/web/boogie-bg.jpg', path=''):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="author" content="Skill Mode">
<meta name="theme-color" content="#1a6bff">
<meta name="color-scheme" content="light dark">
<meta name="darkreader-lock">
<script>try{{var t=localStorage.getItem('sm-theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Skill Mode">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}{image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="images/favicon/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="images/favicon/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="images/favicon/apple-icon-180x180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS[fonts]}">
<link rel="stylesheet" href="css/site.css?v=5">
</head>
'''


THEME_TOGGLE = '''<button class="theme-toggle" type="button" aria-label="Switch to dark mode" title="Dark mode">
        <svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M20.4 14.6A8.5 8.5 0 0 1 9.4 3.6a.6.6 0 0 0-.8-.7A9.6 9.6 0 1 0 21.1 15.4a.6.6 0 0 0-.7-.8z"/></svg>
        <svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></g></svg>
      </button>'''


def header(current, studio=True):
    links = [('games.html', 'Games'), ('about.html', 'About'), ('blog.html', 'Blog'), ('contact.html', 'Contact')]
    cur = ' aria-current="page"'
    menu = '<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>'
    # Studio pages get the light/dark switch; the game pages have their own dark look.
    tools = f'''<div class="header-tools">
      {THEME_TOGGLE}
      {menu}
    </div>''' if studio else menu
    nav = '\n      '.join(
        f'<a href="{h}"{cur if h == current else ""}>{t}</a>' for h, t in links
    )
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="images/web/skillmode-logo.png" width="96" height="74" alt="Skill Mode home"></a>
    {tools}
    <nav id="site-nav" class="nav" aria-label="Main">
      {nav}
    </nav>
  </div>
</header>
'''


FOOTER = f'''<footer class="site-footer">
  <div class="wrap">
    <div>
      <img class="logo-foot" src="images/web/skillmode-logo.png" width="84" height="65" alt="Skill Mode">
      <p class="about-line">Skill Mode is an indie game studio. We make and publish our own games.</p>
    </div>
    <div>
      <h2 class="foot-h">Studio</h2>
      <ul><li><a href="about.html">About</a></li><li><a href="blog.html">Blog</a></li><li><a href="contact.html">Contact</a></li></ul>
    </div>
    <div>
      <h2 class="foot-h">Games</h2>
      <ul><li><a href="cafe-kinship.html">Cafe Kinship</a></li><li><a href="boogie-cruise.html">Boogie Cruise</a></li><li><a href="games.html">All games</a></li></ul>
    </div>
    <div>
      <h2 class="foot-h">Elsewhere</h2>
      <ul><li><a href="{STEAM}" rel="noopener">Steam</a></li><li><a href="{YT}" rel="noopener">YouTube</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul>
    </div>
    <div class="legal-line">
      <span>&copy; 2026 Skill Mode. All rights reserved.</span>
      <a href="privacy_policy.html">Privacy policy</a>
    </div>
  </div>
</footer>
<script src="js/site.js?v=5"></script>
</body>
</html>
'''


def signup(heading='Get new game news first'):
    return f'''<section class="section" id="signup" aria-labelledby="signup-title">
  <div class="wrap">
    <div class="signup">
      <div>
        <h2 id="signup-title">{heading}</h2>
        <p>We only email when there's something worth telling you: new games, updates and behind-the-scenes stuff. No spam, and you can unsubscribe any time.</p>
      </div>
      <form action="{NEWS_FORM}" method="POST" data-ajax data-done="You're on the list. Thanks for signing up!">
        <label class="sr-only" for="signup-email">Email address</label>
        <input id="signup-email" type="email" name="email" required placeholder="you@example.com" autocomplete="email">
        <button class="btn" type="submit">Subscribe</button>
        <p class="form-note" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
'''


def page(name, title, desc, body, current='', fonts='studio', body_class='', image='images/web/boogie-bg.jpg'):
    path = '' if name == 'index.html' else name
    body_open = f'<body class="{body_class}">' if body_class else '<body>'
    html = head(title, desc, fonts, image, path) + body_open + '\n' + header(current, studio=not body_class) + body + FOOTER
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(html)


BOOGIE_BLURB = 'A racing mystery with wild tracks, big boss fights and a nightclub to hang out in between races. No guns. Just grooves and gas.'

# ------------------------------------------------------------------ home
CK_BLURB = 'A multiplayer music world in the sky. Catch live shows, make beats with friends and bring your Cafe Kinship account with you. Coming soon to the Epic Games Store.'
CK_SITE = 'https://www.cafekinship.com'

home = f'''<main id="main">
  <div class="wrap">
    <section class="select" aria-labelledby="select-title">
      <div class="select-art" aria-hidden="true">
        <img data-for="g-kinship" class="on" src="images/web/ck-hero.jpg" alt="" width="1600" height="900">
        <img data-for="g-boogie" src="images/web/boogie-bg.jpg" alt="" width="1600" height="860">
        <div class="blank" data-for="g-next"></div>
      </div>
      <div>
        <h1 id="select-title" class="sr-only">Skill Mode, an independent game studio</h1>
        <p class="select-intro">Skill Mode makes indie games. Here's what we've got.</p>
      </div>
      <ul class="select-list">
        <li class="select-item is-on" id="g-kinship" data-accent="#ff4fc8" data-accent-ink="#1a0526"
            data-blurb="{escape(CK_BLURB)}"
            data-primary="cafe-kinship.html" data-primary-label="See the game"
            data-secondary="#signup" data-secondary-label="Get updates">
          <a href="cafe-kinship.html">Cafe Kinship <span class="tag">Coming soon</span></a>
        </li>
        <li class="select-item" id="g-boogie" data-accent="#2bf0a6" data-accent-ink="#06140f"
            data-blurb="{escape(BOOGIE_BLURB)}"
            data-primary="{STEAM}" data-primary-label="Play on Steam" data-primary-ext="1"
            data-secondary="boogie-cruise.html" data-secondary-label="See the game">
          <a href="boogie-cruise.html">Boogie Cruise <span class="tag">Out now</span></a>
        </li>
        <li class="select-item" id="g-next" data-accent="#8fb8ff" data-accent-ink="#0a1020"
            data-blurb="We're working on another game too. Join the mailing list to hear about it first."
            data-primary="#signup" data-primary-label="Get updates"
            data-secondary="" data-secondary-label="">
          <a href="#signup">Next game <span class="tag">In the works</span></a>
        </li>
      </ul>
      <div class="select-foot">
        <p class="select-blurb" aria-live="polite">{escape(CK_BLURB)}</p>
        <div class="select-actions">
          <a class="btn btn-accent select-primary" href="cafe-kinship.html"><span>See the game</span><span class="ext" hidden>{EXT}</span></a>
          <a class="btn btn-line select-secondary" href="#signup">Get updates</a>
        </div>
      </div>
    </section>
  </div>

  <section class="section" aria-labelledby="studio-title">
    <div class="wrap split">
      <h2 id="studio-title">We make the games we want to play</h2>
      <div>
        <p class="lede">We're a small indie studio making games that are fast, a little weird, and fun to play, at a price anyone can grab.</p>
        <p>Nobody else decides what's fun here. We play our own games over and over and keep changing them until they feel right. Boogie Cruise was our first, and Cafe Kinship is coming soon to the Epic Games Store.</p>
        <a class="btn btn-line" href="about.html">About the studio</a>
        <dl class="facts">
          <div><dt>1</dt><dd>Game out now</dd></div>
          <div><dt>2025</dt><dd>When we started</dd></div>
          <div><dt>100%</dt><dd>Indie</dd></div>
        </dl>
      </div>
    </div>
  </section>

  <section aria-labelledby="news-title">
    <div class="wrap">
      <h2 id="news-title">Latest news</h2>
      <article class="news">
        <img src="images/web/ck-skyline-small.jpg" alt="The Cafe Kinship tower above a city at night, with searchlights" width="800" height="450" loading="lazy">
        <div>
          <time datetime="2026">2026</time>
          <h3>Announcing Cafe Kinship</h3>
          <p>Our next game is a multiplayer music world in the sky, connected to cafekinship.com. It's coming soon to the Epic Games Store.</p>
          <a class="btn btn-line" href="cafe-kinship.html">See the game</a>
          <a class="btn btn-line" href="blog.html">All news</a>
        </div>
      </article>
    </div>
  </section>

{signup()}</main>
'''
page('index.html', 'Skill Mode | Independent Game Studio',
     'Skill Mode is an independent game studio. We develop and publish our own games: Boogie Cruise, out now on Steam, and Cafe Kinship, coming soon to the Epic Games Store.',
     home)

# ------------------------------------------------------------------ games
games = f'''<main id="main">
  <div class="wrap">
    <header class="page-head">
      <h1>Games</h1>
      <p class="lede">Everything we've made so far, and what's next.</p>
    </header>

    <article class="game-band kinship" aria-labelledby="ck-band-title">
      <div class="art"><img src="images/web/ck-hero.jpg" alt="Cafe Kinship: the Sky Club sign and the Cafe Kinship tower with fireworks over the city" width="1600" height="900" loading="lazy"></div>
      <div class="info">
        <div class="chips"><span>Coming soon</span><span>Epic Games Store</span><span>Multiplayer</span><span>Music</span></div>
        <h2 id="ck-band-title">Cafe Kinship</h2>
        <p>{escape(CK_BLURB)}</p>
        <div class="actions">
          <a class="btn btn-accent" href="cafe-kinship.html">See the game</a>
          <a class="btn btn-line" href="index.html#signup">Get updates</a>
        </div>
      </div>
    </article>

    <article class="game-band boogie" aria-labelledby="bc-title">
      <div class="art"><img src="images/web/boogie-bg.jpg" alt="Boogie Cruise: a car in a torch-lit hall beside a glowing green fountain" width="1600" height="860" loading="lazy"></div>
      <div class="info">
        <div class="chips"><span>Out now</span><span>Racing</span><span>Action</span><span>Indie</span></div>
        <h2 id="bc-title">Boogie Cruise</h2>
        <p>{escape(BOOGIE_BLURB)}</p>
        <div class="actions">
          <a class="btn btn-accent" href="{STEAM}" rel="noopener">Play on Steam{EXT}</a>
          <a class="btn btn-line" href="boogie-cruise.html">See the game</a>
        </div>
      </div>
    </article>

    <article class="game-band soon" aria-labelledby="next-title">
      <div class="info">
        <h2 id="next-title">Next game</h2>
        <p>We're working on it. It'll show up here, and on the mailing list first.</p>
        <div class="actions"><a class="btn btn-line" href="index.html#signup">Get updates</a></div>
      </div>
    </article>
  </div>
</main>
'''
page('games.html', 'Games | Skill Mode', 'Games by Skill Mode, an independent game studio: Cafe Kinship, coming soon to the Epic Games Store, and Boogie Cruise, out now on Steam.',
     games, current='games.html', fonts='all')

# ------------------------------------------------------------------ boogie cruise
shots = [(1, 'a car boosting through a checkpoint ring on a raised track'), (4, 'an explosion in a stone corridor, with the health bar on screen'), (5, 'cars lined up on a desert track in a sandstorm under the Boogie Cruise sign'), (6, 'cars flying off a ramp in a sandstorm')]
shot_html = '\n'.join(
    f'        <button type="button" data-full="images/web/screenshot{n}.jpg"><img src="images/web/screenshot{n}-small.jpg" alt="Boogie Cruise screenshot {i + 1}: {escape(a)}" width="800" height="430" loading="lazy"></button>'
    for i, (n, a) in enumerate(shots)
)
boogie = f'''<main id="main">
  <section class="bc-hero" aria-labelledby="bc-title">
    <img src="images/web/boogie-bg.jpg" alt="" width="1600" height="860">
    <div class="wrap">
      <div class="chips"><span>Out now on Steam</span><span>Racing</span><span>Action</span><span>Indie</span></div>
      <h1 class="bc-title" id="bc-title">Boogie<span>Cruise</span></h1>
      <p>A racing mystery full of wild tracks, huge boss fights and a nightclub to hang out in. No guns. Just grooves and gas.</p>
      <div class="bc-actions">
        <a class="btn btn-accent" href="{STEAM}" rel="noopener">Play on Steam{EXT}</a>
        <a class="btn btn-line" href="#trailer">Watch the trailer</a>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="buy-title">
    <div class="wrap bc-buy">
      <div>
        <h2 id="buy-title">Out now on Steam</h2>
        <p>Add it to your library or wishlist right here.</p>
      </div>
      <iframe src="https://store.steampowered.com/widget/3709600/" title="Boogie Cruise on the Steam store" loading="lazy"></iframe>
    </div>
  </section>

  <section class="section" aria-labelledby="feat-title" style="padding-top:0">
    <div class="wrap">
      <h2 id="feat-title">What to expect</h2>
      <div class="bc-features">
        <div><h3>Racing with a twist</h3><p>Fast tracks packed with obstacles, hazards and surprises around every corner.</p></div>
        <div><h3>Boss battles</h3><p>Race against huge bosses. It's part race, part fight.</p></div>
        <div><h3>The nightclub</h3><p>Hang out between races, tune up your car in the garage and meet the crowd on the dance floor.</p></div>
      </div>
    </div>
  </section>

  <section class="section" id="trailer" aria-labelledby="trailer-title" style="padding-top:0">
    <div class="wrap">
      <h2 id="trailer-title">Trailer</h2>
      <div class="bc-video">
        <video controls preload="none" playsinline poster="images/web/screenshot1.jpg">
          <source src="images/Trailer.mp4" type="video/mp4">
          <a href="{STEAM}">Watch the trailer on Steam</a>
        </video>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="shots-title" style="padding-top:0">
    <div class="wrap">
      <h2 id="shots-title">Screenshots</h2>
      <p>Click a screenshot to see it bigger.</p>
      <div class="shots">
{shot_html}
      </div>
    </div>
  </section>

  <div class="lightbox" role="dialog" aria-modal="true" aria-label="Screenshot">
    <img src="" alt="">
    <button class="close" type="button">Close</button>
    <button class="prev" type="button" aria-label="Previous screenshot">&lsaquo;</button>
    <button class="next" type="button" aria-label="Next screenshot">&rsaquo;</button>
  </div>

  <section class="bc-cta" aria-labelledby="cta-title">
    <div class="wrap">
      <h2 id="cta-title">Ready to race?</h2>
      <p>It's out now on Steam.</p>
      <a class="btn btn-accent" href="{STEAM}" rel="noopener">Play on Steam{EXT}</a>
    </div>
  </section>
</main>
'''
page('boogie-cruise.html', 'Boogie Cruise | Skill Mode',
     'Boogie Cruise: a high-speed racing mystery with boss battles, a nightclub hub and no guns. By Skill Mode, out now on Steam.',
     boogie, current='games.html', fonts='boogie', body_class='theme-boogie')

# ------------------------------------------------------------------ cafe kinship (the game)
ck_shots = [
    ('ck-vip', 'The entrance to the VIP lounge, with white couches under a neon equalizer wall'),
    ('ck-lounge', 'The neon-lit VIP lounge'),
    ('ck-mall', 'The Sky Mall, a neon shopping arcade'),
    ('ck-fireworks', 'Fireworks over the Sky Club and the Cafe Kinship tower'),
    ('ck-skyline', 'The Cafe Kinship tower above the city at night, with searchlights'),
    ('ck-greenscreen', 'The green screen stage in Kinship Studios'),
]
ck_shot_html = '\n'.join(
    f'        <button type="button" data-full="images/web/{n}.jpg"><img src="images/web/{n}-small.jpg" alt="Cafe Kinship screenshot {i + 1}: {escape(a)}" width="800" height="450" loading="lazy"></button>'
    for i, (n, a) in enumerate(ck_shots)
)
kinship = f'''<main id="main">
  <section class="ck-hero" aria-labelledby="ck-title">
    <img src="images/web/ck-hero.jpg" alt="" width="1600" height="900">
    <div class="wrap">
      <div class="chips"><span>Coming soon</span><span>Epic Games Store</span><span>PC</span><span>Multiplayer</span></div>
      <h1 class="ck-title" id="ck-title">Cafe Kinship</h1>
      <p class="ck-tagline">Where music comes to life.</p>
      <p class="ck-intro">A multiplayer music world in the sky. Hang out at the Sky Club, catch live shows, make beats with friends, and bring your Cafe Kinship account with you.</p>
      <div class="ck-actions">
        <span class="ck-soon">Coming soon to the Epic Games Store</span>
        <a class="btn btn-accent" href="#signup">Get updates</a>
        <a class="btn btn-line" href="{CK_SITE}" rel="noopener">Visit cafekinship.com{EXT}</a>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="stages-title">
    <div class="wrap">
      <h2 id="stages-title">Three stages, every night</h2>
      <p>Live festivals on three stages, each with its own sound.</p>
      <div class="lineup">
        <div class="poster lava"><img src="images/web/ck-stage-lava-small.jpg" alt="The Lava Stage, glowing orange" width="800" height="450" loading="lazy"><p class="genre">Country &amp; rock</p><p class="stage">Lava Stage</p></div>
        <div class="poster crystal"><img src="images/web/ck-stage-crystal-small.jpg" alt="The Crystal Stage, glowing pink" width="800" height="450" loading="lazy"><p class="genre">Hip-hop</p><p class="stage">Crystal Stage</p></div>
        <div class="poster aurora"><img src="images/web/ck-stage-aurora-small.jpg" alt="The Aurora Stage, with blue lasers" width="800" height="450" loading="lazy"><p class="genre">EDM</p><p class="stage">Aurora Stage</p></div>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="studios-title" style="padding-top:0">
    <div class="wrap ck-split">
      <img src="images/web/ck-studio.jpg" alt="The beat maker in Kinship Studios: a big grid of colored pads" width="1600" height="900" loading="lazy">
      <div>
        <h2 id="studios-title">Kinship Studios</h2>
        <p>Make music with your friends, right there in the club.</p>
        <ul>
          <li>Make beats together on a giant pad grid</li>
          <li>Record vocals in the booth</li>
          <li>Shoot videos on the green screen stage</li>
          <li>Beats you make sync with your Cafe Kinship studio on the website</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="account-title" style="padding-top:0">
    <div class="wrap">
      <h2 id="account-title">Your account comes with you</h2>
      <p>Sign in with your Cafe Kinship account and the game knows who you are.</p>
      <div class="ck-account">
        <div><h3>Your friends</h3><p>Everyone you follow on Cafe Kinship shows up on your in-game friends list.</p></div>
        <div><h3>Your artist status</h3><p>Verified artists on the site are artists in the game too.</p></div>
        <div><h3>Your beats</h3><p>Save a beat in the game and it's waiting in your studio on the website.</p></div>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="explore-title" style="padding-top:0">
    <div class="wrap">
      <h2 id="explore-title">Explore the Sky Club</h2>
      <p>VIP lounges, the Sky Mall for art, music and fashion, and fireworks over the city. Click a screenshot to see it bigger.</p>
      <div class="shots">
{ck_shot_html}
      </div>
    </div>
  </section>

  <div class="lightbox" role="dialog" aria-modal="true" aria-label="Screenshot">
    <img src="" alt="">
    <button class="close" type="button">Close</button>
    <button class="prev" type="button" aria-label="Previous screenshot">&lsaquo;</button>
    <button class="next" type="button" aria-label="Next screenshot">&rsaquo;</button>
  </div>

  <section class="section" aria-labelledby="dlc-title" style="padding-top:0">
    <div class="wrap">
      <article class="ck-dlc">
        <img src="images/web/ck-champions.jpg" alt="Champions DLC: neon race tracks floating above the clouds" width="1600" height="686" loading="lazy">
        <div class="inner">
          <h2 id="dlc-title">Champions DLC</h2>
          <p>18 new challenge stages in THE GRID, a brand-new neon world floating above the clouds. Every stage is harder than the last: clear one to unlock the next, earn credits and become a Grand Champion.</p>
          <div class="ck-modes">
            <div><img src="images/web/ck-dlc-cycles-small.jpg" alt="Light cycles racing on a neon track" width="800" height="450" loading="lazy"><h3>Light Cycle Grand Prix</h3><p>Six neon race tracks in the sky. Race AI riders and friends, leave light walls behind you and hit the boost pads.</p></div>
            <div><img src="images/web/ck-dlc-arena-small.jpg" alt="The Champions Arena laser tag floor" width="800" height="450" loading="lazy"><h3>Champions Arena</h3><p>A laser tag tournament: six rounds from the Qualifier to the Championship, against trooper bots and your friends.</p></div>
            <div><img src="images/web/ck-dlc-vault-small.jpg" alt="A Prism Vault puzzle chamber with mirrors and light beams" width="800" height="450" loading="lazy"><h3>Prism Vault</h3><p>Six laser-mirror puzzle chambers. Bounce, split and color the beams to light every crystal, solo or as a team.</p></div>
          </div>
          <p>The DLC belongs to your Cafe Kinship account: get it on cafekinship.com and it unlocks in the game right away.</p>
        </div>
      </article>
    </div>
  </section>

{signup('Hear when it launches')}</main>
'''
page('cafe-kinship.html', 'Cafe Kinship | Skill Mode',
     'Cafe Kinship by Skill Mode: a multiplayer music world in the sky. Live stages, beat making with friends and your Cafe Kinship account. Coming soon to the Epic Games Store.',
     kinship, current='games.html', fonts='kinship', body_class='theme-kinship', image='images/web/ck-hero.jpg')

# ------------------------------------------------------------------ about
about = f'''<main id="main">
  <div class="wrap">
    <header class="page-head">
      <h1>About Skill Mode</h1>
      <p class="lede">We're a small indie studio that makes the games we want to play.</p>
    </header>
  </div>

  <section class="section">
    <div class="wrap split">
      <div>
        <p class="quote">If we wouldn't play it, we don't ship it.</p>
        <p>The Skill Mode team</p>
      </div>
      <div>
        <p>Skill Mode started in 2025 because we wanted to make the kind of games we'd actually play: fast, a bit weird, and fun from the first minute. We don't chase trends. We make what we're excited about.</p>
        <p>We're small, so we do everything ourselves, from the first prototype to the Steam page. That also means nobody else decides what's fun. We play our games constantly and keep changing them until they feel right.</p>
        <p>Our first game, Boogie Cruise, is a racing mystery with boss fights and a nightclub hub. Our next one, <a href="cafe-kinship.html">Cafe Kinship</a>, is a multiplayer music world in the sky, coming soon to the Epic Games Store.</p>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0" aria-labelledby="values-title">
    <div class="wrap">
      <h2 id="values-title">What we care about</h2>
      <div class="values">
        <div><h3>Make something new</h3><p>We want every game to feel different from anything else out there.</p></div>
        <div><h3>Fun comes first</h3><p>A game can look great, but if it isn't fun to play, it's not done. Most of our time goes into how it feels.</p></div>
        <div><h3>Be straight with players</h3><p>We'll tell you what's done, what's coming and what we got wrong. No overpromising.</p></div>
        <div><h3>Do it right</h3><p>Being indie means no excuses. If something isn't good enough, we fix it.</p></div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0" aria-labelledby="talk-title">
    <div class="wrap split">
      <h2 id="talk-title">Get in touch</h2>
      <div>
        <p class="lede">Got a question, a bug, or want to work together? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        <a class="btn btn-blue" href="contact.html">Contact us</a>
        <a class="btn btn-line" href="games.html">See our games</a>
      </div>
    </div>
  </section>
</main>
'''
page('about.html', 'About | Skill Mode', 'Skill Mode is a small, independent game studio that develops and publishes its own games, starting with Boogie Cruise.',
     about, current='about.html')

# ------------------------------------------------------------------ blog
blog = f'''<main id="main">
  <div class="wrap">
    <header class="page-head">
      <h1>Blog</h1>
      <p class="lede">News and updates from the studio.</p>
    </header>

    <article class="post" aria-labelledby="p2">
      <img src="images/web/ck-skyline.jpg" alt="The Cafe Kinship tower above a city at night, with searchlights" width="1600" height="900" loading="lazy">
      <div>
        <time datetime="2026">2026</time>
        <h2 id="p2">Announcing Cafe Kinship</h2>
        <p>That surprise we mentioned? It's our next game. Cafe Kinship is a multiplayer music world in the sky, connected to cafekinship.com.</p>
        <p>Catch live shows on three festival stages, make beats with friends in Kinship Studios, hang out in the VIP lounge and shop the Sky Mall. Sign in with your Cafe Kinship account and your friends, artist status and beats come with you.</p>
        <p>It's coming soon to the Epic Games Store for PC.</p>
        <a class="btn btn-blue" href="cafe-kinship.html">See the game</a>
      </div>
    </article>

    <article class="post" aria-labelledby="p1">
      <img src="images/web/boogie-bg.jpg" alt="" width="1600" height="860" loading="lazy">
      <div>
        <time datetime="2025">2025</time>
        <h2 id="p1">Boogie Cruise is out now on Steam</h2>
        <p>After months of building and testing tracks, Boogie Cruise is finally out on Steam.</p>
        <a class="btn btn-line" href="boogie-cruise.html">See the game</a>
      </div>
    </article>
  </div>
{signup('Get new posts by email')}</main>
'''
page('blog.html', 'Blog | Skill Mode', 'News and dev updates from Skill Mode, an independent game studio.', blog, current='blog.html')

# ------------------------------------------------------------------ contact
contact = f'''<main id="main">
  <div class="wrap">
    <header class="page-head">
      <h1>Contact</h1>
      <p class="lede">Questions, bug reports, press or business stuff: send it our way. We read everything.</p>
    </header>
  </div>
  <section class="section">
    <div class="wrap contact-grid">
      <div class="contact-ways">
        <div>
          <h3>Email</h3>
          <a class="big-email" href="mailto:{EMAIL}">{EMAIL}</a>
          <p>For press, partnerships and support.</p>
        </div>
        <div>
          <h3>Boogie Cruise on Steam</h3>
          <p>The store page, reviews and community hub: <a href="{STEAM}" rel="noopener">store.steampowered.com</a></p>
        </div>
        <div>
          <h3>YouTube</h3>
          <p>Trailers and dev videos: <a href="{YT}" rel="noopener">youtube.com/@SkillMode-r9s</a></p>
        </div>
      </div>
      <form class="form" action="{CONTACT_FORM}" method="POST" data-ajax data-done="Message sent. We'll reply by email.">
        <h2 style="font-size:1.8rem">Send a message</h2>
        <label>Your name<input type="text" name="name" required autocomplete="name"></label>
        <label>Email address<input type="email" name="_replyto" required autocomplete="email"></label>
        <label>Subject<input type="text" name="subject" required></label>
        <label>Message<textarea name="message" required></textarea></label>
        <button class="btn btn-blue" type="submit">Send message</button>
        <p class="form-note" aria-live="polite"></p>
      </form>
    </div>
  </section>
</main>
'''
page('contact.html', 'Contact | Skill Mode', 'Contact Skill Mode, an independent game studio: press, partnerships and support.', contact, current='contact.html')

print('built pages')

# ------------------------------------------------------------------ privacy
sections = [
    ('overview', 'Overview', f'''
      <p>Skill Mode ("we", "us") is an independent game studio. We run skill-mode.com and develop and publish the games Boogie Cruise and Cafe Kinship. This policy explains what information we collect, how we collect it, what we use it for, who we share it with and how long we keep it.</p>
      <p>It covers this website and our games. Questions about it go to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'''),
    ('collect', 'What we collect and how', f'''
      <h3>Things you give us</h3>
      <ul>
        <li><strong>Mailing list:</strong> your email address, when you sign up on this site.</li>
        <li><strong>Contact form and email:</strong> your name, email address, subject and message, when you write to us.</li>
      </ul>
      <h3>Things collected automatically</h3>
      <ul>
        <li><strong>Server logs:</strong> like almost every website, our web host records each visit: IP address, browser type, the page requested, the referring page and the time. Our host also uses this to block automated attacks.</li>
        <li>We don't use analytics or advertising trackers on this site.</li>
      </ul>
      <h3>In our games</h3>
      <ul>
        <li><strong>Boogie Cruise</strong> is sold and played through Steam. The game doesn't send us your personal information. Steam (Valve) handles your account, purchase, achievements and any stats under <a href="https://store.steampowered.com/privacy_agreement/" rel="noopener">Valve's privacy policy</a>. Steam gives us sales and usage numbers in aggregate, which don't identify you.</li>
      </ul>
      <h3>In Cafe Kinship (the game)</h3>
      <ul>
        <li><strong>Your Cafe Kinship account:</strong> you link the game to your account by entering a code at cafekinship.com/link. The game then gets a sign-in token, saved on your PC, and uses it to load your username, profile picture, artist status, the people you follow and which DLC you own. Your password is never entered in the game.</li>
        <li><strong>Beats:</strong> beats you save in the game are saved to your Cafe Kinship account, the same as beats you make on the website.</li>
        <li><strong>Epic Games account:</strong> if you sign in with your Epic Games account, the game receives your Epic account ID and display name after you agree on Epic's sign-in screen, and uses them for online play. We don't store them on our servers.</li>
        <li><strong>Online play:</strong> when you play online, your game connects to the other players in your session, so they can see your display name, your character and what you do in the game.</li>
        <li><strong>DLC purchases:</strong> DLC is bought on cafekinship.com, where Stripe handles the payment. We record which DLC your account owns so the game can unlock it. We never see your card details.</li>
      </ul>
      <p>Your Cafe Kinship account itself, and everything you do on cafekinship.com, is also covered by the <a href="https://www.cafekinship.com/privacy" rel="noopener">Cafe Kinship privacy policy</a>.</p>'''),
    ('use', 'How we use it', '''
      <ul>
        <li>To send the mailing list: game announcements and dev updates, only if you signed up.</li>
        <li>To reply to your messages and support requests.</li>
        <li>To run Cafe Kinship (the game): sign you in, load your profile, friends and beats, unlock DLC you own, and run online play.</li>
        <li>To keep the website and our games running and secure, and to fix problems.</li>
        <li>To meet legal obligations.</li>
      </ul>
      <p>We don't sell your information, and we don't use it for advertising.</p>'''),
    ('share', 'Who we share it with', f'''
      <p>Only the services that run things for us, and only what they need:</p>
      <ul>
        <li><strong>Formspree</strong> receives mailing list sign-ups and contact form messages and passes them to us (<a href="https://formspree.io/legal/privacy-policy/" rel="noopener">their privacy policy</a>).</li>
        <li><strong>Our web host</strong> stores the site and its server logs.</li>
        <li><strong>Google Fonts</strong> serves the site's fonts, so your browser connects to Google when a page loads (<a href="https://policies.google.com/privacy" rel="noopener">Google's privacy policy</a>).</li>
        <li><strong>Steam (Valve)</strong>: the Boogie Cruise page shows Steam's store widget, which loads from Valve's servers. Steam links take you to Valve's site.</li>
        <li><strong>YouTube</strong>: links to our channel take you to YouTube.</li>
        <li><strong>Epic Online Services</strong> runs online play in Cafe Kinship (the game), including Epic Games sign-in.</li>
        <li><strong>Supabase and Vercel</strong> store and serve Cafe Kinship accounts, beats and DLC records for cafekinship.com and the game.</li>
        <li><strong>Stripe</strong> processes DLC payments on cafekinship.com.</li>
      </ul>
      <p>We'll also share information if the law requires it, or to protect Skill Mode or others from harm.</p>'''),
    ('keep', 'How long we keep it', '''
      <table>
        <thead><tr><th scope="col">Information</th><th scope="col">How long</th></tr></thead>
        <tbody>
          <tr><td>Mailing list email address</td><td>Until you unsubscribe or ask us to delete it. Then it's removed.</td></tr>
          <tr><td>Contact form messages and emails</td><td>Kept in our inbox so we can look back at past conversations. Ask us and we'll delete yours. Formspree, which delivers form messages, also keeps a copy under its own policy.</td></tr>
          <tr><td>Server logs</td><td>Kept by our web host for a short time for security and troubleshooting, then deleted automatically.</td></tr>
          <tr><td>Steam account and game data (Boogie Cruise)</td><td>Kept by Valve under its own policy. We don't hold it.</td></tr>
          <tr><td>Cafe Kinship game sign-in token</td><td>Until you sign out in the game or unlink it at cafekinship.com/link. Then it stops working and is deleted.</td></tr>
          <tr><td>Beats saved from the game</td><td>Until you delete them, or delete your Cafe Kinship account.</td></tr>
          <tr><td>DLC you own</td><td>Kept with your Cafe Kinship account so your purchase keeps working, and deleted if you delete your account. A refunded purchase is taken off your account.</td></tr>
          <tr><td>Epic account ID and display name</td><td>Not stored on our servers. They're only used while you play.</td></tr>
        </tbody>
      </table>'''),
    ('cookies', 'Cookies', '''
      <p>This site doesn't set cookies of its own. The Steam store widget on the Boogie Cruise page comes from Valve and may set Valve's cookies. You can block or clear cookies in your browser settings.</p>'''),
    ('security', 'Security', '''
      <p>The site is served over an encrypted connection (HTTPS), and only we can see what's sent through our forms. No system is completely secure, but we keep what we collect to a minimum.</p>'''),
    ('rights', 'Your choices and rights', f'''
      <ul>
        <li>Unsubscribe from the mailing list at any time with the link in any email.</li>
        <li>Ask for a copy of the information we hold about you, or ask us to correct or delete it.</li>
        <li>Cafe Kinship (the game): sign out in the game, or unlink it any time at cafekinship.com/link. To delete everything, delete your Cafe Kinship account in Settings on cafekinship.com.</li>
      </ul>
      <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> and we'll answer within 30 days. Depending on where you live, you may have further rights under local law (for example the GDPR or CCPA); contact us to use them.</p>'''),
    ('children', 'Children', '''
      <p>This website isn't directed at children under 13, and we don't knowingly collect information from them. Cafe Kinship (the game) needs a Cafe Kinship account, which is for people 13 and older. If you think a child has sent us information, email us and we'll delete it.</p>'''),
    ('changes', 'Changes to this policy', '''
      <p>When we add a game or change how we handle information, we'll update this page and the date at the top.</p>'''),
    ('contact', 'Contact', f'''
      <p>Skill Mode<br><a href="mailto:{EMAIL}">{EMAIL}</a><br>Or use our <a href="contact.html">contact form</a>.</p>'''),
]
toc = '\n        '.join(f'<a href="#{i}">{t}</a>' for i, t, _ in sections)
body_sections = '\n'.join(f'      <section id="{i}" aria-labelledby="{i}-h"><h2 id="{i}-h">{t}</h2>{c}\n      </section>' for i, t, c in sections)
privacy = f'''<main id="main">
  <div class="wrap">
    <header class="page-head">
      <h1>Privacy policy</h1>
      <p class="updated">Last updated October 8, 2026. Applies to skill-mode.com, Boogie Cruise and Cafe Kinship (the game).</p>
    </header>
  </div>
  <div class="section" style="padding-top:clamp(28px,5vw,48px)">
    <div class="wrap legal">
      <nav aria-label="On this page">
        {toc}
      </nav>
      <div>
{body_sections}
      </div>
    </div>
  </div>
</main>
'''
page('privacy_policy.html', 'Privacy Policy | Skill Mode',
     'How Skill Mode collects, uses, shares and keeps information on skill-mode.com and in its games.', privacy)

with open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    urls = ['', 'games.html', 'cafe-kinship.html', 'boogie-cruise.html', 'about.html', 'blog.html', 'contact.html', 'privacy_policy.html']
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        f.write(f'  <url><loc>{SITE}{u}</loc></url>\n')
    f.write('</urlset>\n')

# ------------------------------------------------------------------ thank-you (Formspree's no-JavaScript fallback)
thanks = '''<main id="main">
  <div class="wrap">
    <header class="page-head" style="border-bottom:0">
      <h1>Message sent</h1>
      <p class="lede">Thanks for writing. We'll reply by email as soon as we can.</p>
      <p style="margin-top:24px"><a class="btn btn-blue" href="index.html">Back to home</a></p>
    </header>
  </div>
</main>
'''
page('thank-you.html', 'Thanks | Skill Mode', 'Your message to Skill Mode was sent.', thanks)
with open(os.path.join(OUT, 'thank-you.html'), encoding='utf-8') as f:
    t = f.read()
with open(os.path.join(OUT, 'thank-you.html'), 'w', encoding='utf-8') as f:
    f.write(t.replace('<meta name="author" content="Skill Mode">', '<meta name="author" content="Skill Mode">\n<meta name="robots" content="noindex">'))
print('built privacy + sitemap + thank-you')

# ------------------------------------------------------------------ 404 (Vercel serves 404.html for any missing page)
missing = '''<main id="main">
  <div class="wrap">
    <header class="page-head" style="border-bottom:0">
      <h1>Page not found</h1>
      <p class="lede">That page doesn't exist, or it moved. Try one of these instead.</p>
      <p style="margin-top:24px">
        <a class="btn btn-blue" href="index.html">Home</a>
        <a class="btn btn-line" href="games.html">Our games</a>
      </p>
    </header>
  </div>
</main>
'''
page('404.html', 'Page not found | Skill Mode', 'This page does not exist on skill-mode.com.', missing)
with open(os.path.join(OUT, '404.html'), encoding='utf-8') as f:
    t = f.read()
# It can be shown at any address (even /a/b/c), so relative links need a fixed base.
t = t.replace('<meta name="author" content="Skill Mode">',
              '<meta name="author" content="Skill Mode">\n<meta name="robots" content="noindex">\n<base href="/">')
with open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8') as f:
    f.write(t)
print('built 404')
