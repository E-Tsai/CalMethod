ENOMEM = 1
#Newton_Method
def f(x):
    return 2*x**4+24*x**3+61*x**2-16*x+1

def g(x):
    return 8*x**3+72*x**2+122*x-16

def Newton(f,g,x0,e,MAX):
    x=[x0]
    y=[f(x0)]
    for i in range(MAX):
        x0=x[len(x)-1]
        x1=x0-f(x0)/g(x0)
        x.append(x1)
        y.append(f(x1))
        if abs(f(x1))<e:
            return (x,y)
    return ([], [])
#Secant_Method
def Secant(f,x0,x1,e,MAX):
    x=[x0,x1]
    y=[f(x0),f(x1)]
    for i in range(MAX):
        x0=x[len(x)-2]
        x1=x[len(x)-1]
        x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
        x.append(x2)
        y.append(f(x2))
        if abs(f(x2))<e:
            return (x,y)
    return ([], [])

def printmd(x, y):
    print("| k | x | y |")
    print("| -- | -- | -- |")
    for i in range(len(x)):
        print("| k={:d} | {:.12e} | {:.12e} |".format(i, x[i], y[i]))
    print("\n")


if __name__=='__main__':
    x, y = Newton(f,g,0,1e-10,10000000)
    printmd(x, y)
    x, y = Newton(f,g,1,1e-10,10000000)
    printmd(x, y)
    x, y = Secant(f,0,0.1,1e-10,10000000)
    printmd(x, y)
    x, y = Secant(f,0.5,1.0,1e-10,10000000)
    printmd(x, y)
    
