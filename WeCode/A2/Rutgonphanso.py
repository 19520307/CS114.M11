
import math as m

t = int(input())

for i in range(0,t):
    a, b =map(int,input().split())
    Gcd = m.gcd(a,b)
    a = a // Gcd
    b = b // Gcd
    if (b == 1):
        print(a)
    else:
        print(a,b)


