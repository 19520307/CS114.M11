def process(s,st):
    
    if (len(s) != len(st)):
        return False
    for i in range(0,len(st)):
        if (s[i] != st[len(st) - i - 1]):
            return False
    return True

s1 = input()
s2 = input()
if (process(s1,s2)):
    print("YES")
else:
    print("NO")