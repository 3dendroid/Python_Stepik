from time import *

iter = 33
n = []
n_a = 0
n_b = 0
t = perf_counter ()  # time()
for i in range (1, iter):
    for j in range (iter):
        for k in range (iter):
            for l in range (iter):
                n_a = i ** 3 + j ** 3
                n_b = k ** 3 + l ** 3
                if n_a == n_b and i != k and j != l and i != l and j != k:
                    if not n_a in n:
                        n.append (n_a)
                        # print(n_a, i, j, k, l)
n.sort ()
print (n, sep='\n')
# print(time() - t)
print (perf_counter () - t)
