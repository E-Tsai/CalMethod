from math import sin
from math import cos
from math import fabs
from math import log



def simpr(f, a, b, n):
    h = (b-a)/n 
    mid1 = mid2 = 0
    for i in range(0, n//2):
        mid1 += f(a+(2*i+1)*h)
        mid2 += f(a+2*i*h)
    return h*(f(a)+4*mid1+2*mid2+f(b))/3


def trapez(f, a, b, n):
    h = (b-a)/n
    mid = 0
    for i in range(1, n):
        mid += f(a+i*h)
    return h*(f(a)/2+mid+f(b)/2)


if __name__ == '__main__':
    
    expect = -cos(6) + cos(1)

    print(expect)

    r = 5*(sin(1)+4*sin(7/2)+sin(6))/6
    er = (expect-r)/r

    for i in range(0, 13):
        n = pow(2, i)
        res = trapez(sin, 1, 6, n)
        e = (expect - res)/res
        print("n = {}, {:.12e}\n {:.12e}\n".format(n, res, e)) 

    print()

    for i in range(0, 13):
        n = pow(2, i)
        res = simpr(sin, 1, 6, n)
        e = (expect - res)/res
        print("n = {}, {:.12e}\n {:.12e}\n".format(n, res, e)) 



    
