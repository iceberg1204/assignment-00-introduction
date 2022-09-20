"""
Задача: написать функцию для сложения двух дробей, заданных числителями и знаменателями.

Результат работы функции (x, y) должен удовлетворять свойствам:
1. a/b + c/d = x/y
2. x/y несократима
3. y >= 0

Можно считать, что передаваемые в функцию b и d всегда ненулевые.
"""
from math import gcd


def least_common_multiple(a, b):
    lcm = abs(a * b) // gcd(a, b)

    return lcm


def add_fractions(a, b, c, d):
    y = least_common_multiple(b, d)
    x = (a * (y // b)) + (c * (y // d))

    return x // gcd(x, y), y // gcd(x, y)
