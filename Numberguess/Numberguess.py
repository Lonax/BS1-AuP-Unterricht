import random

name = input("Bitte Geben Sie ihren Namen ein\n")
string = name
zufallszahlen = random.randint(1, 100)
counter = 0

while True:
    guess = input("Bitte geben Sie eine Zahl ein\n")
    guess = int(guess)
    counter = counter + 1
    if zufallszahlen == guess:
        print("Glückwunsch", name, "Du hast gewonnen und hast", counter, "Versuche gebraucht")
        break
    elif zufallszahlen > guess:
        print("Größer")
    else:
        print("Kleiner")


