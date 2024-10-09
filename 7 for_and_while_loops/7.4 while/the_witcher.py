digit = int (input ())
count = 0

while digit >= 25:
    count += 1
    digit = digit - 25
while digit >= 10:
    count += 1
    digit = digit - 10
while digit >= 5:
    count += 1
    digit = digit - 5
while digit >= 1:
    count += 1
    digit = digit - 1
print (count)
