# Fiind date vârstele a doi copii afișați care dintre ei este cel mai mare și cu cât

nume1 = input("Cum il cheama pe primul copil? ")
copil1 = int(input("Ce varsta are primul copil? "))

nume2 = input("Cum il cheama pe al doilea copil? ")
copil2 = int(input("Ce varsta are al doilea copil? "))

if copil1 > copil2:
    # print(nume1, "este mai mare decat", nume2, "cu", (copil1 - copil2), "ani")
    print(f"{nume1} este mai mare decat {nume2} cu {copil1 - copil2} ani")
else:
    # print(nume2, "este mai mare decat", nume1, "cu", (copil2 - copil1), "ani")
    print(f"{nume2} este mai mare decat {nume1} cu {copil2 - copil1} ani")
