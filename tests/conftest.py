from typing import Literal

import pytest

# Fixtures for `add`
@pytest.fixture
def valid_integers() -> tuple[Literal[5], Literal[3]]:
    return 5, 3

@pytest.fixture
def invalid_integer_a() -> tuple[Literal['5'], Literal[3]]:
    return "5", 3  # a is invalid (string)

@pytest.fixture
def invalid_integer_b() -> tuple[Literal[5], Literal['3']]:
    return 5, "3"  # b is invalid (string)


# Fixtures for `reverse_string`
@pytest.fixture
def valid_string() -> Literal['taiwo']:
    return "taiwo"

@pytest.fixture
def invalid_non_string() -> Literal[123]:
    return 123  # Not a string


# Fixtures for `divide`
@pytest.fixture
def valid_division_pair() -> tuple[Literal[10], Literal[2]]:
    return 10, 2

@pytest.fixture
def division_by_zero() -> tuple[Literal[10], Literal[0]]:
    return 10, 0

@pytest.fixture
def invalid_division_a() -> tuple[Literal['10'], Literal[2]]:
    return "10", 2

@pytest.fixture
def invalid_division_b() -> tuple[Literal[10], Literal['2']]:
    return 10, "2"


# Fixtures for `is_palindrome`
@pytest.fixture
def palindrome_string() -> Literal['madam']:
    return "madam"

@pytest.fixture
def non_palindrome_string() -> Literal['hello']:
    return "hello"

@pytest.fixture
def invalid_palindrome_input() -> Literal[123]:
    return 123  # Not a string


# Fixtures for `count_words`
@pytest.fixture
def sentence_with_words() -> Literal['Hello world this is a test']:
    return "Hello world this is a test"

@pytest.fixture
def empty_text() -> Literal['']:
    return ""

@pytest.fixture
def invalid_count_input() -> Literal[42]:
    return 42  # Not a string