#!/usr/bin/python3
"""
Log parsing
"""
import sys


total_size = 0
status_codes = {}

try:
    for i, line in enumerate(sys.stdin, start=1):
        parts = line.split()
        if len(parts) >= 8:
            ip_address, _, _, date, _, _, status_code_str, file_size_str = parts[:8]

            try:
                status_code = int(status_code_str)
                file_size = int(file_size_str)
                total_size += file_size

                if 200 <= status_code <= 500:
                    status_codes[status_code] = status_codes.get(status_code, 0) + 1

                if i % 10 == 0:
                    print(f"File size: {total_size}")
                    for code in sorted(status_codes):
                        print(f"{code}: {status_codes[code]}")

            except ValueError:
                pass

except KeyboardInterrupt:
    pass

print(f"File size: {total_size}")
for code in sorted(status_codes):
    print(f"{code}: {status_codes[code]}")
