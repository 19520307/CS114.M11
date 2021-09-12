a,b,c = map(int,input().split())

if (a % c != 0):
    a = a // c + 1
else:
    a = a // c

if (b % c != 0):
    b = b // c + 1
else:
    b = b // c

print(a*b)