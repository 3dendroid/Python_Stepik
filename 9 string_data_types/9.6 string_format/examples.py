birth_year = 1993
text = 'My name is Denis, I was born in ' + str (birth_year)
print (text)

birth_year = 1993
text = 'My name is Denis, I was born in {}'.format (birth_year)
print (text)

birth_year = 1993
name = 'Denis'
profession = 'Quality Engineer'
text = 'My name is {}, I was born in {}, I work as a {}.'.format (name, birth_year, profession)
print (text)

name = 'Denis'
city = 'Bangkok'
text1 = 'My name is {0}-{0}-{0}!'.format (name, city)
text2 = '{1} is my city and {0} is my name!'.format (name, city)
print (text1)
print (text2)

first_name = 'Taylor'
second_name = 'Swift'
country = 'USA'
birth_date = '1989/12/13'
birth_place = 'West Reading, Pennsylvania'
text = '{0} {1} is a very famous singer from the {2}. She was born on {3} in {4}.'.format (first_name, second_name,
                                                                                           country, birth_date,
                                                                                           birth_place)

print (text)

first_name = 'Taylor'
last_name = 'Swift'
country = 'USA'
birth_date = '1989/12/13'
birth_place = 'West Reading, Pennsylvania'
text = f'{first_name} {last_name} is a very famous singer from the {country}. She was born on {birth_date} in {birth_place}.'

print (text)
