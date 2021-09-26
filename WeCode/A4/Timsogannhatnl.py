from bisect import bisect_left
n = int(input())
a = list(map(int,input().split()))
def solve(a,k,x,n):
    n = len(a)
    if (x >= a[n-1]):
        print(a[-k],a[n-1])
    elif (x <= a[0]):
        print(a[0],a[k-1])
    else:
        g = bisect_left(a, x)
        r = g + 1
        l = g - 1
        max = a[g]
        min = a[g]
        i = k - 1
        while(i > 0):
            if (l >= 0 and r < n):
                if (x - a[l] > a[r] - x):
                    max = a[r]
                    r = r + 1
                else:
                    min = a[l]
                    l = l - 1
            elif (l < 0):
                max = a[r]
                r = r + 1
            elif (r >= n):
                min = a[l]
                l = l - 1
            i = i - 1       
        print(min,max)
    return


while (True):
    try:
        k , x = map(int,input().split())
        solve(a,k,x,n)
    except:
        exit()