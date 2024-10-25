digit = int (input ())
count = 0

for _ in range (digit):
    s = input ()
    if s.count ('11') >= 3:
        count += 1

print (count)
