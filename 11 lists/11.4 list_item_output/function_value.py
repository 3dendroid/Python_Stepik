n = int(input())
l = []

for i in range(n):
    a = int(input())
    f = (a + 1) ** 2
    l.append(f)
    print(a)
print()
print(*l, sep='\n')
