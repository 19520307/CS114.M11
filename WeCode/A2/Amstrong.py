n = int(input())


def Sochuso(x):
    scs = 0
    while (x != 0):
        x = int(x / 10)
        scs = scs + 1
    return scs


scs = Sochuso(n)

m = n 

Ams = 0
while (m != 0):
    s = m % 10
    m = int(m / 10)
    Ams = Ams + s**scs

if (Ams == n):
    print("True")
else:
    print("False")

    

