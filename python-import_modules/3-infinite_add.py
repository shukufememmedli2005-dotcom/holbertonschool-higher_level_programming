#!/usr/bin/python3
from sys import argv


def main():
    total = 0
    for i in range(1, len(argv)):
        total += int(argv[i])
    print(total)


if __name__ == "__main__":
    main()
