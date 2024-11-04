# Se dau 3 numere x, a, b. Verifica daca nr x aparține intervalului [a, b]

# x, a, b

# x = 13
# a = 0
# b = 100

# x apartine intervalului [a, b]

x = int(input("X: "))

a = int(input("A: "))

b = int(input("B: "))

# if x >= a and x <= b:
if a <= x <= b:
    print("X apartine intervalului [a,b]")
else:
    print("X NU apartine intervalului [a,b]")
