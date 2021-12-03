l_1 = []
l_2 = []

for x in range(0,6):
    if x%2 == 0:
        l_2.append(x)
    else:
        l_1.append(x)

l_2.extend(l_1)
l_2.sort()
print(l_1)
print(l_2)