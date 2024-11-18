intrebari = {
    "Care este capitala Frantei? ": "Paris",
    "Cate continente sunt pe Pamant? ": "7",
    "Care este cel mai lung rau din lume? ": "Nil",
    "Cate planete sunt in sistemul solar? ": "8",
    "Care este cel mai inalt munte din lume? ": "Everest",
    "Care este capitala Japoniei? ": "Tokyo",
    "Cate oase are corpul uman adult? ": "206",
    "Care este cel mai mare ocean din lume? ": "Pacific",
    "Cate litere are alfabetul englez? ": "26",
    "Care este cel mai mare mamifer terestru? ": "Elefant",
    "Cate luni are planeta Marte? ": "2",
    "Care este cel mai mare lac din lume? ": "Caspic",
    "Cate taste are o claviatura standard? ": "88",
    "Care este cel mai mic os din corpul uman? ": "Scărița",
    "Cate elemente sunt in tabelul periodic? ": "118",
    "Care este capitala Italiei? ": "Roma",
    "Cate zile are un an bisect? ": "366",
    "Care este cel mai mare mamifer marin? ": "Balena albastră",
    "Cate culori are un curcubeu? ": "7",
    "Care este capitala Spaniei? ": "Madrid",
}

scor = 0
scor_maxim = len(intrebari) * 10

for intrebare in intrebari:
    print(intrebare)
    raspuns = input(">> ")
    raspuns_corect = intrebari[intrebare]
    if raspuns_corect == raspuns:
        scor += 10

print("Ai obtinut", scor, "puncte din", scor_maxim)

if scor > 0.9 * scor_maxim:
    print("Wow! Esti un adevarat geniu!!!")
elif scor > 0.75 * scor_maxim:
    print("Super! Te-ai descurcat bine!!!")
elif scor >= 0.5 * scor_maxim:
    print("Meh! Ai avut un scor mediu -_-")
else:
    print("Du-te si mai citeste :(")
