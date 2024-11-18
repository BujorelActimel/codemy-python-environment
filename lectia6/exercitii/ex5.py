# Scrie un program care folosește exact 4 for-uri pt a printa secvența următoare:
# AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG

rezultat = ""

for _ in range(10):
    rezultat += "A"


for _ in range(7):
    rezultat += "B"

for _ in range(4):
    rezultat += "CD"

rezultat += "E"

for _ in range(6):
    rezultat += "F"

rezultat += "G"

print(rezultat)