numar = int(input("Ce numar vrei sa verifici: "))

nr_divizori = 0

for divizor in range(1, numar + 1):
    if numar % divizor == 0:
        nr_divizori += 1

if nr_divizori == 2:
    print("Este numar prim")
else:
    print("Nu este numar prim")