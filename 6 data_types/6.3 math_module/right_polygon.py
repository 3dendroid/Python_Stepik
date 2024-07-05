import math as m

n = int(input())
a = float(input())

S = (n * a ** 2) / (4 * m.tan(m.pi / n))
print(S)
