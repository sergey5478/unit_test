"""Напишите тесты, покрывающие на 100% метод is_odd,
который проверяет, является ли переданное число четным или нечетным."""


def is_odd(random_number):
    """Функция проверки на чётность."""
    return random_number % 2 == 0


def test_is_odd():
    """Странные тесты))."""
    assert is_odd(3) == True  # Нечетное число
    assert is_odd(4) == False  # Четное число
    assert is_odd(0) == False  # Ноль, считается четным
    assert is_odd(-5) == True  # Отрицательное нечетное число
    assert is_odd(-6) == False  # Отрицательное четное число
    assert is_odd(1000001) == True  # Большое нечетное число
    assert is_odd(-1000000) == False  # Большое четное число


if __name__ == '__main__':
    test_is_odd()
