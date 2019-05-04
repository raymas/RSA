#!/usr/bin/env python3

import random
from multiprocessing import Process
import time


def generatePrime(size=4096):
    candidate = random.randint(2**(size - 1), 2**(size))
    return candidate


def checkPrime(number):
    for i in range(2, int(number / 2)):
        if (number % i) == 0:
            return False
    return True


for taille in range(10, 60):
    print("Taille :" + str(taille))
    start = time.time()
    isPrime = False
    while isPrime is False:
        n = generatePrime(taille)
        isPrime = checkPrime(n)
        # print("Check if n is prime : " + str(n) + " result: " + str(isPrime))

    print("Temps : " + str(time.time() - start) + " secondes")
    print(n)
