a = int (input ())
b = int (input ())
c = int (input ())
d = int (input ())

if a == c or (c == d and a == d):
    print ('YES')
elif b == d or (c == d and a == d):
    print ('YES')
else:
    print ('NO')
