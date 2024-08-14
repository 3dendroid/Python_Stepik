from math import log

n = int(input())
num = 0

for i in range(1, n + 1):
    x = (1 / i)
    num = num + x
    sum = num - log(n)

print(sum)