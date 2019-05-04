#!/usr/bin/env python3

# Important modules for rsa key generation
import random
from multiprocessing import Process
import time
import math

# for file location
import os

# for plot and data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def generatePrime(size=4096):
    candidate = random.randint(pow(2, size-1), pow(2, size))
    return candidate



def checkPrime(number):
    for i in range(2, int(math.sqrt(number) / 2)):
        if (number % i) != 0:
            return False
    return True


def checkPrimeFermat(number):
    a = 2
    if number == 1:
        return True
    #print("la valeur de p : ", number)
    while(pow(a, 1, number) == 0):
        a = random.randint(2, number-1)
        #print("la valeur de a: ", a)
    fermat = pow(a, number) - a
    #print("la valeur de fermat : ", fermat)
    #print("divisibilite de fermat : ", fermat % number)
    if pow(fermat, 1, number) == 0:
        return True
    else:
        return False


def _try_composite(a, d, n, s):
    x = pow(a, d, n)
    if x == 1:
        return True
    for i in range(s - 1):
        if x == n - 1:
            return True
        x = pow(x, 2, n)
    return x == n - 1


def checkRabinMiller(number, k=18):
    if number in [1, 2, 3]:
        return True
    if not number & 1:
        return False
    
    d, s = number - 1, 0
    while d % 2 == 0:
        # dividing by two using bitshift
        d >>= 1
        s += 1
    
    for i in range(k):
        a = random.randint(2, number - 2)
        if not _try_composite(a, d, number, s):
            return False
    
    return True