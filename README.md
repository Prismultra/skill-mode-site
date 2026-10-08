# skill-mode.com

The Skill Mode studio website: plain HTML/CSS/JS, served by Vercel.

- `public/` is the site exactly as it's served. Vercel publishes this folder; there's no build step on Vercel.
- `src/build.py` writes every page (`public/*.html`, `sitemap.xml`). To change wording or add a page, edit it and run `python3 src/build.py`. Commit the result.
- `public/css/site.css` and `public/js/site.js` are edited by hand. Bump the `?v=` number in `head()` / `FOOTER` in `build.py` after changing them.
- Forms post to Formspree. Nothing on this site has a server or database.

Pushing to `main` deploys to https://skill-mode.com automatically.
