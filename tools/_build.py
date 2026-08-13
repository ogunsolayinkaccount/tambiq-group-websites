import os

# Site root is one level up from /tools
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SEO / DOMAIN CONFIG
# --------------------
# "tambiq.com" is NOT a confirmed production domain — there is no CNAME file
# in this repo and no record of it being purchased/verified. It was already
# present as placeholder/aspirational text in the original site before this
# generator existed. Do not treat it as live until it's confirmed.
#
# This is the single source of truth for canonical/OG URLs on every page
# this script generates (14 of the site's 16 pages — see /tools/README.md
# for which two are hand-written and not covered by this constant).
# When the real domain is confirmed: update SITE_DOMAIN below, re-run
# _pages.py, then manually update the 4 files listed in /tools/README.md
# that this constant does not reach (index.html, about/index.html,
# sitemap.xml, robots.txt).
SITE_DOMAIN = "https://www.tambiq.com"
EMAIL_DOMAIN = "tambiq.com"

DIVISIONS = [
    ("construction", "TambiQ Construction", "Project delivery &amp; controls",
     '<path d="M3 21h18M5 21V9l7-5 7 5v12M9 21v-6h6v6"/>'),
    ("properties", "TambiQ Properties", "Real estate &amp; investment",
     '<path d="M3 11l9-7 9 7M5 10v10h5v-6h4v6h5V10"/>'),
    ("auto", "TambiQ Auto", "Automotive &amp; dealership",
     '<path d="M5 11l1.5-5h11L19 11M5 11h14M5 11v7h14v-7"/><circle cx="8.5" cy="18" r="1.6"/><circle cx="15.5" cy="18" r="1.6"/>'),
    ("logistics", "TambiQ Logistics", "Transportation &amp; supply chain",
     '<path d="M3 17h9V6H3v11zM12 10h5l4 4v3h-9v-7z"/><circle cx="7" cy="19" r="1.6"/><circle cx="17" cy="19" r="1.6"/>'),
    ("recreation", "TambiQ Recreation", "Sports &amp; community leisure",
     '<path d="M6.5 6.5a3 3 0 013-3H8v6h-.5a3 3 0 01-3-3zM17.5 6.5a3 3 0 00-3-3H16v6h.5a3 3 0 003-3zM8 6.5h8M12 9.5v5m0 0c-2 0-3.5 1-3.5 3h7c0-2-1.5-3-3.5-3z"/>'),
    ("fashion", "TambiQ Fashion", "Apparel &amp; lifestyle",
     '<path d="M9 4a3 3 0 006 0M5 7l4-3h6l4 3-3 3v11H8V10L5 7z"/>'),
    ("marketplace", "TambiQ Marketplace", "Digital commerce",
     '<path d="M4 8l1.5-4h13L20 8M4 8h16M4 8l1 12h14l1-12M9 12a3 3 0 006 0"/>'),
]

def mega_menu(prefix):
    items = []
    for i, (slug, name, tag, icon) in enumerate(DIVISIONS):
        span_cls = " col-span-2" if slug == "marketplace" else ""
        items.append(f'''<a href="{prefix}companies/{slug}/" class="{span_cls.strip()} flex items-start gap-3 p-3 rounded-xl hover:bg-gray-50 dark:hover:bg-white/5 transition-colors"><span class="h-9 w-9 shrink-0 rounded-lg bg-gold-500/10 flex items-center justify-center text-gold-600 dark:text-gold-400"><svg class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{icon}</svg></span><span><span class="block text-sm font-semibold">{name}</span><span class="block text-xs text-gray-500 dark:text-gray-400">{tag}</span></span></a>''')
    return "\n                ".join(items)

def mobile_division_links(prefix):
    items = [f'<a href="{prefix}companies/" class="py-1.5 font-semibold text-gold-600 dark:text-gold-400">View All Companies</a>']
    for slug, name, tag, icon in DIVISIONS:
        items.append(f'<a href="{prefix}companies/{slug}/" class="py-1.5">{name}</a>')
    return "\n            ".join(items)

def nav_link(href, label, active):
    cls = "text-gold-600 dark:text-gold-400" if active else "hover:text-gold-600 dark:hover:text-gold-400 transition-colors"
    return f'<a href="{href}" class="{cls}">{label}</a>'

def mobile_nav_link(href, label, active):
    cls = "py-3 text-gold-600 dark:text-gold-400" if active else "py-3 hover:text-gold-600 dark:hover:text-gold-400"
    return f'<a href="{href}" class="{cls}">{label}</a>'

def header(prefix, active):
    """active: one of home, about, companies, projects, careers, contact, news"""
    home = prefix if prefix else "./"
    return f'''  <header id="site-header" class="fixed top-0 inset-x-0 z-50 transition-all duration-300 bg-white/80 dark:bg-ink/80 backdrop-blur-md border-b border-black/5 dark:border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16 sm:h-20">
        <a href="{home}" class="flex items-center gap-2.5 shrink-0">
          <svg class="h-9 w-9 sm:h-10 sm:w-10" viewBox="0 0 40 40" role="img" aria-label="TambiQ Group emblem">
            <rect width="40" height="40" rx="9" fill="#0a0e1a"/><rect x="1" y="1" width="38" height="38" rx="8" fill="none" stroke="#c9973a" stroke-width="1"/>
            <text x="20" y="27" text-anchor="middle" font-family="'Playfair Display',serif" font-size="19" font-weight="700" fill="#e0bd66">T</text>
          </svg>
          <span class="leading-tight">
            <span class="block font-serif font-bold text-lg sm:text-xl tracking-tight">TambiQ Group</span>
            <span class="block text-[10px] sm:text-[11px] uppercase tracking-[0.2em] text-gold-600 dark:text-gold-400 -mt-0.5">LLC</span>
          </span>
        </a>
        <nav class="hidden lg:flex items-center gap-7 text-sm font-medium text-gray-600 dark:text-gray-300">
          {nav_link(home, "Home", active == "home")}
          {nav_link(prefix + "about/", "About", active == "about")}
          <div class="relative group">
            <button type="button" class="flex items-center gap-1 {"text-gold-600 dark:text-gold-400" if active == "companies" else "hover:text-gold-600 dark:hover:text-gold-400 transition-colors"}">
              Our Companies
              <svg class="h-3.5 w-3.5 mt-px" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>
            </button>
            <div class="invisible opacity-0 translate-y-1 group-hover:visible group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:visible group-focus-within:opacity-100 group-focus-within:translate-y-0 transition-all duration-150 absolute left-1/2 -translate-x-1/2 top-full pt-3 w-[640px] max-w-[90vw]">
              <div class="rounded-2xl bg-white dark:bg-ink-800 border border-black/5 dark:border-white/10 shadow-2xl p-5 grid grid-cols-2 gap-1">
                {mega_menu(prefix)}
              </div>
              <div class="mt-1 rounded-2xl bg-gray-50 dark:bg-ink-700/40 border border-black/5 dark:border-white/10 px-5 py-3">
                <a href="{prefix}companies/" class="text-sm font-semibold text-gold-600 dark:text-gold-400 hover:underline">View All Companies →</a>
              </div>
            </div>
          </div>
          {nav_link(prefix + "projects/", "Projects &amp; Investments", active == "projects")}
          {nav_link(prefix + "careers/", "Careers", active == "careers")}
          <a href="{prefix}contact/" class="px-4 py-2 rounded-full bg-ink text-white dark:bg-gold-500 dark:text-ink hover:opacity-90 transition-opacity">Contact</a>
        </nav>
        <div class="flex items-center gap-1.5">
          <button id="theme-toggle" type="button" aria-label="Toggle dark mode" class="p-2.5 rounded-full text-gray-500 hover:text-ink dark:text-gray-300 dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/10 transition-colors">
            <svg id="icon-sun" class="h-5 w-5 hidden dark:block" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
            <svg id="icon-moon" class="h-5 w-5 block dark:hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1111.2 3 7 7 0 0021 12.8z"/></svg>
          </button>
          <button id="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false" class="lg:hidden p-2.5 rounded-full text-gray-600 dark:text-gray-300 hover:bg-black/5 dark:hover:bg-white/10">
            <svg id="icon-burger" class="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
            <svg id="icon-close" class="h-6 w-6 hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
          </button>
        </div>
      </div>
    </div>
    <div id="mobile-menu" class="hidden lg:hidden border-t border-black/5 dark:border-white/10 bg-white dark:bg-ink max-h-[calc(100vh-4rem)] overflow-y-auto">
      <nav class="max-w-7xl mx-auto px-4 py-3 flex flex-col text-gray-700 dark:text-gray-200 divide-y divide-black/5 dark:divide-white/10">
        {mobile_nav_link(home, "Home", active == "home")}
        {mobile_nav_link(prefix + "about/", "About", active == "about")}
        <details class="py-3">
          <summary class="cursor-pointer list-none flex items-center justify-between hover:text-gold-600 dark:hover:text-gold-400">Our Companies<svg class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg></summary>
          <div class="mt-2 pl-3 flex flex-col gap-2 text-sm text-gray-600 dark:text-gray-300">
            {mobile_division_links(prefix)}
          </div>
        </details>
        {mobile_nav_link(prefix + "projects/", "Projects &amp; Investments", active == "projects")}
        {mobile_nav_link(prefix + "news/", "News &amp; Insights", active == "news")}
        {mobile_nav_link(prefix + "careers/", "Careers", active == "careers")}
        {mobile_nav_link(prefix + "contact/", "Contact", active == "contact")}
      </nav>
    </div>
  </header>'''

def footer(prefix):
    div_links = "\n          ".join(
        f'<li><a href="{prefix}companies/{slug}/" class="hover:text-gold-400 transition-colors">{name}</a></li>'
        for slug, name, tag, icon in DIVISIONS
    )
    return f'''  <footer class="bg-ink text-gray-300 pt-16 pb-8 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
      <div>
        <div class="flex items-center gap-2.5 mb-4">
          <svg class="h-9 w-9" viewBox="0 0 40 40" role="img" aria-label="TambiQ Group emblem"><rect width="40" height="40" rx="9" fill="#10162b"/><rect x="1" y="1" width="38" height="38" rx="8" fill="none" stroke="#c9973a" stroke-width="1"/><text x="20" y="27" text-anchor="middle" font-family="'Playfair Display',serif" font-size="19" font-weight="700" fill="#e0bd66">T</text></svg>
          <span class="font-serif font-bold text-white text-lg">TambiQ Group</span>
        </div>
        <p class="text-sm text-gray-400 leading-relaxed">Building Businesses. Creating Value. Investing in Communities.</p>
      </div>
      <div>
        <h4 class="text-white font-semibold text-sm uppercase tracking-wider mb-4">Companies</h4>
        <ul class="space-y-2.5 text-sm">
          {div_links}
        </ul>
      </div>
      <div>
        <h4 class="text-white font-semibold text-sm uppercase tracking-wider mb-4">Company</h4>
        <ul class="space-y-2.5 text-sm">
          <li><a href="{prefix}about/" class="hover:text-gold-400 transition-colors">About</a></li>
          <li><a href="{prefix}projects/" class="hover:text-gold-400 transition-colors">Projects &amp; Investments</a></li>
          <li><a href="{prefix}news/" class="hover:text-gold-400 transition-colors">News &amp; Insights</a></li>
          <li><a href="{prefix}careers/" class="hover:text-gold-400 transition-colors">Careers</a></li>
          <li><a href="{prefix}contact/" class="hover:text-gold-400 transition-colors">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-white font-semibold text-sm uppercase tracking-wider mb-4">Contact</h4>
        <ul class="space-y-2.5 text-sm text-gray-400 mb-5"><li><a href="mailto:info@{EMAIL_DOMAIN}" class="hover:text-gold-400 transition-colors">info@{EMAIL_DOMAIN}</a></li></ul>
        <h4 class="text-white font-semibold text-sm uppercase tracking-wider mb-3">Legal</h4>
        <ul class="space-y-2.5 text-sm text-gray-400">
          <li><a href="{prefix}privacy/" class="hover:text-gold-400 transition-colors">Privacy Policy</a></li>
          <li><a href="{prefix}terms/" class="hover:text-gold-400 transition-colors">Terms of Use</a></li>
        </ul>
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8 border-t border-white/10 text-sm text-gray-500 text-center">&copy; <span id="year"></span> TambiQ Group LLC. All rights reserved.</div>
  </footer>'''

SCRIPT = '''  <script>
    document.getElementById('year').textContent = new Date().getFullYear();
    (function () {
      var saved = localStorage.getItem('theme');
      var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      if (saved === 'dark' || (!saved && prefersDark)) document.documentElement.classList.add('dark');
    })();
    document.getElementById('theme-toggle').addEventListener('click', function () {
      var isDark = document.documentElement.classList.toggle('dark');
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
    var menuBtn = document.getElementById('menu-toggle');
    var mobileMenu = document.getElementById('mobile-menu');
    var burger = document.getElementById('icon-burger');
    var close = document.getElementById('icon-close');
    menuBtn.addEventListener('click', function () {
      var open = mobileMenu.classList.toggle('hidden') === false;
      menuBtn.setAttribute('aria-expanded', String(open));
      burger.classList.toggle('hidden', open);
      close.classList.toggle('hidden', !open);
    });
    mobileMenu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        mobileMenu.classList.add('hidden');
        menuBtn.setAttribute('aria-expanded', 'false');
        burger.classList.remove('hidden');
        close.classList.add('hidden');
      });
    });
    var header = document.getElementById('site-header');
    window.addEventListener('scroll', function () { header.classList.toggle('shadow-md', window.scrollY > 8); }, { passive: true });
    var revealEls = document.querySelectorAll('.reveal');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) { if (entry.isIntersecting) { entry.target.classList.add('in-view'); io.unobserve(entry.target); } });
    }, { threshold: 0.15 });
    revealEls.forEach(function (el) { io.observe(el); });
  </script>'''

HEAD_STYLE = '''<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    darkMode: 'class',
    theme: { extend: {
      colors: {
        ink: { DEFAULT: '#0a0e1a', 800: '#10162b', 700: '#161d38' },
        gold: { 300: '#f0da9e', 400: '#e0bd66', 500: '#c9973a', 600: '#a8791f' },
      },
      fontFamily: { sans: ['Inter', 'sans-serif'], serif: ['"Playfair Display"', 'serif'] },
    } },
  };
</script>
<style>
  html { scroll-behavior: smooth; }
  section[id] { scroll-margin-top: 88px; }
  .reveal { opacity: 0; transform: translateY(16px); transition: opacity .6s ease, transform .6s ease; }
  .reveal.in-view { opacity: 1; transform: translateY(0); }
  .bg-grid { background-image: linear-gradient(rgba(255,255,255,0.045) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px); background-size: 44px 44px; }
</style>'''

def page(title, description, canonical_path, prefix, active, body, og_title=None):
    og_title = og_title or title
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE_DOMAIN}{canonical_path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="TambiQ Group LLC">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{SITE_DOMAIN}{canonical_path}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
{HEAD_STYLE}
</head>
<body class="font-sans antialiased bg-white text-ink dark:bg-ink dark:text-gray-100 transition-colors">

{header(prefix, active)}

  <main>
{body}
  </main>

{footer(prefix)}

{SCRIPT}
</body>
</html>
'''

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(content)
    print("wrote", path)

STATUS_STYLES = {
    "operating": "bg-green-500/10 text-green-600 dark:text-green-400",
    "development": "bg-gold-500/10 text-gold-600 dark:text-gold-400",
    "planning": "bg-gray-100 dark:bg-white/10 text-gray-500 dark:text-gray-400",
    "coming-soon": "bg-gray-100 dark:bg-white/10 text-gray-500 dark:text-gray-400",
}
STATUS_LABELS = {
    "operating": "Operating",
    "development": "In Development",
    "planning": "Planning",
    "coming-soon": "Coming Soon",
}

def status_badge(status, extra="mb-4"):
    return f'<span class="inline-flex items-center text-[11px] font-semibold uppercase tracking-wider px-3 py-1 rounded-full {STATUS_STYLES[status]} {extra}">{STATUS_LABELS[status]}</span>'

def division_hero(eyebrow, title, subtitle, status):
    return f'''    <section class="relative bg-ink text-white overflow-hidden pt-32 pb-20 sm:pt-40 sm:pb-24">
      <div class="absolute inset-0 bg-grid opacity-60"></div>
      <div class="relative max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p class="reveal text-xs sm:text-sm font-semibold tracking-[0.25em] uppercase text-gold-400 mb-5">{eyebrow}</p>
        {status_badge(status, "mb-5")}
        <h1 class="reveal font-serif font-bold text-4xl sm:text-5xl leading-[1.1] mb-6">{title}</h1>
        <p class="reveal text-base sm:text-lg text-gray-300 max-w-2xl mx-auto">{subtitle}</p>
      </div>
    </section>'''

def section_header(eyebrow, title, subtitle=""):
    sub = f'<p class="reveal text-gray-600 dark:text-gray-300 max-w-2xl mx-auto mt-4">{subtitle}</p>' if subtitle else ""
    return f'''<p class="reveal text-xs font-semibold tracking-[0.25em] uppercase text-gold-600 dark:text-gold-400 mb-4">{eyebrow}</p>
        <h2 class="reveal font-serif text-3xl sm:text-4xl font-bold">{title}</h2>
        {sub}'''
