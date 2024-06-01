a = int(input())
b = int(input())
c = int(input())

min = min(a, b, c)
max = max(a, b, c)
middle = (a + b + c) - (max + min)

print(max)
print(middle)
print(min)
