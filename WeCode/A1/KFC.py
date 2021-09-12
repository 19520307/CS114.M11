F = float(input())
C = (F - 32) / 1.8
K = 5 / 9 * (F - 32) + 273.15

if (C == int(C)):

    print(int(C),"{:0.6}".format(K))
else: 
    print("{:0.6}".format(C),"{:0.6}".format(K))
