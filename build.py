#!/usr/bin/env python3
"""Regenerate sw.js: lists every app file for offline precaching and stamps a content
hash as the version, so any change to the app ships as an update. Run after editing."""
import hashlib, json, pathlib
root = pathlib.Path(__file__).parent
files = ['./', 'index.html', 'manifest.webmanifest']
for d in ('fonts', 'icons', 'handout'):
    files += sorted(str(p.relative_to(root)) for p in (root / d).rglob('*') if p.is_file())
h = hashlib.sha256()
for f in files[1:] + ['sw.template.js']:
    h.update(f.encode()); h.update((root / f).read_bytes())
version = h.hexdigest()[:10]
sw = (root / 'sw.template.js').read_text().replace('__VERSION__', version).replace('__ASSETS__', json.dumps(files, indent=2))
(root / 'sw.js').write_text(sw)
print(f'sw.js: version {version}, {len(files)} assets')
