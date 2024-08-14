
import re

with open("emmys.html", encoding ="utf8") as dat:
    besedilo = dat.read()
    niz = (r'<h5>(?P<nominacija>.+?)\B-(?P<leto>.+?)</h5>'
           r'<div class="label_16 uppercase">(?P<rezultat>.+?)</div>')
    nominacije = []
    for najdba in re.finditer(niz, besedilo):
        nominacije.append((najdba["nominacija"][:-1], najdba["leto"][1:], najdba["rezultat"]))
        

print(nominacije, len(nominacije))