n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

i = 0 
j = 0
c=[]
while (i < n or j < m):
    if ( i != n and  j == m):
        for k in range(i,n):
            c.append(a[k])
        break
    elif (i == n and j != m):
        for k in range(j,m):
            c.append(b[k])
        break
    if (a[i] < b[j]):
        c.append(a[i])
        i = i + 1
    else:
        c.append(b[j])
        j = j + 1

for i in range(len(c)):
    print(c[i],end = ' ')