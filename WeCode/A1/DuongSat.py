k,t = map(int, input().split())

p = int(t / k)

if (p % 2 == 0):
    print(0 + t % k)
else:
    print(k - t % k)
