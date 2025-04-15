def compute_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c

x = int(input())
y = int(input())
hypotenuse = compute_hypotenuse(x, y)
print(hypotenuse)