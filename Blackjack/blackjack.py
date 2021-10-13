import random
import os

name = input("Bitte Geben Sie ihren Namen ein\n")
string = name
wuerfel = random.randint(1, 6)
gesamtsumme_spieler = wuerfel

print("Aktuelle Gesamtaugensumme:", wuerfel_ausgabe)

weiter = input("Möchten Sie weiter Würfeln ? [j/n]")

while weiter == "j":
    os.system("cls")
    wuerfel = random.randint(1, 6)
    wuerfel_ausgabe = wuerfel_ausgabe + wuerfel
    print("Aktuelle Gesamtsumme:")