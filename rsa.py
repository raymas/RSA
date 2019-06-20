#!/usr/bin/env python3

import logging

import math

from math_helpers import pgcde
from prime import _getPrime
from multiprocessing import Process, Pipe, cpu_count, Queue

import base64

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
        # as python handle byte more efficiently than bits we directly divide by 64
        self.blockSize = int(size / (8*8))

        self.size = size

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
                    pipe_send, self.size)) for _ in range(nbOfJobs)]

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
        self.d = (self.phi + (pgcde(self.e, self.phi)[1])) % self.phi
        print(self.d)
        # Find e
        # Find d
        pass

    def encrypt(self, m):
        """handle hex stream"""
        return pow(int(m, 16), self.e, self.n)

    def decrypt(self, x):
        """handle hex stream"""
        return pow(int(x, 16), self.d, self.n)

    def encryptBlock(self, blocks):
        """compute encryption on one block must be async"""
        return [self.encrypt(block) for block in blocks]

    def decryptBlock(self, blocks):
        """compute encryption on one block must be async"""
        return [self.decrypt(block) for block in blocks]

    def splitBuffer(self, buffer):
        """convert to ascii"""
        hex_ascii = ''.join('%02x'%ord(i) for i in buffer)
        
        blocks = [hex_ascii[i:i+self.blockSize] for i in range(0, len(hex_ascii), self.blockSize)]
        blocks[-1] = self.addPadding(blocks[-1])

        print(blocks)

        return blocks

    def addPadding(self, block, method="PKSC7"):
        # add padding to a block, this is not a block cipher but we need maleability you know
        if method == "PKSC7":
            deficit = (self.blockSize - len(block)) // 2
            for _ in range(deficit):
                block += '%02x'%deficit
        return block


def main():
   rsa = RSA(1024)
   rsa.getPrimes()
   rsa.getKeys()
   
   print("p={}\nq={}".format(rsa.p, rsa.q))

   text = "Hello world!"
   plain = rsa.splitBuffer(text)

   a = (rsa.encryptBlock(plain))
   for i in a:
       print(len(str(i)))

   print("encrypted {} ".format(a))
   #b = rsa.decrypt(a)
   # print("".join([chr(i) for i in b]))


if __name__ == "__main__":
    main()
