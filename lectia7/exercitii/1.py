# Se da o lista cu n elemente nr nat. 
# Sa se verifice daca toate elem din lista au număr par de cifre

lista = [10, 1123, 13, 80, 1011]
toate_pare = True


for numar in lista:
    # if len(str(numar)) % 2 != 0:
    #     toate_pare = False
    numar_cifre = 0
    while numar > 0:
        numar = numar // 10
        numar_cifre += 1

    if numar_cifre % 2 != 0:
        toate_pare = False

if toate_pare == True:
    print("Toate sunt pare")
else:
    print("Nu sunt toate pare")
