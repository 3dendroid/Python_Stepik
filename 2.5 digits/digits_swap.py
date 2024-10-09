abc = int (input ())

a = abc // 100
b = (abc // 10) % 10
c = abc % 10

print (abc)
print (f"{a}{c}{b}")
print (f"{b}{a}{c}")
print (f"{b}{c}{a}")
print (f"{c}{a}{b}")
print (f"{c}{b}{a}")
