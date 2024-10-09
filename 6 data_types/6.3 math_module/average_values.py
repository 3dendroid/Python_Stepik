from math import sqrt

a = float (input ())
b = float (input ())

avg_math = (a + b) / 2
avg_geom = sqrt (a * b)
avg_garm = (2 * a * b) / (a + b)
avg_sqrt = sqrt ((a ** 2 + b ** 2) / 2)

print (avg_math)
print (avg_geom)
print (avg_garm)
print (avg_sqrt)
