#!/usr/bin/env python3
import sys
from math import isqrt

def factorize(n):
    if n < 2:
        return None
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

def process_file(fn):
    try:
        with open(fn, "r") as f:
            for line in f:
                n = int(line.strip())
                p, q = factorize(n)
                print(f"{n}={q}*{p}")
    except FileNotFoundError:
        print(f"Error {fn} not found")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factors <file>")
        sys.exit(1)
    filename = sys.argv[1]
    process_file(filename)
