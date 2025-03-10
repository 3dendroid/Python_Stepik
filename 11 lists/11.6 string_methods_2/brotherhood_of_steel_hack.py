# n = input()
# for _ in range(int(n[1:])):
#     s = input()
#     if '#' in s:
#         s = s[:s.find('#')]
#     print(s.rstrip())

# x = input()
# x = x.replace(x[x.index("#")::], "").rstrip()

numbers = [4, 2, 8, 6, 5, 3, 10, 4, 100, 1, -7]
numbers.sort()
del numbers[0]
del numbers[-1]
numbers.sort(reverse=True)
print(numbers)