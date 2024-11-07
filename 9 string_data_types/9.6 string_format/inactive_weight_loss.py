day = int (input ())
weight = float (input ())
goal = 100 - day * 0.2

if weight <= goal:
    print ('Все идет по плану')
    print (f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {goal} кг')
elif weight >= goal:
    print ('Что-то пошло не так')
    print (f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {goal} кг')
