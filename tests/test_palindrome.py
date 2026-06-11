from main import is_palindrome
import pytest


def test_is_palindrome(palindrome_string):
    assert is_palindrome(palindrome_string) == True



def test_is_not_palindrome(non_palindrome_string):
    assert is_palindrome(non_palindrome_string) == False


def test_invalid_palindrome_input(invalid_palindrome_input):
    with pytest.raises(TypeError) as exc:
        is_palindrome(invalid_palindrome_input)
    assert str(exc.value) == "text must be a string"