        
import sys
a = set()
while (True):
    try:
        t = list(map(int,sys.stdin.readline().split()))
        if (t[0] == 1):
            a.add(t[1])
        elif (t[0] == 2):
            try:
                if (t[1] in a):
                        sys.stdout.write('1' + "\n")
                else:
                    sys.stdout.write('0' + "\n")
            except:
                pass
        elif (t[0] == 3):
            try:
                a.remove(t[1])
            except: 
                pass
        elif (t[0] == 0):
            break
    except:
        pass
