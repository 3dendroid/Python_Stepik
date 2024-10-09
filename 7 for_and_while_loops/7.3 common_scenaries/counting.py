# counter = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
#
# print('Было введено', counter, 'чисел, больших 10.')

# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter = counter + 1
#
# print(counter)

num1 = 4
num2 = 6
num1 += num2
num1 *= num1
print (num1)

total = 0
for i in range (1, 6):
    total += i
print (total)

total = 0
for i in range (1, 6):
    total += i
    print (total, end='')
