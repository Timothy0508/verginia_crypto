import numpy as np

CHAR_DICT = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}


def encodeString(input: str) -> list[int]:
    code = []
    for char in input:
        code.append(CHAR_DICT[char])
    return code


def generateCodeMap(offset: str) -> np.ndarray:
    offest_encoded = encodeString(offset)
    base = offest_encoded
    for i in range(26):
        if (i + 1) not in base:
            base.append(i + 1)
    map = []
    for _ in range(26):
        map.append(base)
        first = base[0]
        base = base[1:]
        base.append(first)
    code_map = np.array(map)
    return code_map


def main():
    print("Hello from verginia-crypto!")
    print(generateCodeMap("ikhjg"))


if __name__ == "__main__":
    main()
