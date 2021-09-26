import sys
n , m = map(int,sys.stdin.readline().split())
r , c = map(int,sys.stdin.readline().split())

a = []
for  i in range(0,n):
    tmp = list(map(int,sys.stdin.readline().split()))
    a.append(tmp)

if (r * c != n * m):
    r, c = n , m

tmp = []
count = 0
for i in range(n):
    for j in range(m):
        if (count == c-1):
            tmp.append(a[i][j])
            count = 0
            sys.stdout.write(' '.join(map(str,tmp))+ "\n")
            tmp.clear()
        else:
            tmp.append(a[i][j])
            count = count +1
   
        


