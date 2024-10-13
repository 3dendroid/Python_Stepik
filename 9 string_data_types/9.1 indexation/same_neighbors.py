n = input ()
same = 0

for i in range (len (n) - 1):
    if n[i] == n[i + 1]:
        same += 1

print (same)
