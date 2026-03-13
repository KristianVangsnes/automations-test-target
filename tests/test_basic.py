import pytest

from src.app import process_data


def test_process_data():
    assert process_data([1, 2, 3]) == [2, 4, 6]


def test_convert_value_numeric_string():
    from src.converter import convert_value

    assert convert_value("42") == 42


def test_convert_value_non_numeric_raises_descriptive_error():
    from src.converter import convert_value

    with pytest.raises(ValueError, match="Invalid integer input"):
        convert_value("hello")
