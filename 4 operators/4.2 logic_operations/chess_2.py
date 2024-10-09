a = int (input ())
b = int (input ())
c = int (input ())
d = int (input ())

if a - 1 <= c <= a + 1 and b - 1 <= d <= b + 1 and (1 <= a <= 8 and 1 <= b <= 8 and 1 <= c <= 8 and 1 <= d <= 8):
    print ('YES')
else:
    print ('NO')
