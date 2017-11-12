import numpy as np 
from numpy import linalg

def diagonaldeunos(A): # Deja a la matriz con unos en su diagonal
	n=A.shape[0]
	m=A.shape[1]
	M=np.ones((n,m), float)
	for i in range(0,n):
		if(A[i,i] != 0):
			M[i,:]=abs(A[i,:]/A[i,i])	
	return(M)


def gaussjordan(A):
	n=A.shape[0] 
	m=A.shape[1]
	M=np.ones((n,m), float)	
	M_F=np.ones((n,m), float)
	for i in range(0,n):
		for j in range(0,n-1):
			if(i==0 and A[i,i] != 0):
				M_F[i,:]=A[i,:]/A[i,i]
			elif(i>=1 and i>j):
				if(j==0):
					M[i,:]=A[i,:]-A[i,j]*M_F[j,:]
					M_F[i,:]=diagonaldeunos(M)[i,:]
				elif(j>0):
					M[i,:]=M_F[i,:]-M_F[i,j]*M_F[j,:]
					M_F[i,:]=diagonaldeunos(M)[i,:]
	return(M_F)
