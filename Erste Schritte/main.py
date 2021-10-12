x = 42
print(x)



# print () - Methode / Funktion
# print - Funktion
# (Funktionsparameter)

fruits = ["apple", "banana", "cherry"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

age_of_person = {"Max": 18, "Denis": 19}

print(age_of_person["Denis"])
print(age_of_person["Max"])

print("//Zahlen")

print(3 + 4 * 2)
print(2 * 3 ** 2)
print(2 * (3 + 4))
print((2 + 3) * (3 + 4))
print(2 + 3 * 3 + 4)

print((2 + 4) // 3 + 4)
print((2 + 4) // (3 + 4))

print(3 / 2)

print(3 < 2 and 3 < 4 or 5 > 4)
print(5 > 4 or 3 > 2 and 4 < 3)
print((5 > 4 or 3 > 2) and 4 < 3)





#Drachen



import random

schaden=0

wuerfel = random.randint(1,20)

while wuerfel !=1:

    schaden += wuerfel
    wuerfel = random.randint(1,20)

    print("Dem Drachen werden", schaden, "Schadenspunkte hinzugefügt")