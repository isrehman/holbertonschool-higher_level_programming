#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print(sum(int(argv[i]) for i in range(1, len(argv))))
