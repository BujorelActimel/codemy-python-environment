import random

alegere = input("alege dintre piatra/hartie/foarfeca ")

if alegere not in ["hartie", "foarfeca", "piatra"]:
    print("Algere invalida")
else:
    alegerea_robotului = random.choice(["hartie", "foarfeca", "piatra"])

    if alegere == "hartie":
        if alegerea_robotului == "hartie":
            print("Este egalitate")
        elif alegerea_robotului == "piatra":
            print("Ai castigat")
        else:
            print("Ai pierdut")

    elif alegere == "piatra":
        if alegerea_robotului == "hartie":
            print("Ai pierdut")
        elif alegerea_robotului == "piatra":
            print("Este egalitate")
        else:
            print("Ai castigat")

    else:
        if alegerea_robotului == "hartie":
            print("Ai castigat")
        elif alegerea_robotului == "piatra":
            print("Ai pierdut")
        else:
            print("Este egalitate")