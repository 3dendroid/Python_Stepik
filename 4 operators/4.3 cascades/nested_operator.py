x = int (input ())
y = int (input ())

if x > 0:
    if y > 0:
        print ('Первая четверть')
    else:
        print ('Четвертая четверть')
else:
    if y > 0:
        print ('Вторая четверть')
    else:
        print ('Третья четверть')
