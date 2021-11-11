

print("Bußgeldrechner")
print("--------------")

geblitzt = input("Bist du geblitzt worden ? [j/n]")

if geblitzt == "n":
    exit("Glück gehabt!")

if geblitzt == "j":
    außerorts = input("Waren Sie außerorts?")

    if außerorts == "j":
        geschwindigkeit = int(input("Wie viel waren Sie zu schnell ?"))
        if geschwindigkeit in range(2, 11):
            exit("20€ Bußgeld")
        if geschwindigkeit in range(11, 16):
            exit("40€ Bußgeld")
        if geschwindigkeit in range(16, 21):
            exit("60€ Bußgeld")
        if geschwindigkeit in range(21, 26):
            exit("100€ Bußgeld & 1 Punkt, Herzlichen Glückwunsch, Depp")
        if geschwindigkeit in range(26, 31):
            exit("150€ Bußgeld & 1 Punkt, Herzlichen Glückwunsch, Depp")
        if geschwindigkeit in range(31, 41):
            exit("200€ Bußgeld & 1 Punkt, Herzlichen Glückwunsch, Depp")
        if geschwindigkeit in range(41, 51):
            exit("320€ Bußgeld, 2 Punkt & 1 Monat Fahrverbot, Herzlichen Glückwunsch, Depp")
        if geschwindigkeit in range(51, 61):
            exit("480€ Bußgeld, 2 Punkt & 1 Monat Fahrverbot, Herzlichen Glückwunsch, Depp")
        if geschwindigkeit in range(61, 71):
            exit("600€ Bußgeld, 2 Punkt & 2 Monat Fahrverbot, Herzlichen Glückwunsch, Depp")
        if geschwindigkeit > 70:
            exit("Bruder 700€, 2 Punkte, 3 Monate Fahrverbot. Ciao Führerschein viel Spaß mit Fahrrad fahren")
    else:
        if außerorts == "n":
            geschwindigkeit = int(input("Wie viel waren Sie zu schnell ?"))
            if geschwindigkeit in range(2, 11):
                exit("30€ Bußgeld")
            if geschwindigkeit in range(11, 16):
                exit("50€ Bußgeld")
            if geschwindigkeit in range(16, 21):
                exit("70€ Bußgeld")
            if geschwindigkeit in range(21, 26):
                exit("115€ Bußgeld & 1 Punkt, Herzlichen Glückwunsch, Depp")
            if geschwindigkeit in range(26, 31):
                exit("180€ Bußgeld & 1 Punkt, Herzlichen Glückwunsch, Depp")
            if geschwindigkeit in range(31, 41):
                exit("260€ Bußgeld & 2 Punkt & 1 Monat Fahrverbot, Herzlichen Glückwunsch, Depp")
            if geschwindigkeit in range(41, 51):
                exit("400€ Bußgeld, 2 Punkt & 1 Monat Fahrverbot, Herzlichen Glückwunsch, Depp")
            if geschwindigkeit in range(51, 61):
                exit("560€ Bußgeld, 2 Punkt & 2 Monat Fahrverbot, Herzlichen Glückwunsch, Depp")
            if geschwindigkeit in range(61, 71):
                exit("700€ Bußgeld, 2 Punkt & 3 Monat Fahrverbot, Herzlichen Glückwunsch, Depp")
            if geschwindigkeit > 70:
                exit("Bruder 800€, 2 Punkte, 3 Monate Fahrverbot. Ciao Führerschein viel Spaß mit Fahrrad fahren")

