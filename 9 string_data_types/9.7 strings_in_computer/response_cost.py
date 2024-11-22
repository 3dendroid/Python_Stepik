response = input ()
cost = 0
bee = chr (128029)

for i in range (len (response)):
    cost += ord (response[i]) * 3
print (f"Текст сообщения: '{response}'")
print (f'Стоимость сообщения: {cost}{bee}')
