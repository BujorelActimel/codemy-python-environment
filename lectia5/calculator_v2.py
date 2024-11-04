import mate
import sys

primul_numar = input("Primul numar: ")
if primul_numar.isnumeric():
    primul_numar = int(primul_numar)
else:
    print("Nu ai introdus un numar")
    sys.exit(1)


al_doilea_numar = input("Al doilea numar: ")
if al_doilea_numar.isnumeric():
    al_doilea_numar = int(al_doilea_numar)
else:
    print("Nu ai introdus un numar")
    sys.exit(1)

operatie = input("Alege o operatie(+, -, /, *): ")

if operatie == "+":
    rez = mate.suma(primul_numar, al_doilea_numar)
    print(f"Rezultatul este {rez}")
elif operatie == "-":
    rez = mate.scadere(primul_numar, al_doilea_numar)
    print(f"Rezultatul este {rez}")
elif operatie == "/":
    rez = mate.impartire(primul_numar, al_doilea_numar)
    print(f"Rezultatul este {rez}")
elif operatie == "*":
    rez = mate.inmultire(primul_numar, al_doilea_numar)
    print(f"Rezultatul este {rez}")
else:
    print("Operatie invalida")