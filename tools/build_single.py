#!/usr/bin/env python3
"""Inline voice.js into index.html so the whole game is one file.

Usage: python3 tools/build_single.py [out.html] [--fragment]
--fragment drops the outer <html>/<head>/<body> wrapper (for hosts that add their own).
"""
import pathlib, re, sys
root = pathlib.Path(__file__).resolve().parent.parent
args = [a for a in sys.argv[1:] if not a.startswith("--")]
out = pathlib.Path(args[0]) if args else root / "jenseits-tiger.single.html"
html = (root / "index.html").read_text()
tag = '<script src="voice.js"></script>'
assert tag in html, "voice.js script tag not found"
html = html.replace(tag, "<script>\n" + (root / "voice.js").read_text() + "</script>")
if "--fragment" in sys.argv:
    drop = re.compile(r'^(<!doctype html>|<html[^>]*>|</html>|<head>|</head>|<body>|</body>|<meta charset="utf-8">|<meta name="viewport"[^>]*>)$')
    html = "\n".join(l for l in html.split("\n") if not drop.match(l))
out.write_text(html)
print(out, len(html) // 1024, "KB")
