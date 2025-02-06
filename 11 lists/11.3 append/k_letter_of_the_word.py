n = int(input())
s = [input() for _ in range(n)]
k = int(input())

for i in range(n):
    x = []
    x.extend(s[i])
    print(x[k - 1] if k <= len(x) else '', end='')
