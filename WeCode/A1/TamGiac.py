import math as m
a = float(input())
b = float(input())
c = float(input())

p = (1.0) * (1/2) * (a + b + c)
s = m.sqrt(p * (p - a) * (p - b) * (p - c))
if (a + b <= c) or (a + c <= b) or (c + b <= a):
    print("Khong phai tam giac")
elif (a == b == c):
    if (s == int(s)):
        print("Tam giac deu, dien tich =",int(s))
    else:
        print("Tam giac deu, dien tich =",round(s,2))

elif (a == b !=c) or (a == c != b) or ( b == c != a):
    if (s == int(s)):
        print("Tam giac can, dien tich =",int(s))
    else:
        print("Tam giac can, dien tich =",round(s,2))
elif (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
    if (s == int(s)):
        print("Tam giac vuong, dien tich =",int(s))
    else:
        print("Tam giac vuong, dien tich =",round(s,2))
else:
    if (s == int(s)):
        print("Tam giac thuong, dien tich =",int(s))
    else:
        print("Tam giac thuong, dien tich =",round(s,2))