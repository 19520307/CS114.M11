import sys

n, m = map(int,input().split())

a=[]
#Tim Max length
Max = []
for i in range(m):
    Max.append(0)
for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(m):
        a[i][j] = str(a[i][j])
        Max[j] = max(Max[j],len(a[i][j]))

for i in range(n):
    for j in range(m): 
        if (j != m - 1):
            print(a[i][j].rjust(Max[j]," "),end=' ')
        else:
            print(a[i][j].rjust(Max[j]," "))