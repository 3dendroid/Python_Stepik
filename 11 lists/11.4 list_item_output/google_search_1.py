n = int(input())
l = []

for i in range(n):
    l.append(input())

g = input()
for j in l:
    if g.lower() in j.lower():
        print(j)