# Se da o lista cu n elemente nr nat. Sa se verifice dacă exista nr impare

n = int(input("N: "))
am_gasit_impar = False

for i in range(n):
    nr = int(input(f"Numar {i + 1}: "))
    if nr % 2 == 1:
        am_gasit_impar = True

if am_gasit_impar:
    print("Exista numere impare")
else:
    print("Nu exista numere impare")