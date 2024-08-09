import unittest

from main import add, subtract, multiply, divide, check, divide_chek

# Класс для тестирования математических функций
class TestMath(unittest.TestCase):
    # Тестирование функции сложения
    def test_add(self):
        # Проверяем, что 2 + 5 равно 7
        self.assertEqual(add(2, 5), 7)
        # Проверяем, что 3 + 7 не равно 9
        self.assertNotEqual(add(3, 7), 9)

    # Тестирование функции вычитания
    def test_subtract(self):
        # Проверяем, что 7 - 4 равно 3
        self.assertEqual(subtract(7, 4), 3)
        # Проверяем, что 4 - 2 не равно 1
        self.assertNotEqual(subtract(4, 2), 1)

    # Тестирование функции умножения
    def test_multiply(self):
        # Проверяем, что 2 * 5 не равно 12
        self.assertNotEqual(multiply(2, 5), 12)
        # Проверяем, что 3 * 6 равно 18
        self.assertEqual(multiply(3, 6), 18)

    # Тестирование функции деления
    def test_divide(self):
        # Проверяем, что 4 / 2 не равно 3
        self.assertNotEqual(divide(4, 2), 3)
        # Проверяем, что 20 / 5 равно 4
        self.assertEqual(divide(20, 5), 4)

# Класс для тестирования функции check
class TestCheck(unittest.TestCase):
    # Тестирование функции check
    def testcheck(self):
        # Проверяем, что 2, 6 и 220 возвращают True
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertTrue(check(220))

        # Проверяем, что 3 и 57 возвращают False
        self.assertFalse(check(3))
        self.assertFalse(check(57))

# Класс для тестирования функции деления
class TestDivide(unittest.TestCase):
    # Тестирование успешного деления
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)  # 10 / 2 равно 5
        self.assertEqual(divide(6, 3), 2)    # 6 / 3 равно 2
        self.assertEqual(divide(70, 2), 35)  # 70 / 2 равно 35

# Класс для тестирования функции divide_chek
class TestDivide_Chek(unittest.TestCase):
    # Тестирование функции divide_chek
    def testdivide_chek(self):
        self.assertEqual(divide_chek(10, 3), 1)  # 10 // 3 равно 1
        self.assertEqual(divide_chek(10, 4), 2)  # 10 // 4 равно 2
        self.assertEqual(divide_chek(29, 5), 4)  # 29 // 5 равно 4

    # Тестирование деления на ноль
    def test_divide_by_zero(self):
        # Проверяем, что при делении на 0 возникает ValueError
        self.assertRaises(ValueError, divide_chek, 10, 0)

# # Запуск тестов, если этот файл запускается как основной
if __name__ == '__main__':
    unittest.main()