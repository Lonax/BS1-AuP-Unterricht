import numbers

Gewicht = float(input("Gewicht in KG"))
Größe = float(input("Größe in M"))


BMI = Gewicht / (Größe*Größe)

print("Dein BMI ist", round(BMI, 2))