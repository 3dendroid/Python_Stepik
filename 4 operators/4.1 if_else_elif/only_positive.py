a = int (input ())
b = int (input ())
c = int (input ())

sum = 0

if a >= 0:
    sum += a
else:
    a = 0

if b >= 0:
    sum += b
else:
    b = 0
if c >= 0:
    sum += c
else:
    c = 0

print (a + b + c)
