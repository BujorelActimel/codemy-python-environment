"""
Cere utilizatorului sa introduca adresa de email si salveaza-o intr-o variabila.
Cere utilizatorului sa introduca un numar de telefon (10 cifre) si salveaza-l intr-o variabila.
Afiseaza partea de dinainte de "@" din email + ultimele 3 cifre din numarul de telefon.

Exemplu:
Care este adresa ta de email? ion.popescu@gmail.com
Care este numarul tau de telefon? 0723456789
ion.popescu789
"""

email = input("Care este adresa ta de email? ")
nr_telefon = input("Care este numarul tau de telefon?(10 cifre) ")

# gasirea indexului lui @
index = email.find("@")

rezultat = email[:index] + nr_telefon[-3:]

print(rezultat)