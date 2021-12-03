def a1():
    for i in range(1, 101): print(i)


def a2():
    for i in range(1, 101):
        if i != 50:
            print(i)


def a3():
    for i in range(1, 101, 2): print(i)


def a4():
    x = int(input("Ganzzahl eingeben"))
    for x in range(x, -1, -1):
        print(x)




def a5():
    x = int(input("Ganzzahl eingeben"))
    y = 1
    for n in range(x, 0, -1):
        y *= n
    print(y)


a5()
