# creeaza o aplicatie care gestioneaza un magazin de fructe
# fiecare fruct are corespondent un pret
# afiseaza fructele, dupa scumpeste-le cu 10 lei si afiseaza-le
# toate perechile de fructe - preturi

fructe = {
    "banane": 30,
    "struguri": 20,
    "kiwi": 2,
    "Mango": 9
}

print(list(fructe.keys()))

fructe["banane"] += 10
fructe["struguri"] += 10
fructe["kiwi"] += 10
fructe["Mango"] += 10

print(fructe)
