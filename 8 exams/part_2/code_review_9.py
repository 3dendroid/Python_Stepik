n = 4
counter = 0
maximum = -10 ** 4

for i in range (1, n + 1):
    x = int (input ())
    if x % 2 != 0:
        counter += 1
        if x > maximum:
            maximum = x
if counter > 0:
    print (counter, sep='')
    print (maximum, sep='')
else:
    print ('NO')
