from .. import main


def test_encode_string():
    input_str = "hello"
    expected_output = [7, 4, 11, 11, 14]  # Assuming 'h' -> 7, 'e' -> 4, etc.
    assert main.encodeString(input_str) == expected_output
