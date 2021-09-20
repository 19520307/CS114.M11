        
a = set()
while (True):
    t = list(map(int,input().split()))
    if (t[0] == 1):
        a.add(t[1])
    elif (t[0] == 2):
        if (t[1] in a):
            print("1")
        else:
            print("0")
    elif (t[0] == 0):
        break

