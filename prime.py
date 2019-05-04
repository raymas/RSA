#!/usr/bin/env python3

import random
from multiprocessing import Process
import time
import math

import os

import matplotlib.pyplot as plt

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

    start_length = 1
    end_length = 9

    key_size= []
    time_values = []

    isPrime = False
    print("Starting classical")
    for taille in range(start_length, end_length):
        key_size.append(taille)
        start = time.time()
        isPrime = False
        while isPrime is False:
            n = generatePrime(taille)
            isPrime = checkPrime(n)
        totalTime = time.time() - start
        time_values.append(totalTime)

    key_size_fermat = []
    time_values_fermat = []

    isPrime = False
    print("Starting Fermat")
    for taille in range(start_length, end_length):
        key_size_fermat.append(taille)
        start = time.time()
        isPrime = False
        while isPrime is False:
            n = generatePrime(taille)
            isPrime = checkPrimeFermat(n)
        totalTime = time.time() - start
        time_values_fermat.append(totalTime)

    plt.plot(key_size, time_values, key_size_fermat, time_values_fermat)
    plt.legend("Naive sqrt/2 ", "Fermat")
    plt.xlabel("Key size in bits")
    plt.ylabel("Check time in second")
    plt.title("Comparaison of method")
    plt.savefig(os.path.join(os.path.dirname(__file__), "speed.png"))
    plt.show()

if __name__ == "__main__":
    testPrime()