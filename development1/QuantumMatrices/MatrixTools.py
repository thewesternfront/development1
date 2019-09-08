#!/usr/bin/env python

"""MatrixTools.py. Manipulates Matrices and Vectors for Quantum Computing"""

__author__      = "Troy Eugene West"
__copyright__   = "Belowmiddlec.co.uk"



from array import *

def main():
    print("Matrix Libs")

    T = [[11, 12, 5],
         [15, 6, 10],
         [10, 8, 12]]

    M = [[2, 2, 2],
         [3, 3, 3],
         [2, 2, 2]]

    V = [2, 3, 5 ]

    matrixAddScalar(T, 3)
    matrixMultiplyScalar(T, 4)
    matrixMultiplyVector(T, V)
    matrixMultiplyMatrix(T, M)

def matrixAddScalar(TM, increm):
    for i in TM:
        for j in i:
            print(j+increm)

def matrixMultiplyScalar(TM, multiplier):
    for i in TM:
        for j in i:
            print(j*multiplier)

def matrixMultiplyVector(TM, VM):

    for y in range(len(TM)):
        for x in range(len(VM)):
            #print(y, x)
            result = TM[y][x]
            #print(" the result ", result)
            result2 = VM[x]
            #print(" result2 = ", result2)
            answer = result * result2
            print("THE ANSWER = ", answer)

# in this case multiply the row of one matrix by the column of another.
def matrixMultiplyMatrix(TM, MM):
    for y in range(len(TM)):
        for x in range(len(MM)):
            #print(y, x)
            result = TM[y][x]
            #print(" the result ", result)
            result2 = MM[x][y]
            #print(" result2 = ", result2)
            answer = result * result2
            print("THE ANSWER = ", answer)

if __name__ == '__main__':
    main()