from difflib import HtmlDiff
from os import getcwd
from webbrowser import open as web_open

with open("input/a.txt", "r", encoding="utf-8_sig") as f:
    fileA = f.readlines()
with open("input/b.txt", "r", encoding="utf-8_sig") as f:
    fileB = f.readlines()

with open("output/diff.html", "w", encoding="utf-8") as html:
    html.writelines(HtmlDiff().make_file(fileA, fileB))

web_open(f"{getcwd()}/output/diff.html")
