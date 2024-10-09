even = 0

for i in range (0, 7):
    n = int (input ())
    if n % 2 == 0:
        even += n

if even > 0:
    print (even)
else:
    print ("0")
