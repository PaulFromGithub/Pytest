import pytest

from func.calculator import Calculator


class TestCalculator:
    @pytest.mark.parametrize("x, y, result",
        [
        (2, 3, 5),
        (10, 100, 110),
        (-1, 2, 1),
        (5, "5", 25),
        ]
    )
    def test_add(self, x, y, result):
        assert Calculator().add(x, y) == result

    @pytest.mark.parametrize("x, y, result",
        [
        (2, 3, 6),
        (10, 100, 1000),
        (-1, 2, -2),
        ]
    )
    def test_multiply(self, x, y, result):
        assert Calculator().multiply(x, y) == result