s = str (input ())
count = 0

for i in range (len (s)):
    if s[i].isnumeric ():
        count += 1

print (count)

# print(sum(i.isdigit() for i in input()))
