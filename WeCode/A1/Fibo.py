def fibo(n):
    if (n == 1 or n == 2):
        return 1
    else:
        dem = 2
        a = 1
        b = 1
        c = 0
        while (dem != n):
            c = a + b
            a = b
            b = c
            dem = dem + 1
        return c

n = int(input())

if (1 <= n and n <= 30):    
    print(fibo(n))
else:
    print("So",n,"khong nam trong khoang [1,30].")