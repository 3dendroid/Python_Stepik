# n = int (input ())
# print (bin (n)[2:])

n = int (input ())
s = ''

while n != 0:
    s = str (n % 2) + s
    n = n // 2
print (s)
