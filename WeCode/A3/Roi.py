import sys
h, w = map(int,sys.stdin.readline().split())

c = []
for  i in range(0,h):
    tmp = list(map(int,sys.stdin.readline().split()))
    c.append(tmp)

top, left, bottom, right = map(int,sys.stdin.readline().split())

tmp = []
for i in range(0,h):
    tmp.clear()
    if (i in range(top, bottom + 1)):
        for j in range(0, left):
            tmp.append(0)
        for j in range(left, right + 1):
            tmp.append(c[i][j])
        for j in range(right + 1 , w):
            tmp.append(0)    
        sys.stdout.write(' '.join(map(str,tmp))+ "\n")
    else:
        for j in range(0, w):
            tmp.append(0)
        sys.stdout.write(' '.join(map(str,tmp))+ "\n")
