# Declara o variabila de tipul string: “ Ma numesc Alina si am 13 ani.”
text = "Ma numesc Alina si am 13 ani!"

# Afișează lungimea stringului
print(len(text))

# Afișează de cate ori apare litera a
print(text.lower().count("a"))

# Afiseaza al 5-lea caracter
print(text[4])

# Afișează numele Alina din șir
print(text[10:15])

# Afiseaza ultimele 4 caractere din șir
print(text[25:])
print(text[-4:])
print(text[-4] + text[-3] + text[-2] + text[-1])

# Verifica dacă apare litera g
print(text.find("g") != -1)

# Înlocuiește toate aparițiile lui a cu &
print(text.replace("a", "&")) # fa case insensitive

# Verifica daca se termina cu !
print(text.endswith("!"))

# Afișează textul de la dreapta la stanga cu majuscule
print(text.upper())