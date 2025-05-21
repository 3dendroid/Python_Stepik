import math


# объявление функции
def compute_binom(n, k):
    res = math.factorial(n) // math.factorial(k) / math.factorial(n - k)
    return int(res)


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
