n = int (input ())

counter_three = 0
counter_last_digit = 0
counter_even = 0
counter_sum_more_5 = 0
counter_multiplication_more_7 = 1
count_greater_than_seven = 0
counter_digits_0_and_5 = 0

counter_last = n % 10

while n != 0:
    a = n % 10
    n = n // 10

    if a == 3:
        counter_three += 1
    if a == counter_last:
        counter_last_digit += 1
    if a % 2 == 0:
        counter_even += 1
    if a > 5:
        counter_sum_more_5 += a
    if a > 7:
        counter_multiplication_more_7 *= a
        count_greater_than_seven += 1
    if a in (0, 5):
        counter_digits_0_and_5 += 1

if count_greater_than_seven == 0:
    counter_multiplication_more_7 = 1

print (counter_three)
print (counter_last_digit)
print (counter_even)
print (counter_sum_more_5)
print (counter_multiplication_more_7)
print (counter_digits_0_and_5)
