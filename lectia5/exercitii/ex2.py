# Cere utilizatorului să introducă de la tastatura varsta lui, dacă introduce un nr negativ,
# programul sa ii spuna ca varsta este invalidă

varsta = float(input("Ce varsta ai? "))

if varsta < 0:
    print("Varsta este invalida")