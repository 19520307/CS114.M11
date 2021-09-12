n = int(input())
import math as m
s = 0
t = m.trunc(m.sqrt(n))
for i in range(1,t + 1):
    if (n % i == 0):
        if( n / i == i):
            s = s + i
        else:
            s = s + i + n / i

print(int(s - n))