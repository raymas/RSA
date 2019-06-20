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


if __name__ == "__main__":
    startGCD = "%.20f" % time.time()
    print(extended_gcd(120, 23))
    finalTimeGCD = float("%.20f" % time.time()) - float(startGCD)

    startGCD2 = "%.20f" % time.time()
    # print(extended_gcd2(120, 23))
    finalTimeGCD2 = float("%.20f" % time.time()) - float(startGCD2)

    y_pos       = [0, 1]
    performance = [finalTimeGCD, finalTimeGCD2]
    objects     = ["recursive", "iterative"]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Computation time (ms)')
    plt.title('Speed')
    plt.show()