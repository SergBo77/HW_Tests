def count_vowels(s):
    vowels = 'аеёиоуыэюя'  # Все гласные буквы русского алфавита
    count = 0
    for char in s.lower():  # Проверяем каждую букву в исходной строке
        if char in vowels:
            count += 1
    return count