#!/usr/bin/python3
from sys import argv


def main():
    count = len(argv) - 1

    if count == 0:
        print("0 arguments.")
        return

    if count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    for i in range(1, count + 1):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
