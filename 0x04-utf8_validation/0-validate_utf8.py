#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check for valid UTF-8 encoding
    """
    def get_num_bytes(byte):
        """
        get the bytes
        """
        if byte & 0x80 == 0:
            return 1
        elif byte & 0xE0 == 0xC0:
            return 2
        elif byte & 0xF0 == 0xE0:
            return 3
        elif byte & 0xF8 == 0xF0:
            return 4
        else:
            return -1

    i = 0
    while i < len(data):
        num_bytes = get_num_bytes(data[i])

        if num_bytes == -1:
            return False

        if i + num_bytes > len(data):
            return False

        for j in range(1, num_bytes):
            if data[i + j] & 0xC0 != 0x80:
                return False

        i += num_bytes

    return True
