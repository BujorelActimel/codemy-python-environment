# Lucrezi pentru EA la noul joc star wars
# Seful tau vine si iti spune ca vrea ca tu sa implementezi
# creearea caracterelor custom
# Creeaza o aplicatie python in care ajuti utilizatorul sa 
# isi creeze propriul caracter din star wars
# Caracterul trebuie sa aibe:
#                             nume
#                             varsta
#                             planeta de provinienta
#                             culoarea sabiei
#                             factiune (Jedi sau Sith)

nume = input("Alege numele caracterului tau: ")
varsta = int(input("Alege varsta caracterului tau: "))
planeta = input("Alege planeta de provinienta al personajului tau (Tatooine, Courasant, Death Star)")
culoarea_sabiei = input("Alege culoare sabiei(rosu, verde, albastru, mov, galben): ")
factiune = input("Vrei sa te alaturi partii intunecate sau stai pe calea cea buna(sith, jedi): ")

print("Caracterul tau:")
print("Nume:", nume)
print("varsta:", varsta)
print("Culoarea sabiei:", culoarea_sabiei)
print("Esti de partea:", factiune)