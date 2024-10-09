a = int (input ())
b = int (input ())
c = int (input ())

if a < b < c or c > b > a:
    print (b)
elif c < b < a or a > b > c:
    print (b)
elif b < a < c or c > a > b:
    print (a)
elif c < a < b or b > a > c:
    print (a)
else:
    print (c)
