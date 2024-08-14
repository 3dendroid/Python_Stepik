def print_numbers(m, n):
    for i in range(m, n + 1):
        if i % 17 == 0 or str(i).endswith('9') or (i % 3 == 0 and i % 5 == 0):
            print(i)


# Пример использования функции:
m = int(input())
n = int(input())

print_numbers(m, n)
