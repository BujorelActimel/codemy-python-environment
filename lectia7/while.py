import random

# for - sa fac actiuni repetate
# repetam un anumit numar de pasi

# while = cat timp ... 

# nume = input("Zi un nume: ")
# while nume != "stop":
#     nume = input("Zi un nume: ")
#     print(f"Ai ales numele: {nume}")

# rezervor = 100

# while rezervor > 0:
#     # merg cu masina
#     rezervor -= 10
#     print(f"Ati calatorit si ati ramas cu : {rezervor} litri")
#     if rezervor == 20:
#         print("Mai aveti un sfert din rezervor")
#     elif rezervor == 50:
#         print("Mai aveti jumate din rezervor")


# numerele de la 1 la 100

# for numar in range(1, 101):
#     print(numar)

# numar = 1
# while numar < 101:
#     print(numar)
#     numar += 1

numar_random = random.randint(1, 100)

numar_utilizator = int(input("Ghiceste numarul: "))

while numar_utilizator != numar_random:
    if numar_utilizator < numar_random:
        print("Incearca un numar mai mare")
    else:
        print("Incearca un numar mai mic")

    numar_utilizator = int(input("Ghiceste numarul: "))

print("Felicitari, ai ghicit!")
