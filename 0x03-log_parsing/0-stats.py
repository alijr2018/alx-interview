#!/usr/bin/python3
"""
0-stats.py
"""
import sys
import signal
from collections import defaultdict


def print_statistics(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")


def main():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            p = line.split()

            if len(p) == 9 and p[2] == "GET" and p[5:7].isdigit():
                status_code = int(p[7])
                file_size = int(p[8])

                total_size += file_size
                status_codes[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    print_statistics(total_size, status_codes)


if __name__ == "__main__":
    main()
