start = population = float (input ())
percent = int (input ()) / 100
day = int (input ())

for i in range (day):
    print (i + 1, population)
    population += population * (percent)
