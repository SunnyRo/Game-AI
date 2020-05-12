"""
Name:           Son Vo
Course:         CS-3310-SPR20
Project:        1
Due:            03/06/20
Description:    Program both classical and strassen's Matrix multiplication.
Matrix size be n x n with n = 2, 4, 8, 16, 32, 64 ..... 
"""
#!/usr/bin/python
import time
import numpy as np

# enter size n of matrix n = 2,4,8,16,32 ....
n = int(input("Please enter matrix size   "))
# using numpy generate two matrices size nxn
matrix1 = np.random.randint(20, size=(n, n))
matrix2 = np.random.randint(20, size=(n, n))
# Matrix Multiplication : classical Method
def classical(matrix1, matrix2):
    n = len(matrix1)
    result = np.zeros([n, n], dtype=int)
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix1[i][0] * matrix2[0][j]
            for k in range(1, n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


# Matrix Multiplication : Strassen Method
def strassen(matrix1, matrix2):
    n = len(matrix1)
    result = np.zeros([n, n], dtype=int)
    if n == 2:
        # row * column to solve multiplication of 2x2 matrices
        result[0][0] = matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0]
        result[0][1] = matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]
        result[1][0] = matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]
        result[1][1] = matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]
        return result
    else:
        # keep dividing matrix size n into 4 sub-matrices size n/2
        newSize = n // 2
        a11 = np.zeros([newSize, newSize], dtype=int)
        a12 = np.zeros([newSize, newSize], dtype=int)
        a21 = np.zeros([newSize, newSize], dtype=int)
        a22 = np.zeros([newSize, newSize], dtype=int)

        b11 = np.zeros([newSize, newSize], dtype=int)
        b12 = np.zeros([newSize, newSize], dtype=int)
        b21 = np.zeros([newSize, newSize], dtype=int)
        b22 = np.zeros([newSize, newSize], dtype=int)

        # move value into new 4 sub-matrices
        for i in range(0, newSize):
            for j in range(0, newSize):
                a11[i][j] = matrix1[i][j]
                a12[i][j] = matrix1[i][j + newSize]
                a21[i][j] = matrix1[i + newSize][j]
                a22[i][j] = matrix1[i + newSize][j + newSize]

                b11[i][j] = matrix2[i][j]
                b12[i][j] = matrix2[i][j + newSize]
                b21[i][j] = matrix2[i + newSize][j]
                b22[i][j] = matrix2[i + newSize][j + newSize]
        # calculating P, Q, R, S, T, U, V
        # numpy for addition and recurrence relation(strassen) for multiplication
        p = strassen(np.add(a11, a22), np.add(b11, b22))
        q = strassen(np.add(a21, a22), b11)
        r = strassen(a11, np.subtract(b12, b22))
        s = strassen(a22, np.subtract(b21, b11))
        t = strassen(np.add(a11, a12), b22)
        u = strassen(np.subtract(a21, a11), np.add(b11, b12))
        v = strassen(np.subtract(a12, a22), np.add(b21, b22))
        # calculating c11, c12, c21, c22
        c11 = np.add(np.subtract(np.add(p, s), t), v)
        c12 = np.add(r, t)
        c21 = np.add(q, s)
        c22 = np.add(np.subtract(np.add(p, r), q), u)
        # grouping result into a matrix
        for i in range(0, newSize):
            for j in range(0, newSize):
                result[i][j] = c11[i][j]  # top left
                result[i][j + newSize] = c12[i][j]  # top right
                result[i + newSize][j] = c21[i][j]  # bottom left
                result[i + newSize][j + newSize] = c22[i][j]  # bottom right
        return result


# function to print a matrix
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print()


# creating a menu enter 1 if we want to see the execution time, 2 if want to see if both functions actually sort the list
print("Enter 1 to see execution time")
print("Enter 2 to see 2 matrices and its mutiplication")
menu = int(input(""))
if menu == 1:
    print("Classical method")
    start_time1 = time.time()
    temp1 = classical(matrix1, matrix2)
    print("--- %.8f seconds ---" % (time.time() - start_time1))
    print("Strassen method")
    start_time2 = time.time()
    temp2 = strassen(matrix1, matrix2)
    print("--- %.8f seconds ---" % (time.time() - start_time2))
else:
    print("\nTwo Matrices:")
    printMatrix(matrix1)
    print()
    printMatrix(matrix2)
    print("\nClassical method:")
    temp1 = classical(matrix1, matrix2)
    printMatrix(temp1)
    print("\nStrassen method:")
    temp2 = strassen(matrix1, matrix2)
    printMatrix(temp2)
