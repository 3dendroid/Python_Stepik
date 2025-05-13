def is_valid_password(password):
    parts = password.split(':')

    if len(parts) != 3:
        return False
    try:
        a, b, c = map(int, parts)
    except ValueError:
        return False
    if str(a) != str(a)[::-1]:
        return False
    if b < 2 or any(b % i == 0 for i in range(2, int(b ** 0.5) + 1)):
        return False

    # Проверка: c — чётное
    if c % 2 != 0:
        return False
    return True

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
