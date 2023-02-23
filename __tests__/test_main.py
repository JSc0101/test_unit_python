import pytest
from src.main import sum, is_greater_than, login


def test_sum():
    assert sum(2, 5) == 7


def test_is_greater_than():
    assert is_greater_than(10, 9)


@pytest.mark.parametrize("input_x, input_y, expected", [
    (2, 5, 7),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5)
])
def test_param_sum(input_x, input_y, expected):
    assert sum(input_x, input_y) == expected

def test_login_user_pass():
    result__login = login("sebastian", "sebastian123")
    assert result__login


def test_login_user_fail():
    result_login = login("johan", "johan123")
    assert not result_login