s = input ()
cost = 0
new_cost = 0
bee = chr (128029)

eng_letters = 'eyopaxcETOPAHXCBM'
rus_letters = 'еуорахсЕТОРАНХСВМ'

for i in range (len (s)):
    cost += ord (s[i]) * 3

for i in range (len (eng_letters)):
    if eng_letters[i] in s:
        s = s.replace (s[i], rus_letters[eng_letters.find (s[i])])

for k in range (len (s)):
    new_cost += ord (s[k]) * 3

print (f"Старая стоимость: {cost}{bee}")
print (f"Новая стоимость: {new_cost}{bee}")
