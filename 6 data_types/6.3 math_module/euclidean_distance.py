from math import sqrt, pow

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

a = pow(x1 - x2, 2)
b = pow(y1 - y2, 2)
p = sqrt(a + b)

print(p)
