import numpy as np

def CalRg(A, B):
    for i in range(len(A)):
        b=A[i][i]
        A[i][i]=0
        for j in range(len(A[0])):
            A[i][j]=A[i][j]/(-b)
        B[i]=B[i]/b
    return A,B
    
def Linf(x1, x2):
    return sum([abs(x1[i]-x2[i]) for i in range(len(x1))])
    
def Jacob(A, B, e, x1, x2):
    R,g=CalRg(A,B)
    i = 0
    while Linf(x1,x2)>e:
        x1=x2
        x2=R.dot(x1)+g
        i+=1
    return x2,i
    
def GaussSeidel(A,B,e,x1):
    i = 0
    R,g=CalRg(A,B)
    x2=R.dot(x1)+g
    while Linf(x1,x2)>e:
        x1=x2
        x2=R.dot(x1)+g
        i+=1
    return x2,i 

if __name__=='__main__':
    A=np.matrix([
        [31,-13,0,0,0,-10,0,0,0],
        [-13,35,-9,0,-11,0,0,0,0],
        [0,-9,31,-10,0,0,0,0,0],
        [0,0,-10,97,-30,0,0,0,-9],
        [0,0,0,-30,57,-7,0,-5,0],
        [0,0,0,0,-7,47,-30,0,0],
        [0,0,0,0,0,-30,41,0,0],
        [0,0,0,0,-5,0,0,27,-2],
        [0,0,0,-9,0,0,0,-2,29]])
    
    B = np.matrix([15,27,-23,0,-20,12,-7,7,10])
    #print(Jacob(A, B, e, x1, x2))
    print(GaussSeidel(A,B,0.000001,[0,0,0,0,0,0,0,0,0]))
