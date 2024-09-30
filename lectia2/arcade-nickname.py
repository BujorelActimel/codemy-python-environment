# Lucrezi la o companie de jocuri arcade
# Trebuie sa ajuti utilizatorul sa isi aleaga gamer Tag-ul
# dupa care va fi cunoscut pe clasamentul jocului

# Care este numele tau de familie?
# Bujor

# Care este prenumele tau?
# Mihai

# Care este porcela da?
# Buji

# Gamer Tag-ul tau este BHI

nume = input("Care este numele tau de familie? ")

prenume = input("Care este prenumele tau? ")

porecla = input("Care este porecla ta? ")

gamer_tag = nume[0] + prenume[len(prenume) // 2] + porecla[-1]

print("Gamer tag-ul tau este: ", gamer_tag.upper())

# Aron:  LOO
# David: IVD
# Ioan:  MAZ