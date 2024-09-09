import math

num = input()
num_list = list(map(int, str(num)))

print(sum(num_list))
print(len(num_list))
print(math.prod(num_list))
print(sum(num_list) / len(num_list))
print(num_list[0])
print(num_list[0] + num_list[-1])
