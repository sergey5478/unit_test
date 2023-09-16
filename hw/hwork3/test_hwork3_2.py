import unittest
from hwork3_2 import number_interval


class TestNumberInInterval(unittest.TestCase):
    """Тест функции number_interval"""
    def test_number_in_interval_positive(self):
        """Число внутри интервала."""
        self.assertTrue(number_interval(50))

    def test_number_in_interval_negative_low(self):
        """Число ниже нижней границы."""
        self.assertFalse(number_interval(10))

    def test_number_in_interval_negative_high(self):
        """Число выше верхней границы."""
        self.assertFalse(number_interval(150))

    def test_number_in_interval_edge_low(self):
        """Число равно нижней границе."""
        self.assertFalse(number_interval(25))

    def test_number_in_interval_edge_high(self):
        """Число равно верхней границе."""
        self.assertFalse(number_interval(100))


if __name__ == '__main__':
    unittest.main()
