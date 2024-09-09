num = int(input())

while num // 100 != 0:
    num = num // 10

print(num % 10)
