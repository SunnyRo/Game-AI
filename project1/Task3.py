import numpy as np
n = int(input('enter array size   '))
matrix1 = np.random.randint(5,size=(n,n))
matrix2 = np.random.randint(5,size=(n,n))
result = np.random.randint(5,size=(n,n))
# matrix1 = np.random.rand(n,n)
# matrix2 = np.random.rand(n,n)
# result = np.random.rand(n,n)
#result = np.zeros(n,n)
print(matrix2)
print(matrix1)

def classical(arr1,arr2,result):
    for i in range(n-1):
        for j in range(n-1):
            result[i][j]= arr1[i][1]*arr2[1][j] 
            for k in range(n-1):
                result[i][j] += arr1[i][k]*arr2[k][j] 
    return result 
temp = classical(matrix1,matrix2,result)
print(temp)