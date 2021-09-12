n = int(input())

a = list(map(int,input().split()))

k,x = map(int,input().split())

b = []
b.append(abs(a[0] - x))

for i in range(1,n):
    b.append(b[i - 1] + abs(a[i] - x))

#print(b)
Min = b[k-1]
#print(Min)
vt = 0

for i in range(1,n - k + 1):    
    s = b[i + k - 1] - b[i - 1]
    #print(s)
    if (Min > s):
        Min = s
        vt = i


for i in range(vt, vt + k ):
    print(a[i],end =' ')
