with open("input.txt") as f:
    lines = f.readlines()

stanga = []
dreapta = []

for line in lines:
    left_number, right_number = line.split()
    left_number = int(left_number)
    right_number = int(right_number)
    stanga.append(left_number)
    dreapta.append(right_number)

stanga = sorted(stanga)
dreapta = sorted(dreapta)

# print(stanga)
# print(dreapta)

suma = 0

for i in range(len(stanga)):
    primul_numar = stanga[i]
    al_doilea_numar = dreapta[i]

    numere = [primul_numar, al_doilea_numar]
    numere = sorted(numere)
    diferenta = numere[-1] - numere[0]

    suma += diferenta

print(suma)

