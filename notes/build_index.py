#!/usr/bin/env python3
"""Regenerate the index table in notes/README.md from the topic files.

Run it whenever you add a note or change a Status line:
    python3 notes/build_index.py
"""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"
ICON = {"not-started": "  ", "learning": "🟡", "can-explain": "✅"}

rows = []
for path in sorted(glob.glob(os.path.join(ROOT, "0[1-5]-*", "*.md"))):
    text = open(path).read()
    title = re.search(r"^# (.+)$", text, re.M)
    meta = re.search(r"\*\*Plan day:\*\* Day ([\d–]+) \(([^)]*)\).*?`([a-z-]+)`", text, re.S)
    if not (title and meta):
        continue
    days, dates, status = meta.groups()
    rows.append({
        "sort": int(re.split(r"\D", days)[0]),
        "days": days,
        "dates": dates,
        "title": title.group(1),
        "status": status,
        "rel": os.path.relpath(path, ROOT),
        "phase": os.path.basename(os.path.dirname(path)),
    })

rows.sort(key=lambda r: r["sort"])
done = sum(1 for r in rows if r["status"] == "can-explain")

out = [START, "",
       f"**{done} of {len(rows)} topics at `can-explain`.**", "",
       "| Day | Date | Topic | Status |", "|---|---|---|---|"]
phase = None
for r in rows:
    if r["phase"] != phase:
        phase = r["phase"]
        out.append(f"| | | **{phase}** | |")
    out.append(f"| {r['days']} | {r['dates']} | [{r['title']}]({r['rel']}) | {ICON.get(r['status'],'  ')} `{r['status']}` |")
out += ["", END]

readme = os.path.join(ROOT, "README.md")
body = open(readme).read()
new = re.sub(re.escape(START) + r".*?" + re.escape(END), "\n".join(out), body, flags=re.S)
open(readme, "w").write(new)
print(f"index rebuilt: {len(rows)} topics, {done} at can-explain")
