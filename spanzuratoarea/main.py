from hangman_art import HANGMAN
import random
from typing import List
import os
import sys

cuvinte = ["ALBASTRU", "ALARMA", "CUTIE", "LEU", "PARALELIPIPED", "MENESTREL", "ANIMATIE", "CUB"]

def clear():
    os.system("clear")

def print_meniu(wrong_guesses: int, cuvant: str, correct_guesses: List[str]):
    clear()
    print("======= SPANZURATOAREA =======")
    print(HANGMAN[wrong_guesses])
    print()

    linie = ""

    for litera in cuvant:
        if litera in correct_guesses:
            linie += litera
            linie += " "
        else:
            linie += "_ "

    print(linie)
    print()
    if linie.find("_ ") == -1:
        print("Ai castigat")
        sys.exit(0)


def main():
    cuvant = random.choice(cuvinte)
    correct_guesses = []
    wrong_guesses = 0

    while True:
        print_meniu(wrong_guesses, cuvant, correct_guesses)
        
        guess = input("Alege o litera: ")

        if guess.upper() in cuvant:
            correct_guesses.append(guess.upper())
        else:
            wrong_guesses += 1
        
        if wrong_guesses == 7:
            print("Ai pierdut")
            sys.exit(0)

main()