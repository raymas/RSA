#!/usr/bin/env python3
from __future__ import print_function
import sys

# Prime number test
from prime import *

from multiprocessing import Queue, Process


def processClassical(start_length, end_length, q, prog):
    time_values = []

    isPrime = False
    print("Starting classical")
    for taille in range(start_length, end_length):
        prog.put(taille)
        start = time.time()
        isPrime = False
        while isPrime is False and not taille > 8:
            n = generatePrime(taille)
            isPrime = checkPrime(n)
        totalTime = time.time() - start
        time_values.append(totalTime if totalTime < 10 else 200)
    q.put(time_values)
    print("Classical ended")


def processFermat(start_length, end_length, q, prog):
    time_values_fermat = []

    isPrime = False
    print("Starting Fermat")
    for taille in range(start_length, end_length):
        prog.put(taille)
        start = time.time()
        isPrime = False
        while isPrime is False:
            n = generatePrime(taille)
            isPrime = checkPrimeFermat(n)
        totalTime = time.time() - start
        time_values_fermat.append(totalTime)
    q.put(time_values_fermat)
    print("Fermat ended")


def processRabinMiller(start_length, end_length, q, prog):
    time_values_rabin = []

    isPrime = False
    print("Starting Rabin Miller")
    for taille in range(start_length, end_length):
        prog.put(taille)
        start = time.time()
        isPrime = False
        while isPrime is False:
            n = generatePrime(taille)
            isPrime = checkRabinMiller(n)
        totalTime = time.time() - start
        time_values_rabin.append(totalTime)
    q.put(time_values_rabin)
    print("Rabin Miller ended")



def testPrime():
    """Testing prime function"""
    # start and stop in byte
    start, stop = 3, 25

    key_size = [i for i in range(start, stop)]

    results = [Queue() for _ in range(3)]
    progress = [Queue() for _ in range(3)]

    pClassical = Process(target=processClassical, args=(start, stop, results[0], progress[0]))
    pClassical.daemon = True

    pFermat = Process(target=processFermat, args=(start, stop, results[1], progress[1]))
    pFermat.daemon = True

    pRabin = Process(target=processRabinMiller, args=(start, stop, results[2], progress[2]))
    pRabin.daemon = True

    pClassical.start()
    pFermat.start()
    pRabin.start()

    time.sleep(0.1)

    while (pClassical.is_alive() or pFermat.is_alive() or pRabin.is_alive()):
        print("Classical : {}/{} | Fermat : {}/{} | Rabin : {}/{}".format(progress[0].get(), stop, progress[1].get(), stop, progress[2].get(), stop), end='\r')
        sys.stdout.flush()
        time.sleep(0.1)

    plt.plot(key_size, results[0].get(), 'r', key_size, results[1].get(), 'b', key_size, results[2].get(), 'g')

    classical_patch = mpatches.Patch(color='red', label='Classical')
    fermat_patch = mpatches.Patch(color='blue', label='Fermat')
    rabin_patch = mpatches.Patch(color='green', label='Rabin')
    plt.legend(handles=[classical_patch, fermat_patch, rabin_patch])

    plt.xlabel("Key size in bits")
    plt.ylabel("Check time in second")
    plt.title("Comparaison of method")
    plt.savefig(os.path.join(os.path.dirname(__file__), "speed.png"))
    plt.show()

if __name__ == "__main__":
    ret = input("This is going to take a long time, do you want to start the computation ? (y/n): ")
    if ret == "y":
        testPrime()