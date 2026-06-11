def add_numbers(a: int, b: int) -> int:
    if not isinstance(a, int):
        raise TypeError("a must be an integer")

    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b




def reverse_string(text : str):
    if not isinstance(text, str):
        raise TypeError("Type must be a valid string")
    return text[::-1]





def divide(a: float, b: float) -> float:
    if not isinstance(a, (int, float)):
        raise TypeError("a must be a number")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be a number")

    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")

    return a / b




def is_palindrome(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = text.lower()

    return cleaned == cleaned[::-1]




def count_words(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return len(text.split())


def say_hello():
    return "say hello , welcome to python"