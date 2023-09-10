class Calculator:
    def calculate_discount(self, total_amount, discount_percent):
        if not isinstance(total_amount, (int, float)) or not \
                isinstance(discount_percent, (int, float)):
            raise ValueError("Both total_amount and discount_percent must be numbers")
        if total_amount < 0 or discount_percent < 0 or discount_percent > 100:
            raise ValueError("Invalid values: total_amount and discount_percent"
                             " must be positive numbers, and discount_percent"
                             " must be between 0 and 100")
        discount_amount = total_amount * (discount_percent / 100)
        discounted_total = total_amount - discount_amount
        return discounted_total


calculator = Calculator()


def test_positive_discount():
    assert calculator.calculate_discount(100, 10), "Test Failed:"


def test_negative_total_amount():
    try:
        calculator.calculate_discount(-100, 10)
    except ValueError as e:
        assert str(e) == "Invalid values: total_amount and discount_percent" \
                         " must be positive numbers, and discount_percent must" \
                         " be between 0 and 100"
        print(f"{e}")


def test_negative_discount():
    try:
        calculator.calculate_discount(100, -10)
    except ValueError as e:
        assert str(e) == "Invalid values: total_amount and discount_percent" \
                         " must be positive numbers, and discount_percent must" \
                         " be between 0 and 100"
        print(f"{e}")


def test_discount_above_100():
    try:
        calculator.calculate_discount(100, 110)
    except ValueError as e:
        assert str(e) == "Invalid values: total_amount and discount_percent" \
                         " must be positive numbers, and discount_percent must" \
                         " be between 0 and 100"
        print(f"{e}")


def test_invalid_types():
    try:
        calculator.calculate_discount("100", 10)
    except ValueError as e:
        assert str(e) == "Both total_amount and discount_percent must be numbers"
        print(f"{e}")


if __name__ == '__main__':
    test_positive_discount()
    test_negative_total_amount()
    test_negative_discount()
    test_discount_above_100()
    test_invalid_types()
