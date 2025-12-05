"""
simple_calculator.py

A minimal interactive calculator that accepts user input for two numbers
and an operation. Supports: +, -, *, /, %, ^ (power).
Type "exit" or "q" to quit.

Usage: Run the script and follow prompts.
"""

import math
import sys

SUPPORTED_OPS = {
    '+': 'add',
    '-': 'subtract',
    '*': 'multiply',
    '/': 'divide',
    '%': 'modulus',
    '^': 'power'
}


def parse_number(s):
    """Try to parse input into int or float. Raise ValueError on failure."""
    s = s.strip()
    if s.lower() in ('exit', 'q'):
        raise EOFError()
    # Allow underscores like Python numeric literals
    try:
        if '.' in s or 'e' in s or 'E' in s:
            return float(s)
        return int(s)
    except ValueError:
        # last resort: try float conversion for inputs like '3.0'
        try:
            return float(s)
        except ValueError:
            raise ValueError(f"Invalid number: {s}")


def calculate(a, b, op):
    """Perform calculation and return result or raise an error for invalid ops."""
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if b == 0:
            raise ZeroDivisionError('Division by zero')
        return a / b
    if op == '%':
        if b == 0:
            raise ZeroDivisionError('Modulo by zero')
        return a % b
    if op == '^':
        return a ** b
    raise ValueError(f"Unsupported operation: {op}")


def pretty(x):
    """Return an int-like number without a trailing .0 when appropriate."""
    if isinstance(x, float):
        if x.is_integer():
            return int(x)
    return x


def prompt(msg):
    try:
        return input(msg)
    except (EOFError, KeyboardInterrupt):
        print('\nExiting.')
        sys.exit(0)


def main():
    print('Simple Calculator — enter numbers and an operation. Type "exit" or "q" to quit.')
    print('Supported operations: ' + ' '.join(SUPPORTED_OPS.keys()))

    while True:
        try:
            s1 = prompt('\nEnter first number: ')
            if s1.strip().lower() in ('exit', 'q'):
                break
            a = parse_number(s1)

            s_op = prompt('Enter operation (e.g. +, -, *, /, %, ^): ')
            if s_op.strip().lower() in ('exit', 'q'):
                break
            op = s_op.strip()
            if op not in SUPPORTED_OPS:
                print(f"Unsupported operation: {op}. Try one of: {', '.join(SUPPORTED_OPS.keys())}")
                continue

            s2 = prompt('Enter second number: ')
            if s2.strip().lower() in ('exit', 'q'):
                break
            b = parse_number(s2)

            try:
                result = calculate(a, b, op)
            except ZeroDivisionError as zde:
                print('Error:', zde)
                continue

            print(f'Result: {pretty(result)}')

        except ValueError as ve:
            print('Input error:', ve)
            continue
        except EOFError:
            # user typed exit in parse_number
            break

    print('Goodbye!')


if __name__ == '__main__':
    main()
