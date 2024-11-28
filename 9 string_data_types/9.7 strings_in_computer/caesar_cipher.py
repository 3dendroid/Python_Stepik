shift = int (input ())
str_cif = input ()
letter = ''

for letter_cif in str_cif:
    letter = ord (letter_cif) - shift
    if letter < 97:
        letter = 122 - (97 - letter) + 1

    print (chr (letter), end='')

# n, s = int(input()), input()
# a = 'abcdefghijklmnopqrstuvwxyz'
# for c in s:
#     print(a[a.find(c) - n], end='')
