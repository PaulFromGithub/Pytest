import pytest

from func.cel_to_fahr import celsius_to_fahrenheit


@pytest.mark.parametrize("cel, result_fahr", [
    (7, 44.6),
    (1, 33.8),
    (10, 50),
    (-3, 26.6),
])
def test_celsius_to_fahrenheit(cel, result_fahr):
    assert celsius_to_fahrenheit(cel) == result_fahr