# len -> length

# a = "alk"

# b = "CEVA!"

# print(len(a))    # lungimea unui string 

# # functia upper
# print(a.upper()) # transforma literele mici ale stringului in litere mari

# print(b.lower()) # inversul lui lower

mesaj = "Buna Ziua Telespectatoriu ...."

print(mesaj.index("i")) # 6 index - returneaza pozitia pe care gaseste litera/substr

print(mesaj.index("")) # 3 (doar prima aparitie)

# print(mesaj.index("x")) # eroare

print(mesaj.index("Ziua")) # 5

# find acelasi ca index, doar ca nu da eraore daca nu gaseste, si iti intoarce -1

# functia count 
print(mesaj.count("iu"))

print(mesaj.startswith("Buna")) # True
print(mesaj.startswith("X"))    # False

print(mesaj.endswith("iu"))     # False
print(mesaj.endswith("..."))    # True

# functia replace()

print(mesaj.replace("a", "x")) # Bunx Ziux Telespectxtoriu ....
