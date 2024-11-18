# se da o lista de numere
# sa se afiseze cel mai mare numar din lista

numar_maxim = 0
lista = [10, 11, 101, 99, 23, 4, 0, 201]

for nr in lista:
    if nr > numar_maxim:
        numar_maxim = nr

print(numar_maxim)
