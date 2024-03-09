#!/usr/bin/python3
import sys
"""print_stats"""


def print_stats(total_size, status_codes):
    """Prints statistics based on the provided total size and status codes."""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        print("{}: {}".format(status_code, status_codes[status_code]))


def parse_line(line):
    """Parses a line from the input and returns IP address, status code, and file size."""
    parts = line.split()
    return parts[0], int(parts[-2]), int(parts[-1])


def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            ip, status_code, file_size = parse_line(line)
            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
