import unittest
from hwork3_1 import is_odd


class TestIsOdd(unittest.TestCase):
    """Тест функции is_odd."""
    def test_is_odd_positive_odd(self):
        """Нечетное положительное число."""
        self.assertTrue(is_odd(3))

    def test_is_odd_positive_even(self):
        """Четное положительное число"""
        self.assertFalse(is_odd(4))

    def test_is_odd_zero(self):
        """Ноль, считается четным."""
        self.assertFalse(is_odd(0))

    def test_is_odd_negative_odd(self):
        """Отрицательное нечетное число."""
        self.assertTrue(is_odd(-5))

    def test_is_odd_negative_even(self):
        """Отрицательное четное число."""
        self.assertFalse(is_odd(-6))

    def test_is_odd_large_positive_odd(self):
        """Большое нечетное положительное число."""
        self.assertTrue(is_odd(1000001))

    def test_is_odd_large_negative_even(self):
        """Большое четное отрицательное число."""
        self.assertFalse(is_odd(-1000000))


if __name__ == '__main__':
    unittest.main()
