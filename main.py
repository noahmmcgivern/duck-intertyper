#!/usr/bin/env python3
import numpy
from random import randint
import sys

MU: int = 130
SIGMA: int = 25

def delay() -> None:
    print("DELAY " + str(int(numpy.random.normal(MU, SIGMA))))

def get_lines(filename: str):
    try:
        f = open(filename, "r")
        return f.read().splitlines()
    except IOError:
        return
    finally:
        f.close()

def intertype(line: str) -> None:
    for char in line[7:]:
        if char == " ":
            print("SPACE")
        else:
            print("STRING " + char)
        delay()

def main(filename: str) -> None:
    for line in get_lines(filename):
        if line[:6] == "STRING":
            intertype(line)
        elif line[:3] == "TAB":
            print(line)
            delay()
        else:
            print(line)

if __name__ == "__main__" and len(sys.argv) == 2: main(sys.argv[1])
