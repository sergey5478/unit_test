from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Базовый абстрактный класс."""
    def __init__(self, company, model, year_release):
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = None
        self.speed = 0

    @abstractmethod
    def test_drive(self):
        """Абстрактный метод"""
        pass

    @abstractmethod
    def park(self):
        """Абстрактный метод"""
        pass


class Car(Vehicle):
    """Подкласс"""
    def __init__(self, company, model, year_release):
        super().__init__(company, model, year_release)
        self.num_wheels = 4
        self.speed = 0

    def test_drive(self):
        self.speed = 60

    def park(self):
        self.speed = 0


class Motorcycle(Vehicle):
    """Подкласс"""
    def __init__(self, company, model, year_release):
        super().__init__(company, model, year_release)
        self.num_wheels = 2
        self.speed = 0

    def test_drive(self):
        self.speed = 75

    def park(self):
        self.speed = 0


if __name__ == '__main__':
    # Проверка, что объект Car также является экземпляром Vehicle
    car = Car("Toyota", "Camry", 2022)
    print(isinstance(car, Vehicle))  # True

    # Проверка количества колёс
    print(car.num_wheels == 4)  # True

    # Проверка, что объект Motorcycle создаётся с 2-мя колёсами
    motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021)
    print(motorcycle.num_wheels == 2)  # True

    # Проверка развития скорости в режиме тестовой поездки
    car.test_drive()
    motorcycle.test_drive()
    print(car.speed == 60)  # True
    print(motorcycle.speed == 75)  # True

    # Проверка остановки в режиме парковки
    car.park()
    motorcycle.park()
    print(car.speed == 0)  # True
    print(motorcycle.speed == 0)  # True
