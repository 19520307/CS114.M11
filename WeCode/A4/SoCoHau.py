n, m = map(int,input().split())
if (n > m):
    print(0)
else:
    n= str(n)
    m = str(m)
    LenN = len(n)
    LenM = len(m) 
    s = "0"
    i =  0
    st =""
    while (LenM > LenN):
        s = s + m[i]
        i += 1
        LenM -= 1 
    LenM = len(m) 
    for k in range(i,LenM):
        st = st + m[k]
    if (int(st) >= int(n)):
        print(int(s) + 1)
    else:
        print(int(s))



    #print(s)
    #print(m)
    #print(st)