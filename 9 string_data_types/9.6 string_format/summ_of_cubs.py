a = int (input ())
b = int (input ())

sum_kub = (a ** 3) + (b ** 3)
kub_sum = ((a + b) ** 3)

print (f'Для чисел {a} и {b}:\n'
       f'  Сумма кубов: {a}**3 + {b}**3 = {sum_kub}\n'
       f'  Куб суммы: ({a} + {b})**3 = {kub_sum}\n')
