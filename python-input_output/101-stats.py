#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import sys

total_size = 0
status_codes = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0


def print_stats():
    """Prints the statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        parts = line.split()
        try:
            total_size += int(parts[-1])
            code = parts[-2]
            if code in valid_codes:
                status_codes[code] = status_codes.get(code, 0) + 1
        except (IndexError, ValueError):
            pass
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
