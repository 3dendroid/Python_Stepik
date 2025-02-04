n = int(input())
l = []

for i in range(n):
    s = int(input())
    l.append(s)
del l[1::2]
print(l)

