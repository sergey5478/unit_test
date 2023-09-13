"""*Задание 1.
Проект Vehicle. Написать следующие тесты с использованием abs:
- Проверить, что экземпляр объекта Car также является экземпляром
транспортного средства (используя оператор instanceof).
- Проверить, что объект Car создается с 4-мя колесами.
- Проверить, что объект Motorcycle создается с 2-мя колесами.
- Проверить, что объект Car развивает скорость 60 в режиме тестового вождения
 (используя метод testDrive()).
- Проверить, что объект Motorcycle развивает скорость 75 в режиме тестового
вождения (используя метод testDrive()).
- Проверить, что в режиме парковки (сначала testDrive, потом park, т.е.
эмуляция движения транспорта) машина останавливается (speed = 0).
- Проверить, что в режиме парковки (сначала testDrive, потом park, т.е.
эмуляция движения транспорта) мотоцикл останавливается (speed = 0).
В этом проекте, вы будете работать с проектом ""Vehicle"", который представляет
 собой иерархию классов, включающую абстрактный базовый класс ""Vehicle"" и
 два его подкласса ""Car"" и ""Motorcycle"".
Базовый класс ""Vehicle"" содержит абстрактные методы ""testDrive()"" и ""park()"",
 а также поля ""company"", ""model"", ""yearRelease"", ""numWheels"" и ""speed"".
Класс ""Car"" расширяет ""Vehicle"" и реализует его абстрактные методы. При создании
объекта ""Car"", число колес устанавливается в 4, а скорость в 0. В методе
""testDrive()"" скорость устанавливается на 60, а в методе ""park()"" - обратно в 0.
Класс ""Motorcycle"" также расширяет ""Vehicle"" и реализует его абстрактные методы.
При создании объекта ""Motorcycle"", число колес устанавливается в 2, а скорость в 0.
В методе ""testDrive()"" скорость устанавливается на 75, а в методе ""park()"" - обратно в 0."""
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
