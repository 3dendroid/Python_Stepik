n = int(input())
end = False

while n != 0:
    last_digit = n % 10
    if last_digit == 0:
        n //= 10
    print(n)

# continue
