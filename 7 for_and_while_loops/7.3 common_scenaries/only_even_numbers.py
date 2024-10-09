count = 0

for i in range (1, 11):
    n = int (input ())
    if n % 2 == 0:
        count += 1
if count == 10:
    print ("YES")
else:
    print ("NO")
