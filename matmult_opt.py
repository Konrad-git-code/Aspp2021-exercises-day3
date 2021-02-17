#!/usr/bin/python
# Program to multiply two matrices using NumPy
import numpy as np

N = 250
@profile
def multiplyMat(N):
# NxN matrix
	X=np.random.rand(N, N)

# Nx(N+1) matrix
	Y=np.random.rand(N,N+1)

	result = np.matmul(X, Y)


	return result

multiplyMat(N)
