#!/usr/bin/env python3

import random
from multiprocessing import Process


def generatePrime(size=4096):
    candidate = random.randint(2**(size-1), 2**(size))

    # TODO : check if prime
    # Naive or intelligent method ?