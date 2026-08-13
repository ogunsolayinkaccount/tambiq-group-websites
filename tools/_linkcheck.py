import os, re, sys

# Site root is one level up from /tools
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    if '.git' in dirpath or '__pycache__' in dirpath or os.sep + 'tools' in dirpath:
        continue
    for f in filenames:
        if f.endswith('.html'):
            html_files.append(os.path.join(dirpath, f))

href_re = re.compile(r'href="([^"]+)"')
errors = []
checked = 0

for html_file in html_files:
    with open(html_file, encoding='utf-8') as f:
        content = f.read()
    page_dir = os.path.dirname(html_file)
    for href in href_re.findall(content):
        if href.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        checked += 1
        # strip query/hash
        clean = href.split('?')[0].split('#')[0]
        if not clean:
            continue
        target = os.path.normpath(os.path.join(page_dir, clean))
        if not os.path.exists(target):
            errors.append(f"{os.path.relpath(html_file, ROOT)} -> {href} (resolved: {os.path.relpath(target, ROOT)})")

print(f"Checked {checked} internal links across {len(html_files)} HTML files.")
if errors:
    print(f"\n{len(errors)} BROKEN LINKS:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
else:
    print("No broken internal links found.")
