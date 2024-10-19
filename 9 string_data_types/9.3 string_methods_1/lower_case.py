s = input ()

count = 0

for i in s:
    if i in s.lower () and i not in s.upper ():
        count += 1

print (count)
