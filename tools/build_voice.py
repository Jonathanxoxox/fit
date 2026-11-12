#!/usr/bin/env python3
"""Pack voice/*.mp3 into voice.js (base64), which index.html loads as window.JT_VOICE."""
import base64, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
items = sorted((root / "voice").glob("*.mp3"))
body = ",\n".join(f'  {p.stem}: "{base64.b64encode(p.read_bytes()).decode()}"' for p in items)
(root / "voice.js").write_text("window.JT_VOICE = {\n" + body + "\n};\n")
print(f"{len(items)} lines, {(root / 'voice.js').stat().st_size // 1024} KB")
