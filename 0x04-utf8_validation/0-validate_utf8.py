#!/usr/bin/python3
"""
0-validate_utf8.py
"""


def validUTF8(data):
    """
    determines if a given data set represents a,
    valid UTF-8 encoding.
    """

    def is_start_byte(byte):
        return (byte & 0b10000000) == 0b00000000

    def is_continuation_byte(byte):
        return (byte & 0b11000000) == 0b10000000

    remaining_continuation_bytes = 0

    for byte in data:
        if remaining_continuation_bytes > 0:
            if not is_continuation_byte(byte):
                return False
            remaining_continuation_bytes -= 1
        else:
            if byte & 0b10000000 == 0b00000000:
                remaining_continuation_bytes = 0
            elif byte & 0b11100000 == 0b11000000:
                remaining_continuation_bytes = 1
            elif byte & 0b11110000 == 0b11100000:
                remaining_continuation_bytes = 2
            elif byte & 0b11111000 == 0b11110000:
                remaining_continuation_bytes = 3
            else:
                return False

    return remaining_continuation_bytes == 0
