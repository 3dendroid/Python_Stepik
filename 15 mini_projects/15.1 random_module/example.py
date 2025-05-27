# import random
#
# for _ in range(10):
#     num = random.randint(0, 1)
#     if num == 0:
#         print('Орел')
#     else:
#         print('Решка')

# import random
# num = random.randint(1, 118)

# import random
# num = random.randrange(9, 81)
# print(num)

# import random
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(numbers)
# print(numbers)

# import random
# print(random.choice('BEEGEEK'))
# print(random.choice([1, 2, 3, 4]))
# print(random.choice(['a', 'b', 'c', 'd']))

# import random
# numbers = [2, 5, 8, 9, 12]
# print(random.sample(numbers, 1))
# print(random.sample(numbers, 2))
# print(random.sample(numbers, 3))
# print(random.sample(numbers, 5))

# import random
# numbers = list(range(2, 10, 2)) + [3]
# num = random.choice(numbers)
# print(num)

import random
numbers = [1, 2, 4, 6, 7, 9]
rand_numbers = random.sample(numbers, 3)
print(rand_numbers)