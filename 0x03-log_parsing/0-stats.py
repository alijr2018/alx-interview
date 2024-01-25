#!/usr/bin/python3
"""
0-stats.py
"""
import sys
import signal
from collections import defaultdict


def print_statistics(total_size, status_counts):
    """
    a formatting and printing the computed statistics
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


def main():
    """
    script that reads stdin line by line and computes metrics
    """
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            try:
                parts = line.split()
                ip_address = parts[0]
                status_code = int(parts[-2])
                file_size = int(parts[-1])
            except (IndexError, ValueError):
                continue

            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        pass

    print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
