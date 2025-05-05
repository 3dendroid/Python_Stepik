def is_password_good(password):
    lens = 0
    upper = 0
    lower = 0
    nums = 0

    if len(password) >= 8:
        lens += 1
    for i in password:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            nums += 1

    if lens == 1 and upper >= 1 and lower >= 1 and nums >= 1:
        return True
    else:
        return False

    # считываем данные


txt = input()

# вызываем функцию
print(is_password_good(txt))

# print(is_password_good("aabbCC11OP"))
# print(is_password_good('abC1pu'))
# print(is_password_good('aa13AN'))


# def is_password_good(password):
#     upp = [i for i in password if i.isupper()]
#     low = [i for i in password if i.islower()]
#     dig = [i for i in password if i.isdigit()]
#     return all([len(password) >= 8, upp, low, dig])
# txt = input()
# print(is_password_good(txt))