import numpy as np
import math

N = 8
T = np.zeros((N,N), dtype="float_")
Tt = np.zeros((N,N), dtype = "float_")

def Generate_T():
    for i in range(N):
        for j in range(N):
            if i == 0:
                T[i][j] = 1 / math.sqrt(N)
            else:
                T[i][j] = math.sqrt(2/N) * math.cos((2*j + 1) * (i * math.pi) / (2 * N))

def printMatrix(numpyArray):
    for i in range(len(numpyArray)):
        for j in range(len(numpyArray[i])):
            print("{0:0.3f}".format(T[i][j]), end = " ")
        print()


def main():
    Generate_T()
    print("Printing T")
    printMatrix(T)
    Tt = np.transpose(T)
    print("Printing the Transpose of T")
    printMatrix(Tt)


if __name__ == "__main__":
    main()