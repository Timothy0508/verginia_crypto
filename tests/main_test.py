from .. import main
import numpy as np


def test_encode_string():
    input_str = "hello"
    expected_output = [7, 4, 11, 11, 14]  # Assuming 'h' -> 7, 'e' -> 4, etc.
    assert main.encodeString(input_str) == expected_output


def test_decode_string():
    input_array = [7, 4, 11, 11, 14]  # Corresponds to "hello"
    expected_output = "hello"
    assert main.decode_string(np.array(input_array)) == expected_output
