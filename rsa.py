#!/usr/bin/env python3

import prime

class RSA(object):
    """RSA main class"""
    def __init__(self, size=4096):
        # prime number 
        self.p, self.q = 2, 3
        # encryption key
        self.e = 0
        # decryption key
        self.d = 0
        # modulus
        self.n = 0

        # block size for encryption assuming 4096 / 8 which is 512 quite correct maybe a little too big
        self.blockSize = int(size / 8)

    def getPrimes(self):
        # TODO: place our call to one of the function in prime
        pass

    def getKeys(self):
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
    print("Hello boys!")

    print("Tchoa :")


if __name__ == "__main__":
    main()
