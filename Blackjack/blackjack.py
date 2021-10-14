import random
import os

name = input("Bitte Geben Sie ihren Namen ein\n")
string = name
wuerfel = random.randint(6, 6)
gesamtsumme_spieler = wuerfel
gesamtsumme_computer = wuerfel

print("Aktuelle Gesamtaugensumme:", gesamtsumme_spieler)

weiter = input("Möchten Sie weiter Würfeln ? [j/n]\n")

while weiter == "j":
    wuerfel = random.randint(6, 6)
    gesamtsumme_spieler = gesamtsumme_spieler + wuerfel
    print("Aktuelle Gesamtsumme:", gesamtsumme_spieler)
    weiter = input("Möchten Sie weiter Würfeln ? [j/n]\n")
    break

if gesamtsumme_spieler < 21:
    wuerfel = random.randint(1, 6)
    gesamtsumme_spieler = gesamtsumme_spieler + wuerfel
    print("Aktuelle Gesamtsumme:", gesamtsumme_spieler)
    weiter = input("Möchten Sie weiter Würfeln ? [j/n]\n")
    while weiter == "j":
        wuerfel = random.randint(1, 6)
        gesamtsumme_spieler = gesamtsumme_spieler + wuerfel
        print("Aktuelle Gesamtsumme:", gesamtsumme_spieler)
        weiter = input("Möchten Sie weiter Würfeln ? [j/n]\n")
        break



while gesamtsumme_computer:
    wuerfel = random.randint(6, 6)
    gesamtsumme_computer = gesamtsumme_computer + wuerfel
    if gesamtsumme_computer > 17:
        print("Es wird verglichen")
        print("Der Spieler hat", gesamtsumme_spieler, "Augen\n")
        print("Der Dealer hat", gesamtsumme_computer, "Augen\n")

        break

if gesamtsumme_spieler == gesamtsumme_computer:
    print("Die Bank gewinnt")
    exit(0)
if gesamtsumme_spieler > 21:
    print("Du hast Verloren")
    exit(0)
if gesamtsumme_computer > 21:
    print("Du hast Gewonnen")
    exit(0)
if gesamtsumme_computer > gesamtsumme_spieler:
    print("Du hast Verloren")
    exit(0)
if gesamtsumme_spieler > gesamtsumme_computer:
    print("Du hast Gewonnen")
    exit(0)




