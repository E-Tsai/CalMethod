import numpy as np

def CalRg(A, B):
    for i in range(len(A)):
        b=A[i][i]
        A[i][i]=0
        for j in range(len(A[0])):
            A[i][j]/=(-b)
        B[i]/=b
    return A,B
    
def Linf(x1, x2):
    return sum([abs(x1[i]-x2[i]) for i in range(len(x1))])
    
def Jacob(A, B, e, x1, x2):
    R,g=CalRg(A,B)
    while Linf(x1,x2)>e:
        x1=x2
        x2=R.dot(x1)+g
    return x2
    
def Gauss-Seidel(A,B,e,x1):
    R,g=CalRg(A,B)
    x2=R.dot(x1)+g
    while Linf(x1,x2)>e:
        x1=x2
        x2=R.dot(x1)+g
    return x2
