cod1 = "1abc2"       # -> 12
cod2 = "pqr3stu8vwx" # -> 38
cod3 = "a1b2c3d4e5f" # -> 15
cod4 = "treb7uchet"  # -> 77

coduri = [cod1, cod2, cod3, cod4]

suma = 0

for cod in coduri:
    primul = None
    al_doilea = None
    for caracter in cod:
        if caracter.isdigit():
            if primul == None:
                primul = caracter
            al_doilea = caracter

    numar = int(primul + al_doilea)

    suma += numar

print(suma)
