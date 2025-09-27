import pytest
from contextlib import nullcontext as not_raise

from func.calculator import Calculator


class TestCalculator:
    @pytest.mark.parametrize("x, y, result, expectation",
        [
        (2, 3, 5, not_raise()),
        (10, 100, 110, not_raise()),
        (-1, 2, 1, not_raise()),
        (5, "5", 25, pytest.raises(TypeError)),
        ]
    )
    def test_add(self, x, y, result, expectation ):
        with expectation:
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