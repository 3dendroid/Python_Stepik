string = input().lower().split()

count = string.count('a')
count += string.count('an')
count += string.count('the')

print(f'Общее количество артиклей: {count}')
