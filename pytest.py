import pytest
from pydef import count_vowels

def test_count_vowels():
    assert count_vowels("Привет, Мир!") == 3  # гласные: и, е, и
    assert count_vowels("Как дела?") == 3  # гласные: а, е, а
    assert count_vowels("мтпрнкфс.") == 0  # гласные: е, о, е
    assert count_vowels("1234567890") == 0  # Нет гласных
    assert count_vowels("") == 0  # Пустая строка
    assert count_vowels("АЕЁИОУЫЭЮЯ") == 10  # Все гласные в верхнем регистре
    assert count_vowels("аеёОУуыэюя") == 10  # Все гласные в нижнем регистре