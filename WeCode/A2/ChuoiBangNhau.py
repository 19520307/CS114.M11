t = int(input())

def process(s,st):
    for i in range(0,len(st)):
        if (s.find(st[i]) != -1):
            return True
    return False


for i in range(0,t):
    s1 = input()
    s2 = input()
    if (process(s1,s2)):
        print("YES")
    else:
        print("NO")