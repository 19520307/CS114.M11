import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

a = []
def find(x,A):
    for i in range(len(A)):
        if (A[i] == x):
            return i
    return -1

while (True):
    b = list(map(int,input().split()))
    if (b[0] == 0):
        a.insert(0,b[1])
    elif (b[0] == 1):
        a.append(b[1])
    elif (b[0] == 2):
        t = find(b[1],a)
        if ( t != -1 and t != len(a)):
            a.insert(t+1,b[2])
        else:
            a.insert(0,b[2])
    elif (b[0] == 3):
        t = find(b[1],a)
        if (t != -1):
            a.pop(t)
    elif (b[0] == 4):
        while (find(b[1],a) != -1):
            t = find(b[1],a)
            a.pop(t)
    elif (b[0] == 5):
        if(len(a) == 0): 
            continue
        a.pop(0)
    elif (b[0] == 6):
        break
    #print("###")
    #print(a)
    #print("###")

if (len(a) == 0):
    print("blank")
else:
    for i in range(len(a)):
        print(a[i], end = ' ')