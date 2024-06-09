a = len(input())
b = len(input())
c = len(input())

max = max(a, b, c)
min = min(a, b, c)
middle = (a + b + c) - (max + min)

if middle - min == max - middle:
    print('YES')
else:
    print('NO')
