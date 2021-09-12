t = int(input())
a = []
def process(n,a):
    s = 0
    for i in range(0,n):
        s = s + a.pop(0)
    tmp = s /n
    if (tmp == int(tmp)):
        return int(tmp)
    else:
        return int(tmp)+1



for i in range(0,t):
    n = int(input())
    a = list(map(int,input().split()))
    print(process(n,a))
