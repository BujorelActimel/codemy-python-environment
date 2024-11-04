# Scrie un program care determina minimul a 3 numere întregi

a = int(input("a: "))

b = int(input("b: "))

c = int(input("c: "))

if a < b and a < c:
    print(f"Minimul este {a}")
elif b < a and b < c:
    print(f"Minimul este {b}")
else:
    print(f"Minimul este {c}")