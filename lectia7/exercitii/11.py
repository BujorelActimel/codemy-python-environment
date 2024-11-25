# Se citește un număr natural n cu cel mult 9 cifre. 
# Afișați mesajul este palindrom sau nu este palindrom 
# dacă numărul are sau nu această proprietate. Un număr 
# este palindrom dacă este egal cu oglinditul său.
# Exemplu: pentru n=1234321 se va afișa este palindrom.


n = int(input("Introduceti un numar: "))


# invers = int(str(n)[::-1])

# if n == invers:
#     print("E palindrom")
# else:
#     print("Nu e palindrom")


# 12321

n = str(n)

e_palindrom = True

for i in range(len(n) // 2):
    if (n[i] != n[-i - 1]):
        e_palindrom = False

if e_palindrom:
    print("Este palindrom")
else:
    print("Nu este palindrom")
