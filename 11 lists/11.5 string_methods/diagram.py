# s = input().split()
#
# for i in s:
#     print('+' * int(i))

nums = [int(x) * "+" for x in input().split()]
print(*nums, sep="\n")