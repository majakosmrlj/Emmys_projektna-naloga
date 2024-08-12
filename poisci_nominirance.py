
import re

with open("emmys.html") as dat:
    besedilo = dat.read()
    niz = r'<h5>(?P<nominacija>.+?)</h5>'
    nominacije = []
    for najdba in re.finditer(niz, besedilo):
        nominacije.append(najdba["nominacija"])
        
print(nominacije, len(nominacije))