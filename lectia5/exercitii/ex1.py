# Verifica dacă un număr este par sau impar

numar = int(input("Alege un numar: "))

# 23 / 2 = 11 rest 1
# 22 / 2 = 11 rest 0

if numar % 2 == 0:
    print("Numarul tau este par")
else:
    print("Numarul tau este impar")

# if numar / 2 == int(numar / 2):
#     print("Numarul tau este par")
# else:
#     print("Numarul tau este impar")