def cereNumar(mesaj):
    while True:
        try:
            numar = int(input(mesaj))
            return numar
        except:
            print("Nu ai introdus un numar")


a = cereNumar("primul numar: ")
b = cereNumar("al doilea numar: ")

try:
    print("Rezultatul impartirii este", a / b)
except ZeroDivisionError:
    print("Am avut o eroare")