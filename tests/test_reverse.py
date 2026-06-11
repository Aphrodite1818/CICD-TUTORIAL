from main import reverse_string

import pytest


def test_reverse_valid_string(valid_string):
    result = reverse_string(valid_string)
    assert result == "owiat"




def test_reverse_invalid_string(invalid_non_string):
    with pytest.raises(TypeError) as exc:
        result = reverse_string(invalid_non_string)
    assert str(exc.value) == "Type must be a valid string"
    


@pytest.mark.parametrize("string , outcome" ,(
    [("hello" ,"olleh"),
    ("underpants" , "stnaprednu"),
    (123 , TypeError)
    ]
))
def test_multiple_strings(string , outcome):
    if outcome is TypeError:
        with pytest.raises(TypeError) as out:
            reverse_string(string)
        assert str(out.value) == "Type must be a valid string"
    else:
        assert reverse_string(string) == outcome
