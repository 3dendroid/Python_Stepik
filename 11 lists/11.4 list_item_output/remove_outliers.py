n = int(input())
l = []

# Чтение n чисел
for _ in range(n):
    l.append(int(input()))

# Находим минимальное и максимальное значения
min_value = min(l)
max_value = max(l)

# Удаляем минимальное и максимальное значения, сохраняя порядок
for x in l:
    if x != min_value and x != max_value:
        print(x)

# l = [x for x in l if x != min_value and x != max_value]

