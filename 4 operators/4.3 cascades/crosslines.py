a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b < c or d < a:
    print("пустое множество")
elif b == c:
    print(b)
elif d == a:
    print(d)
elif a <= c and b <= d:
    print(c, b)
elif c <= a and d <= b:
    print(a, d)
elif a == c and b <= d:
    print(a, b)
elif c <= a and b >= d:
    print(a, b)
elif c <= a and b == d:
    print(b, d)
elif a <= c and d >= b:
    print(c, b)
elif a <= c and d >= b:
    print(a, d)
elif a <= c and d == b:
    print(d, c)
elif a == b and c == d:
    print(a, d)



# working code
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# if b < c or d < a:
#     print("пустое множество")
# elif b == c:
#     print(b)
# elif d == a:
#     print(d)
# else:
#     print(max(a, c), min(b, d))
