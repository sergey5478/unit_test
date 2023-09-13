import unittest

from task_11 import Car, Motorcycle, Vehicle


class TestVehicle(unittest.TestCase):
    """Клас тестирования"""

    def test_car_is_instance_of_vehicle(self):
        """Проверка, что объект Car также является экземпляром Vehicle"""
        car = Car("Toyota", "Camry", 2022)
        self.assertIsInstance(car, Vehicle)

    def test_car_has_4_wheels(self):
        """Проверка количества колёс"""
        car = Car("Toyota", "Camry", 2022)
        self.assertEqual(car.num_wheels, 4)

    def test_motorcycle_has_2_wheels(self):
        """Проверка, что объект Motorcycle создаётся с 2-мя колёсами"""
        motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021)
        self.assertEqual(motorcycle.num_wheels, 2)

    def test_car_speed_after_test_drive(self):
        """Проверка развития скорости в режиме тестовой поездки"""
        car = Car("Toyota", "Camry", 2022)
        car.test_drive()
        self.assertEqual(car.speed, 60)

    def test_motorcycle_speed_after_test_drive(self):
        """Проверка развития скорости в режиме тестовой поездки"""
        motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021)
        motorcycle.test_drive()
        self.assertEqual(motorcycle.speed, 75)

    def test_car_speed_after_park(self):
        """Проверка остановки в режиме парковки"""
        car = Car("Toyota", "Camry", 2022)
        car.test_drive()
        car.park()
        self.assertEqual(car.speed, 0)

    def test_motorcycle_speed_after_park(self):
        """Проверка остановки в режиме парковки"""
        motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021)
        motorcycle.test_drive()
        motorcycle.park()
        self.assertEqual(motorcycle.speed, 0)


if __name__ == '__main__':
    unittest.main()
