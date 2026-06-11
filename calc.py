#!/usr/bin/env python3
"""A simple CLI calculator that supports basic arithmetic operations."""

import sys


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def main():
    if len(sys.argv) != 4:
        print("Usage: python calc.py <num1> <operator> <num2>")
        print("Operators: +  -  *  /")
        print("Example: python calc.py 10 + 5")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        op = sys.argv[2]
        b = float(sys.argv[3])
    except ValueError:
        print("Error: Invalid number")
        sys.exit(1)

    if op not in OPERATIONS:
        print(f"Error: Unknown operator '{op}'. Use: + - * /")
        sys.exit(1)

    try:
        result = OPERATIONS[op](a, b)
        print(f"{a} {op} {b} = {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
