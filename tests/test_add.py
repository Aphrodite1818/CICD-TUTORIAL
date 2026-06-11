

from main import add_numbers
import pytest



def test_add_numbers(valid_integers) -> None:
    result = add_numbers(valid_integers[0] ,valid_integers[1])

    assert result == 8


def test_add_invalid_numbers_a(invalid_integer_a) -> None:
    with pytest.raises(TypeError) as exc:
        result = add_numbers(invalid_integer_a[0] , invalid_integer_a[1])
    assert str(exc.value) == "a must be an integer"




def test_add_invalid_numbers_b(invalid_integer_b) -> None:
    with pytest.raises(TypeError) as exc:
        result = add_numbers(invalid_integer_b[0] , invalid_integer_b[1])
    assert str(exc.value) == "b must be an integer"


