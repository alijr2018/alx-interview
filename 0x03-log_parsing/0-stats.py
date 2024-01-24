#!/usr/bin/python3
"""
0-stats.py
"""
import sys
import signal
from collections import defaultdict


status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
total_file_size = 0
status_code_count = {code: 0 for code in status_codes}
line_count = 0


def print_statistics():
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 10 or parts[8] != "\"GET" or not parts[9].startswith("/projects/"):
            continue

        file_size = int(parts[9 + 1])
        status_code = int(parts[9 - 1])

        total_file_size += file_size
        status_code_count[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
