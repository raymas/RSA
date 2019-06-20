#!/usr/bin/env python3

import time
import math
import matplotlib.pyplot as plt


def extended_gcd(x, y):
    if y == 0:
        return (1, 0)
    else:
        (u, v) = extended_gcd(y, pow(x, 1, y))
        return (v, u - (x // y) * v)


def extended_gcd2(x, y):
    (u0, v0, u1, v1) = (1, 0, 0, 1)
    while y:
        (q, r) = divmod(x, y)
        (x, y) = (y, x)
        (u0, v0, u1, v1) = (u1, v1, u0-q*u1, v0-q*v1)
        return (u0, v0)


if __name__ == "__main__":
    startGCD = "%.20f" % time.time()
    extended_gcd()
    finalTimeGCD = float("%.20f" % time.time()) - float(startGCD)

    startGCD2 = "%.20f" % time.time()
    extended_gcd2()
    finalTimeGCD2 = float("%.20f" % time.time()) - float(startGCD2)

    plt.plot()
