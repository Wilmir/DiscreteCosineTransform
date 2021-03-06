import math
import numpy as np


class DCT_Demo(object):
    def __init__(self, level):
        self.Qlevel = level
        self.N = 8
        self.n = 8.0
        self.T = np.zeros((self.N, self.N), dtype="float")
        self.Tt = np.zeros((self.N, self.N), dtype="float")  # transpose of T

        # Compression
        self.TM = np.zeros((self.N, self.N), dtype="float")  # the matrix product of (T * M) for compression or (Tt * R) for decompression
        self.DCT = np.zeros((self.N, self.N), dtype="float")  # the matrix product of (TM * Tt) for compression or (TtR * T) for decompression
        self.Qq = np.zeros((self.N, self.N), dtype="int32")  # The quality level
        self.C = np.zeros((self.N, self.N), dtype="int32")  # DCT divided by Qq

        # Decompression
        self.R = np.zeros((self.N, self.N), dtype="float")  # the product of C and Qq
        self.fin = np.zeros((self.N, self.N), dtype="int32")  # the matric product of TM * T

        # Givens
        self.M = np.array([[16, 8, 23, 16, 5, 14, 7, 22],
                           [20, 14, 22, 7, 14, 22, 24, 6],
                           [15, 23, 24, 23, 9, 6, 6, 20],
                           [14, 8, 11, 14, 12, 12, 25, 10],
                           [10, 9, 11, 9, 13, 19, 5, 17],
                           [8, 22, 20, 15, 12, 8, 22, 17],
                           [24, 22, 17, 12, 18, 11, 23, 14],
                           [21, 25, 15, 16, 23, 14, 22, 22]])

        self.Q50 = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                             [12, 12, 14, 19, 26, 58, 60, 55],
                             [14, 13, 16, 24, 40, 57, 69, 56],
                             [14, 17, 22, 29, 51, 87, 80, 62],
                             [18, 22, 37, 56, 68, 109, 103, 77],
                             [24, 35, 55, 64, 81, 104, 113, 92],
                             [49, 64, 78, 87, 103, 121, 120, 101],
                             [72, 92, 95, 98, 112, 100, 103, 99]])

        self.Generate_T()
        self.Calculate_Q()

    def Calculate_FDCT(self):
        self.TM = np.matmul(self.T, self.M)
        self.DCT = np.matmul(self.TM, self.Tt)
        self.DCT = self.DCT.astype(int)

        print("\n\nDCT")
        self.printMatrix(self.DCT, 1)

    def Calculate_IDCT(self):
        self.TM = np.matmul(self.Tt, self.R)
        self.fin = np.matmul(self.TM, self.T)
        self.fin = self.fin.astype(int)


    def Generate_T(self):
        for r in range(self.N):
            for c in range(self.N):
                if r == 0:
                    self.T[r][c] = 1 / math.sqrt(self.n)
                else:
                    self.T[r][c] = math.sqrt(2 / self.n) * math.cos((2 * c + 1) * (r * math.pi) / (2 * self.n))
        # print("Matrix T")
        # self.printMatrix(self.T, 0)
        self.Tt = np.transpose(self.T)
        # print("Matrix T - Transpose")
        # self.printMatrix(self.Tt, 0)

    def Calculate_Q(self):
        """
        if self.Qlevel == 50:
            self.Qq = np.copy(self.Q50)
        elif (self.Qlevel >= 1) and (self.Qlevel < 50):
            for r in range(self.N):
                for c in range(self.N):
                    temp = int(self.Q50[r][c] * (50 / self.Qlevel))
                    if (temp > 255):
                        self.Qq[r][c] = 255
                    else:
                        self.Qq[r][c] = temp

        elif (self.Qlevel > 50) and (self.Qlevel <= 100):
            for r in range(self.N):
                for c in range(self.N):
                    self.Qq[r][c] = int(round(self.Q50[r][c] * ((100 - float(self.Qlevel)) / 50.0)))

        else:
            print("An invalid quantisation level was entered")
        """
        temp = 0
        print("Quality Selected: {0}".format(self.Qlevel))

        if  self.Qlevel == 50:
            self.Qq = np.copy(self.Q50)
        elif 1 <= self.Qlevel <= 100:
            q = (100 - float(self.Qlevel))/50.0 if self.Qlevel >=50 else 50.0 / self.Qlevel
            for r in range(self.N):
                for c in range(self.N):
                    temp = int(round(self.Q50[r][c] * q))
                    self.Qq[r][c] = temp if temp <= 255 else 255
        else:
            print("An invalid quantisation level was entered")

        self.printMatrix(self.Qq, 1)

    def printMatrix(self, npArray, type):
        if type == 0:
            for r in range(self.N):
                for c in range(self.N):
                    print("{0:0.3f}".format(npArray[r][c]), end=" ")
                print()
        elif type == 1:
            for r in range(self.N):
                for c in range(self.N):
                    print("{}".format(npArray[r][c]), end=" ")
                print()

    def QuantizationStepForward(self):
        self.C = np.divide(self.DCT,self.Qq)
        self.C = self.C.astype(int)

    def QuantizationStepInverse(self):
        self.R = np.multiply(self.C,self.Qq)

    def Compare(self):
        dif = np.abs(np.subtract(self.M, self.fin))
        np.set_printoptions(precision=2)
        print("\n\nDifference\n")
        print(dif)
