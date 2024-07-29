import pytest
from pydef import count_vowels


@pytest.mark.parametrize("text, expected", [
   ("Как дела?", 3),
   ("мтпрнкфс", 0),
   ("1234567890", 0),
   ("АЕЁИОУЫЭЮЯ", 10),
   ("аеёОУуыэюя", 10)
])

def test_count_vowels1(text, expected):
   assert count_vowels(text) == expected