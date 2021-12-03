import random

l1 = []
x=0


while x < 100:
    l1.append(random.randint(1, 6))
    x = x + 1
print(l1)

y = 0
summe = 0

while y < 0:
    print("Zahl",y, ":", l1.count(y))
    y = y + 1
    summe = (summe + l1.count(y)*y)
    print("Mittelwert Beträgt:", summe/100)