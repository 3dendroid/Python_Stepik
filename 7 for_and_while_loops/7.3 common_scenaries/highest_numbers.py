n = int(input())
max_1 = 0
max_2 = 1

for i in range(1, n + 1):
    num = int(input())
    if num > max_1:
        max_2 = max_1
        max_1 = num
    elif num > max_2:
        max_2 = num
print(max_1)
print(max_2)
