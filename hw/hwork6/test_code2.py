import pytest
from code import AverageCalculator

"""Каждый тест проверяет разные сценарии использования программы, 
чтобы убедиться, что она работает правильно в различных ситуациях.
list1 = [1, 2, 3, 4, 5], list2 = [6, 7, 8, 9, 10]:
Ожидается, что второй список имеет большее среднее значение.
list1 = [1, 2, 3, 4, 5], list2 = [1, 2, 3, 4, 5]:
Ожидается, что средние значения равны.
list1 = [], list2 = []:
Ожидается, что средние значения равны (оба списка пусты).
list1 = [], list2 = [6, 7, 8, 9, 10]:
Ожидается, что второй список имеет большее среднее значение (первый список пуст).
list1 = [1, 2, 3, 4, 5], list2 = []:
Ожидается, что первый список имеет большее среднее значение (второй список пуст)."""

test_data = [
    ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], "The second list has a higher average value"),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "The average values"),
    ([], [], "The average values"),
    ([], [6, 7, 8, 9, 10], "The second list has a higher average value"),
    ([1, 2, 3, 4, 5], [], "The first list has a higher average value")
]


@pytest.mark.parametrize('list1, list2, expected_result', test_data)
def test_compare_averages(list1, list2, expected_result):
    calculator = AverageCalculator(list1, list2)
    result = calculator.compare_averages()
    assert result == expected_result, f'Test failed: list1={list1}, list2={list2}'


if __name__ == "__main__":
    pytest.main(['-v'])
