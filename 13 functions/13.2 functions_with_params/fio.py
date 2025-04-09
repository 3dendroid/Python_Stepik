def print_fio(name, surname, patronymic):
    for i in [surname, name, patronymic]:
        print(i.upper()[0], end='')
    # print(surname.upper()[0], name.upper()[0], patronymic.upper()[0], sep='')


name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)
