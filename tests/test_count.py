

import pytest
from main import count_words




def test_count_sentence_with_words(sentence_with_words):
    outcome = len(sentence_with_words.split())
    assert count_words(sentence_with_words) == outcome


def test_count_empty_sentence(empty_text):
    outcome = len(empty_text.split())
    assert count_words(empty_text) == outcome


def test_count_invalid_srt_type(invalid_count_input):
    with pytest.raises(TypeError) as exc:
        count_words(invalid_count_input)
    assert str(exc.value) == "text must be a string"