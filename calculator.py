import os
import sys


def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def divide(a, b):
    result = a / b
    return result


def percentage(part, whole):
    temp = 0
    return part / whole * 100
