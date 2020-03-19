import numpy
import sys
from typing import List

MU: int = 130  # Mean
SIGMA: int = 25  # Standard Deviation


def delay() -> None:
    """Write a delay with a random time to STDOUT."""
    print("DELAY " + str(int(numpy.random.normal(MU, SIGMA))))


def get_lines(filename: str) -> List[str]:
    """Return a list of lines for the file at the given filename."""
    try:
        f = open(filename, "r")
        return f.read().splitlines()
    except IOError:
        return
    finally:
        f.close()


def intertype(line: str) -> None:
    """Writes a String to STDOUT, character-by-character, with a delay in-between."""
    for char in line:
        if char == " ":
            print("SPACE")
        else:
            print("STRING " + char)
        delay()


def main(filename: str) -> None:
    """Takes in a Ducky Script file. Adds a random DELAY in-between characters. Writes output to STDOUT."""
    for line in get_lines(filename):
        if line[:6] == "STRING":
            intertype(line[7:])
        elif line[:3] == "TAB":
            print(line)
            delay()
        else:
            print(line)


if __name__ == "__main__" and len(sys.argv) == 2:
    main(sys.argv[1])
