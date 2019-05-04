#!/usr/bin/env python3

import random
from multiprocessing import Process
import time


def generatePrime(size=4096):
    candidate = random.randint(pow(2, size-1), pow(2, size))
    return candidate


def checkPrime(number):
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


n = 104729

# print(checkPrime(6))
# print(checkPrime(11))
# print(checkPrime(5))
# print(checkPrime(3))
# print(checkPrime(2))
# print(checkPrime(97))
#
# print(checkPrime(1))

print(checkPrime(n))


#
# for taille in range(10, 60):
#     print("Taille :" + str(taille))
#     start = time.time()
#     isPrime = False
#     while isPrime is False:
#         n = generatePrime(taille)
#         isPrime = checkPrime(n)
#         # print("Check if n is prime : " + str(n) + " result: " + str(isPrime))
#
#     print("Temps : " + str(time.time() - start) + " secondes")
#     print(n)
