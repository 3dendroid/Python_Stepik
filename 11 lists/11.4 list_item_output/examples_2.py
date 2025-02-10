numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
sums = 0

for i in range(len(numbers)):
    sums += numbers[i] ** 2
print(sums)