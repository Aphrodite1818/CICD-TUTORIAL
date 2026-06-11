import pytest
from main import divide





def test_valid_division_pair(valid_division_pair):
    assert divide(valid_division_pair[0] , valid_division_pair[1]) == 5


def test_invalid_division_pair_a(invalid_division_a):
    with pytest.raises(TypeError) as exc:
        result = divide(invalid_division_a[0] , invalid_division_a[1])

    assert str(exc.value)  == "a must be a number"




def test_invalid_division_pair_b(invalid_division_b):
    with pytest.raises(TypeError) as exc:
        result = divide(invalid_division_b[0] , invalid_division_b[1])

    assert str(exc.value)  == "b must be a number"



def test_division_by_zero(division_by_zero):
    with pytest.raises(ZeroDivisionError) as exc:
        divide(division_by_zero[0] , division_by_zero[1])
    assert str(exc.value) == "cannot divide by zero"