m = int(input())
p = int(input())
n = int(input())

for i in range(m, p, n):
    population = m * ((1 + (p / 100)) ** (i - 1))
    print(population)
