#!/usr/bin/env python3

from typing import List
import base64

# String > Reversed > Charcode > Sub 20 > String 7digit > utf-8 > base64

def encode_stage1(string: str) -> str:
    return string[::-1]

def encode_stage2(string: str) -> List[int]:
    return [ord(char) for char in string]

def encode_stage3(chars: List[int]) -> List[int]:
    return [num - 20 for num in chars]

def encode_stage4(chars: List[int]) -> str:
    return "".join([f"{num:07d}" for num in chars])

def encode_stage5(string: str) -> bytes:
    return string.encode("utf-8")

def encode_stage6(b: bytes) -> bytes:
    return base64.b64encode(b)

def encode_stage7(b: bytes) -> str:
    return b.decode("utf-8")


def encode_string(string: str) -> str:
    return encode_stage7(encode_stage6(encode_stage5(encode_stage4(encode_stage3(encode_stage2(encode_stage1(string)))))))


def main():
    stage1 = encode_string("BSU{0bfu5c4t10n_15_4w350m3}")
    print(encode_string(stage1))


if __name__ == "__main__":
    main()
