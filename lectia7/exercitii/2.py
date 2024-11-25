# Scrie un program care sa inverseze un număr. Ex: 1234 -> 4321

numar = int(input("Introduceti un numar: "))

print(f"Inainte: {numar}")

# rezultat = ""
rezultat = 0

while numar > 0:
    # rezultat += str(numar)[-1]
    ultima_cifra = numar % 10
    rezultat = rezultat * 10 + ultima_cifra
    numar = numar // 10

print(f"Dupa: {rezultat}")


# print(f"Dupa: {str(numar)[::-1]}")