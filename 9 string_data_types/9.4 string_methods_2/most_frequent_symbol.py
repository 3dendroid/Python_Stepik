a = input ()
b = 0
max = 0

for i in a:
    if a.count (i) >= b:
        b = a.count (i)
        max = i

print (max)
