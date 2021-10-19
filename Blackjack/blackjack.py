import random
import os

name = input("Bitte Geben Sie ihren Namen ein\n")
string = name
wuerfel = int(0)
gesamtsumme_spieler = int(0)
gesamtsumme_computer = int(0)

#print("Aktuelle Gesamtaugensumme:", gesamtsumme_spieler)

#weiter = input("Möchten Sie weiter Würfeln ? [j/n]\n")

while gesamtsumme_spieler < 21:
        wuerfel = random.randint(1, 6)
        gesamtsumme_spieler = gesamtsumme_spieler + wuerfel
        print("Aktuelle Gesamtsumme:", gesamtsumme_spieler)

        if gesamtsumme_spieler > 21:
            exit("Du hast Verloren")

        weiter = input("Möchten Sie weiter Würfeln ? [j/n]\n")

        if weiter == "n":
            print("Das Würfeln wird beendet")
            break


while gesamtsumme_computer:
        wuerfel = random.randint(1, 6)
        gesamtsumme_computer = gesamtsumme_computer + wuerfel

        if gesamtsumme_computer > 17:
            wuerfel = random.randint(1, 6)
            print("Es wird verglichen")
            print("Der Spieler hat", gesamtsumme_spieler, "Augen\n")
            print("Der Dealer hat", gesamtsumme_computer, "Augen\n")
            if gesamtsumme_spieler > 21:
                exit('Du hast gewonnen')


if gesamtsumme_spieler == gesamtsumme_computer:
    exit("Die Bank gewinnt")

if gesamtsumme_computer > gesamtsumme_spieler:
    exit("Du hast Verloren")

if gesamtsumme_spieler > gesamtsumme_computer:
    exit("Du hast Gewonnen")
