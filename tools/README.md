# /tools — Development Utilities

These scripts are **development-only utilities** used to generate and verify the
TambiQ Group LLC static site. They are **not required by the live website** —
GitHub Pages (or any static host) only ever serves the plain `.html`, `.json`,
`.xml`, and `.txt` files elsewhere in this repo. Nothing in `/tools` is
referenced by, or loaded from, any page.

Requires Python 3 (no third-party packages). Run all commands from the `/tools`
directory itself, e.g.:

```bash
cd tools
python _pages.py
```

## `_build.py`

Shared library, not run directly. Defines the site's design-system building
blocks in one place — the header (with mega-menu and mobile accordion nav),
footer, `<head>` boilerplate/SEO tags, status badges, and a few reusable
section layouts (hero, card grid, CTA). `_pages.py` imports from this file so
every page stays visually and structurally consistent without hand-copying
~500 lines of HTML per page.

If you need to change something that appears identically on every page —
the nav links, the footer columns, the color/font tokens, the status badge
styles — change it here once, then re-run `_pages.py` (see below) to
regenerate every page that uses it.

## `_pages.py`

Run this to (re)generate every page **except** the homepage (`/index.html`)
and `/about/index.html`, which are hand-written and not touched by this
script:

```
/companies/index.html
/companies/construction/index.html
/companies/properties/index.html
/companies/auto/index.html
/companies/logistics/index.html
/companies/recreation/index.html
/companies/fashion/index.html
/companies/marketplace/index.html
/projects/index.html
/careers/index.html
/news/index.html
/contact/index.html
/privacy/index.html
/terms/index.html
```

Run it with:

```bash
cd tools
python _pages.py
```

This is the fastest way to add an 8th division later, or to push a nav/footer
change from `_build.py` out to every generated page — edit the content in
`_pages.py` (or the shared blocks in `_build.py`), then re-run.

**Note:** this script overwrites the files above every time it runs. Don't
hand-edit those files expecting the change to survive the next run — change
the generator instead. (`/index.html` and `/about/index.html` are safe to
hand-edit; the script doesn't touch them.)

## `_linkcheck.py`

Scans every `.html` file in the site for internal `href="..."` links and
verifies each one resolves to a real file/directory on disk. Ignores
`http(s)://`, `mailto:`, and `#anchor` links. Run it with:

```bash
cd tools
python _linkcheck.py
```

Exits non-zero and lists every broken link if it finds one; otherwise prints
a clean summary. Good to run after any bulk content or structure change.
