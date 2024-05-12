a = int(input())
b = int(input())
c = int(input())

if a == b == c == a:
    print('Равносторонний')
elif a != b != c != a:
    print('Разносторонний')
else:
    print('Равнобедренный')
