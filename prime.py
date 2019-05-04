#!/usr/bin/env python3

import random
from multiprocessing import Process
import time

import matplotlib.pyplot as plt

def generatePrime(size=4096):
    candidate = random.randint(pow(2, size-1), pow(2, size))
    return candidate


def checkPrimeFermat(number):
    a = 2
    if number == 1:
        return True
    #print("la valeur de p : ", number)
    while((a % number) == 0):
        a += 1
        #print("la valeur de a: ", a)
    fermat = pow(a, number) - a
    #print("la valeur de fermat : ", fermat)
    #print("divisibilite de fermat : ", fermat % number)
    if (fermat % number) == 0:
        return True
    else:
        return False


def testPrime():
    """Testing prime function"""
    key_size = []
    time_values = []

    for taille in range(1, 30):
        key_size.append(taille)
        start = time.time()
        isPrime = False
        while isPrime is False:
            n = generatePrime(taille)
            isPrime = checkPrimeFermat(n)
        totalTime = time.time() - start
        time_values.append(totalTime)

    plt.plot(key_size, time_values)
    plt.legend("Fermat")
    plt.xlabel("Key size in bits")
    plt.ylabel("Check time in second")
    plt.title("Comparaison of method")
    plt.show()

if __name__ == "__main__":
    testPrime()