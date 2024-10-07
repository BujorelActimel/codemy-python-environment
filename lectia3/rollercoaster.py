# Esti paznic la intrarea unui rollercoaster. Intrarea sa face doar daca
# indeplinesti mai multe conditii: 
#       - sa ai macar 16 ani impliniti,
#       - sa ai acord parental sau sa ai macar 18 ani
#       - sa ai 40 lei pentru bilet. 
# Sunt atatea chestii de verificat care sunt greu de tinut minte incat
# faci un program care sa verifice daca o persoana poate sa intre sau nu.
# Asa nu te mai pot pacali diavolii astia impielitati

# Bonus round
# Dupa o saptamana de lucrat realizezi ca ai salariul cam mic, asa ca accepti si mita
# Daca cineva iti da macar 100 de lei, ii lasi sa intre indiferent daca indeplinesc criteriile


varsta = int(input("Cati ani are? "))
acord = input("Are acord parental?(da sau nu) ")
bani = int(input("Cati bani are? "))

conditie1 = varsta >= 16
conditie2 = acord == "da" or varsta >= 18
conditie3 = bani >= 40

if ((conditie1 and conditie2 and conditie3) or bani >= 100):
    print("Poti sa intrii")
else:
    print("Nu poti sa intrii")
