import random
import os

name = input("Bitte Geben Sie ihren Namen ein\n")
string = name
wuerfel = random.randint(1, 6)
gesamtsumme_spieler = wuerfel
gesamtsumme_computer = wuerfel

print("Aktuelle Gesamtaugensumme:", gesamtsumme_spieler)

weiter = input("Möchten Sie weiter Würfeln ? [j/n]\n")

if gesamtsumme_spieler < 21 or weiter == "j":
    while gesamtsumme_spieler < 21:
        wuerfel = random.randint(1, 6)
        gesamtsumme_spieler = gesamtsumme_spieler + wuerfel
        print("Aktuelle Gesamtsumme:", gesamtsumme_spieler)
        weiter = input("Möchten Sie weiter Würfeln ? [j/n]\n")
        if gesamtsumme_spieler > 21:
            exit("Du hast Verloren")


while gesamtsumme_computer:
    wuerfel = random.randint(1, 6)
    gesamtsumme_computer = gesamtsumme_computer + wuerfel
    break

    while weiter == "n":
        if gesamtsumme_computer > 17:
            print("Es wird verglichen")
            print("Der Spieler hat", gesamtsumme_spieler, "Augen\n")
            print("Der Dealer hat", gesamtsumme_computer, "Augen\n")
            break
        break

if gesamtsumme_spieler == gesamtsumme_computer:
    exit("Die Bank gewinnt")

if gesamtsumme_spieler > 21:
    exit("Du hast Verloren")

if gesamtsumme_computer > 21:
    exit("Du hast Gewonnen")

if gesamtsumme_computer > gesamtsumme_spieler:
    exit("Du hast Verloren")

if gesamtsumme_spieler > gesamtsumme_computer:
    exit("Du hast Gewonnen")
