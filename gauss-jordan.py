import numpy as np

def guassElimination(A, b):
    n =  len(A)
    if b.size != n:
        raise ValueError("Incompatible sizes")
    for pivot in xrange(n-1):
        for row in xrange(pivot+1, n):
            multiplier = A[row][pivot]/A[pivot][pivot]
            A[row][pivot] = multiplier
            for column in xrange(pivot+1, n):
                A[row][column] =  A[row][column] - multiplier*A[pivot][column]
            b[row] = b[row] - multiplier*b[pivot]
    print("Matrix A:")
    print (A)
    print("Vector b:")
    print (b)
    x = np.zeros(n)
    k = n-1
    x[k] = b[k]/A[k,k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    print ("The Solution to Ax=b is:")
    return x

if __name__ == "__main__":
    A = (np.random.rand(3,3)*10).astype(int)
    b = (np.random.rand(3,1)*10).astype(int)
    print (guassElimination(np.copy(A), np.copy(b)))

