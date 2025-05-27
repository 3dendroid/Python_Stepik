n = int(input())
attempts = 0

while 2 ** attempts <= n:
    attempts += 1

print(attempts)