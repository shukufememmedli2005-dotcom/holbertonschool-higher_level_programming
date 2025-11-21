#!/usr/bin/env python3
from sys import argv, stderr, exit

def main():
    try:
        total = sum(int(s) for s in argv[1:])
    except ValueError:
        print("Error: all arguments must be integers", file=stderr)
        exit(1)
    print(total)

if __name__ == "__main__":
    main()
