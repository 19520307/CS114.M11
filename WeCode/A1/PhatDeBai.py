n = int(input())
k = int(input())
p = int(input())
q = int(input())

t = (p - 1) * 2 + q 

 
if (t - k > 0):
    p = int((t - k) / 2)  + (t - k) % 2
    if ((t - k) % 2 == 0):
        q = 2
    else:
        q = 1
    print(p,q)
    exit(0)

if (t + k <= n):
    p = int((t + k) / 2)  + (t + k) % 2
    if ((t + k) % 2 == 0):
        q = 2
    else:
        q = 1
    print(p,q)
    exit(0)

print(-1) 
