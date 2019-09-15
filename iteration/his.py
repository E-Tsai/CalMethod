def Jacobi(A,x,b):
    n=len(b)
    x1=x.copy()
    x2=x.copy()
    count=0
    while sum([abs(x1[i]-x2[i])for i in range(n)])>1e-5 or count==0:
        for i in range(n):
            x2[i]=b[i]
            for j in range(n):
                if j!=i:
                    x2[i]+=-x1[j]*A[i][j]
            x2[i]/=A[i][i]
        count+=1
        x1,x2=x2,x1
    return (x1,count)

def Gauss_Seidel(A,x,b):
    n=len(b)
    count=0
    x=x.copy()
    x_=x.copy()
    while sum([abs(x[i]-x_[i])for i in range(n)])>1e-5 or count==0:
        x_=x.copy()
        for i in range(n):
            x[i]=b[i]
            for j in range(n):
                if j!=i:
                    x[i]+=-x[j]*A[i][j]
            x[i]/=A[i][i]
        count+=1
    return (x,count)

A=[
    [31,-13,0,0,0,-10,0,0,0],
    [-13,35,-9,0,-11,0,0,0,0],
    [0,-9,31,-10,0,0,0,0,0],
    [0,0,-10,79,-30,0,0,0,-9],
    [0,0,0,-30,57,-7,0,-5,0],
    [0,0,0,0,-7,47,-30,0,0],
    [0,0,0,0,0,-30,41,0,0],
    [0,0,0,0,-5,0,0,27,-2],
    [0,0,0,-9,0,0,0,-2,29]
]
b=[-15,27,-23,0,-20,12,-7,7,10]

x=[0.0 for i in range(9)]
x,count=Jacobi(A,x,b)
print(count)
print("| x1 |")
print("|  -- |")
for i in range(len(x)):
    print("|  {:.12e} |".format(x[i]))

x=[0.0 for i in range(9)]
x,count=Gauss_Seidel(A,x,b)
print(count)
print("| x1 |")
print("|  -- |")
for i in range(len(x)):
    print("|  {:.12e} |".format(x[i]))