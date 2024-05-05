a = int(input())
first_a = a // 1000
second_a = (a // 100) % 10
thrid_a = (a // 10) % 10
fourth_a = a % 10

if first_a + fourth_a == second_a - thrid_a:
    print('ДА')
else:
    print('НЕТ')

# print(first_a)
# print(second_a)
# print(thrid_a)
# print(fourth_a)
