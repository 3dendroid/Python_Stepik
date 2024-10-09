a = str (input ())
b = str (input ())
c = str (input ())

d = len (a)
e = len (b)
f = len (c)

if min (d, e, f) == d:
    print (a)
elif min (d, f, e) == e:
    print (b)
else:
    print (c)

if max (d, e, f) == d:
    print (a)
elif max (d, e, f) == e:
    print (b)
else:
    print (c)
