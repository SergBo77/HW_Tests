import unittest

from main import add, subtract, multiply, divide, check, divide_chek

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertNotEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)

class TestCheck(unittest.TestCase):
    def testcheck(self):
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertTrue(check(220))

        self.assertFalse(check(3))
        self.assertFalse(check(57))

class TestDivide(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)


class TestDivide_Chek(unittest.TestCase):
    def testdivide_chek(self):
        self.assertEqual(divide_chek(10, 3), 1)
        self.assertEqual(divide_chek(10, 4), 2)
        self.assertEqual(divide_chek(29, 5), 4)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide_chek, 10, 0)


if __name__ == '__main__':
		unittest.main()