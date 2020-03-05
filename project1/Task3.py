import time
import numpy as np
n = int(input('enter array size   '))
# using numpy generate two arrays or lists size n
matrix1 = np.random.randint(20,size=(n,n))
matrix2 = np.random.randint(20,size=(n,n))
# Matrix Multiplication : classical Method
def classical(arr1,arr2):
    n = len(arr1)
    result = np.zeros([n,n], dtype=int)
    for i in range(n):
        for j in range(n):
            result[i][j]= arr1[i][0]*arr2[0][j] 
            for k in range(1,n):
                result[i][j] += arr1[i][k]*arr2[k][j] 
    return result 
# Matrix Multiplication : Strassen Method
def strassen(arr1,arr2):
    n = len(arr1)
    result = np.zeros([n,n],dtype =int)
    if n == 2:
        result[0][0]= arr1[0][0]*arr2[0][0] + arr1[0][1]*arr2[1][0]
        result[0][1]= arr1[0][0]*arr2[0][1] + arr1[0][1]*arr2[1][1]
        result[1][0]= arr1[1][0]*arr2[0][0] + arr1[1][1]*arr2[1][0]
        result[1][1]= arr1[1][0]*arr2[0][1] + arr1[1][1]*arr2[1][1]
        return result
    else:
        # dividing matrix size n into 4 sub-matrices size n/2
        newSize = n//2
        a11 = np.zeros([newSize,newSize],dtype = int)
        a12 = np.zeros([newSize,newSize],dtype = int)
        a21 = np.zeros([newSize,newSize],dtype = int)
        a22 = np.zeros([newSize,newSize],dtype = int)

        b11 = np.zeros([newSize,newSize],dtype = int)
        b12 = np.zeros([newSize,newSize],dtype = int)
        b21 = np.zeros([newSize,newSize],dtype = int)
        b22 = np.zeros([newSize,newSize],dtype = int)
         
        #move value into new sub-matrices
        for i in range(0,newSize):
            for j in range(0,newSize):
                a11[i][j] = arr1[i][j]
                a12[i][j] = arr1[i][j + newSize]
                a21[i][j] = arr1[i + newSize][j]
                a22[i][j] = arr1[i + newSize][j + newSize]

                b11[i][j] = arr2[i][j]
                b12[i][j] = arr2[i][j + newSize]
                b21[i][j] = arr2[i + newSize][j]
                b22[i][j] = arr2[i + newSize][j + newSize]
        # calculating P, Q, R, S, T, U, V, c11, c12, c21, c22
        p = strassen(np.add(a11,a22),np.add(b11,b22))
        q = strassen(np.add(a21,a22),b11) 
        r = strassen(a11,np.subtract(b12,b22))
        s = strassen(a22,np.subtract(b21,b11))
        t = strassen(np.add(a11,a12),b22)
        u = strassen(np.subtract(a21,a11),np.add(b11,b12))
        v = strassen(np.subtract(a12,a22),np.add(b21,b22))
        # c11 = np.subtract(np.add(p,s),np.add(t,v)) 
        c11 = np.add(np.subtract(np.add(p,s),t),v)
        c12 = np.add(r,t) 
        c21 = np.add(q,s) 
        c22 = np.add(np.subtract(np.add(p,r),q),u)
        # c22 = np.subtract(np.add(p,r),np.add(q,u)) 
        # grouping result into a single matrix
        for i in range (0,newSize):
            for j in range(0,newSize):
                result[i][j] = c11[i][j]
                result[i][j + newSize] = c12[i][j]
                result[i + newSize][j] = c21[i][j]
                result[i + newSize][j + newSize] = c22[i][j]
        return result
# function to print a matrix
def printMatrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end =" ")
        print()

start_time1= time.time()
temp = classical(matrix1,matrix2)
print("--- %.8f seconds ---" % (time.time() - start_time1))
start_time2 = time.time()
temp2 = strassen(matrix1,matrix2)
print("--- %.8f seconds ---" % (time.time() - start_time2))
