import numpy as np
import math
import pandas as pd

N = 8
T = np.zeros((N,N), dtype="float_")
Tt = np.zeros((N,N), dtype = "float_")

def dctFunc(i,j):
    if i == 0:
        return 1/math.sqrt(N)
    else:
        return (math.sqrt(2/N)) * math.cos((i * math.pi)*(2*j + 1)/(2*N))

def Generate_T():
    for i in range(N):
        for j in range(N):
            T[i][j] = dctFunc(i,j)

def print_Array(npArray):
    for i in range(N):
        for j in range(N):
            print("{0:0.03f}".format(T[i][j]), end = "\t")
        print()


npArray = Generate_T()
print_Array(npArray)



