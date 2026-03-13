from src.app import process_data


def test_process_data():
    assert process_data([1, 2, 3]) == [2, 4, 6]


def test_convert_value_fails():
    """This test deliberately fails to give CI Fixer something to fix."""
    from src.converter import convert_value
    result = convert_value("hello")
    assert result == 42
