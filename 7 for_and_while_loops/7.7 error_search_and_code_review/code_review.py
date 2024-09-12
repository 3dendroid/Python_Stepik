# Ревью кода – проверка исходного кода программы с целью обнаружения и исправления ошибок и неточностей, которые остались незамеченными при начальной разработке.

# В процессе ревью кода могут быть исправлены:

# фактические ошибки;
# производительность кода;
# читабельность кода и ошибки форматирования кода.

# Целью ревью кода является улучшение качества программного кода и совершенствование навыков программиста.


num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
        break
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')