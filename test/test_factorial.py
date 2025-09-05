import pytest

from func.factorial import factorial


@pytest.mark.parametrize("num_1, result", [
    (1, 1),
    (0, 1),
    (5, 120),
    (10, 3628800),
])
def test_factorial(num_1, result):
    assert factorial(num_1) == result
