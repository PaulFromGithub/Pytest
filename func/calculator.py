class Calculator:
    @staticmethod
    def add(number_1, number_2):
        if not isinstance(number_1, (int, float)) or not isinstance(number_2, (int, float)):
            raise TypeError ("Нужны числа")
        return number_1 + number_2

    @staticmethod
    def multiply(number_1, number_2):
        if not isinstance(number_1, (int, float)) or not isinstance(number_2, (int, float)):
            raise TypeError ("Нужны числа")
        return number_1 * number_2