s = input ()

vowels = 'ауоыиэяюе'
consonants = 'бвгджзйклмнпрстфхцчшщ'
count_vowels = 0
count_consonants = 0

for i in range (len (s)):
    if s[i].lower () in vowels:
        count_vowels += 1
    if s[i].lower () in consonants:
        count_consonants += 1

print (f"Количество гласных букв равно {count_vowels}")
print (f"Количество согласных букв равно {count_consonants}")
