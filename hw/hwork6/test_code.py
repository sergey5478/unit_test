from code import AverageCalculator


def test_compare_averages():
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]

    calculator = AverageCalculator(list1, list2)
    result = calculator.compare_averages()

    assert result == "The second list has a higher average value"


def test_compare_averages_equal():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]

    calculator = AverageCalculator(list1, list2)
    result = calculator.compare_averages()

    assert result == "The average values"


def test_compare_averages_empty_lists():
    list1 = []
    list2 = []

    calculator = AverageCalculator(list1, list2)
    result = calculator.compare_averages()

    assert result == "The average values"


def test_compare_averages_list1_empty():
    list1 = []
    list2 = [6, 7, 8, 9, 10]

    calculator = AverageCalculator(list1, list2)
    result = calculator.compare_averages()

    assert result == "The second list has a higher average value"


def test_compare_averages_list2_empty():
    list1 = [1, 2, 3, 4, 5]
    list2 = []

    calculator = AverageCalculator(list1, list2)
    result = calculator.compare_averages()

    assert result == "The first list has a higher average value"
