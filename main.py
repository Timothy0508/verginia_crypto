import numpy as np

CHAR_DICT = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
}


def encodeString(input: str) -> list[int]:
    code = []
    for char in input:
        code.append(CHAR_DICT[char])
    return code


def decode_string(input: np.ndarray) -> str:
    reversed_dict = {value: key for key, value in CHAR_DICT.items()}
    text = ""
    for char in input.tolist():
        text += reversed_dict[char]
    return text


def generateCodeMap(offset: str) -> np.ndarray:
    offest_encoded = encodeString(offset)
    base = offest_encoded
    for i in range(26):
        if i not in base:
            base.append(i)
    map = []
    for _ in range(26):
        map.append(base)
        first = base[0]
        base = base[1:]
        base.append(first)
    code_map = np.array(map)
    return code_map


def encrypt_string(offset: str, key: str, msg: str):
    code_map = generateCodeMap(offset)
    encoded_key = encodeString(key)
    encoded_msg = encodeString(msg)
    result = []

    for i in range(len(encoded_msg)):
        result.append(code_map[encoded_key[i % len(encoded_key)], encoded_msg[i]])

    text = decode_string(np.array(result))
    print(text)


def main():
    print("Hello from verginia-crypto!")
    offset = input("Offest: ")
    key = input("Key: ")
    msg = input("Message: ")
    encrypt_string(offset, key, msg)


if __name__ == "__main__":
    main()
