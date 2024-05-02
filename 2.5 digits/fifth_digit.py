a = int(input())
first_a = a // 10000
second_a = (a // 1000) % 10
thrid_a = (a // 100) % 10
fourth_a = (a // 10) % 10
fifth_a = a % 10

print(f"Цифра в позиции тысяч равна {first_a}")
print(f"Цифра в позиции сотен равна {second_a}")
print(f"Цифра в позиции десятков равна {thrid_a}")
print(f"Цифра в позиции единиц равна {fourth_a}")
print(f"Цифра в позиции единиц равна {fifth_a}")
