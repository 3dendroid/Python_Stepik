m = int (input ())
n = int (input ())

for i in range (m % 2 - 1 + m, n - 1, -2):
    print (i)
