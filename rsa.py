#!/usr/bin/env python3

import logging

from math_helpers import pgcde
from prime import _getPrime
from multiprocessing import Process, Pipe, cpu_count, Queue


class RSA(object):
    """RSA main class"""

    def __init__(self, size=4096):
        # prime number
        self.p, self.q = 2, 3
        # encryption key
        self.e = 65537
        # decryption key
        self.d = 0
        # modulus
        self.n = 0

        # block size for encryption assuming 4096 / 8 which is 512 quite correct maybe a little too big
        self.blockSize = int(size / 8)

        # logger to see what's going on
        self.logger = logging.getLogger(__name__)

    def getPrimes(self, numberOfKeys=2):
        # TODO: place our call to one of the function in prime
        numbers = []
        for _ in range(numberOfKeys):
            try:
                processes = []
                (pipe_recv, pipe_send) = Pipe(duplex=False)
                nbOfJobs = int(cpu_count())
                self.logger.debug(
                    "Prime generation | number of jobs {}".format(nbOfJobs))

                processes = [Process(target=_getPrime, args=(
                    pipe_send, 1024)) for _ in range(nbOfJobs)]

                for process in processes:
                    process.daemon = True
                    process.start()
                self.logger.debug("Starting processes")

                numbers.append(pipe_recv.recv())

            finally:
                pipe_recv.close()
                pipe_send.close()

                for process in processes:
                    if process.is_alive():
                        process.terminate()

        (self.p, self.q) = numbers

    def getKeys(self):
        print(self.e)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        while pgcde(self.e, self.phi)[0] != 1:
            self.e += 1
        print(self.e)
        """
        'd' à verifier
        """
        self.d = pgcde(self.e, self.phi)[1]
        print(self.d)
        # Find e
        # Find d
        pass

    def processBlock(self):
        # TODO : compute encryption on one block
        pass

    def splitBuffer(self, buffer):
        # split a buffer via block size
        return ""

    def addPadding(self, method):
        # add padding to a block, this is not a block cipher but we need maleability you know
        # look at PKSC5 or PKSC7
        return ""


def main():
   rsa = RSA()
   rsa.getPrimes()
   rsa.getKeys()

   print("p={}\nq={}".format(rsa.p, rsa.q))


if __name__ == "__main__":
    main()
