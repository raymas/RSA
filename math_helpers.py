#!/usr/bin/env python3

import time
import math
import matplotlib.pyplot as plt


import numpy as np


def extended_gcd(x, y):
    """recursive"""
    if y == 0:
        return (1, 0)
    else:
        (u, v) = extended_gcd(y, pow(x, 1, y))
        return (v, u - (x // y) * v)


"""
def extended_gcd2(x, y):
    (u0, v0, u1, v1) = (1, 0, 0, 1)
    while y:
        (q, r) = divmod(x, y)
        (x, y) = (y, r)
        (u0, v0, u1, v1) = (u1, v1, u0-q*u1, v0-q*v1)
        return (u0, v0)
"""


def pgcde(a, b):
    """ pgcd étendu avec les 2 coefficients de bézout u et v
        Entrée : a, b entiers
        Sorties : r = pgcd(a,b) et u, v entiers tels que a*u + b*v = r
    """
    r, u, v = a, 1, 0
    rp, up, vp = b, 0, 1
    while rp != 0:
        q = r//rp
        rs, us, vs = r, u, v
        r, u, v = rp, up, vp
        rp, up, vp = (rs - q*rp), (us - q*up), (vs - q*vp)
    return (r, u, v)


if __name__ == "__main__":
    startGCD = "%.20f" % time.time()
    print(extended_gcd(120, 23))
    finalTimeGCD = float("%.20f" % time.time()) - float(startGCD)

    startGCD2 = "%.20f" % time.time()
    # print(extended_gcd2(120, 23))
    finalTimeGCD2 = float("%.20f" % time.time()) - float(startGCD2)

    y_pos = [0, 1]
    performance = [finalTimeGCD, finalTimeGCD2]
    objects = ["recursive", "iterative"]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Computation time (ms)')
    plt.title('Speed')
    plt.show()
