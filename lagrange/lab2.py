from math import cos
from math import pi
from math import fabs

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    if x < -5 or x > 5:
        print("error: out of range.")
        return -1
    return 1.0/(x*x+x+4)

def insert1(N):
    res = []
    for i in range(N+1):
        x = -5 + 10.0/N * i
        res.append((x, f(x)))
    return res

def insert2(N):
    res = []
    for i in range(N+1):
        x = -5*cos((2*i+1)*pi/(2*N+2))
        res.append((x, f(x)))
    return res


def cal(x, arr, n):
    fx = 0
    for i in range(n+1):
        tmp = 1
        for j in range(n+1):
            if i == j:
                continue
            tmp *= (x - arr[j][0])/(arr[i][0] - arr[j][0])
        fx += tmp * arr[i][1]
    return fx

def draw(x, p, f, N):
    
    fig,ax = plt.subplots()
    
    plt.xlabel('Lagrange Integration, N = {}'.format(N))
    #plt.ylabel('migration time (s); request delay (ms)')
    
    """set interval for y label"""
    yticks = np.arange(-0.1, 0.3, 0.05)
    ax.set_yticks(yticks)
    
    
    """set min and max value for axes"""
    ax.set_ylim([-0.1,0.3])
    ax.set_xlim([-5,5])
    
    
    plt.plot(x,p,"-",label="lagrange integration", lw=0.5)
    plt.plot(x,f,"-",label="original function", lw=0.5)
    
    """open the grid"""
    plt.grid(True)
    
    plt.legend(bbox_to_anchor=(1.0, 1), loc=1, borderaxespad=0.)
    
    plt.show()


def calerror(arr, N):
    err = 0
    p = []
    f = []
    a = []
    for i in range(501):
        x = i/50 - 5
        fx = 1.0/(x*x+x+4)
        px = cal(x, arr, N)
        a.append(x)
        p.append(px)
        f.append(fx)
        tmp = fabs(fx - px)
        if tmp > err:
            err = tmp
    draw(a, p, f, N)
    return err

def printerr(N, arr):
    err = calerror(arr, N)
    print("n = {}, {:.12e}".format(N, err))


if __name__ == '__main__':
    for N in [4, 8, 16]:
        insert_arr = insert1(N)
        printerr(N, insert_arr)
    print()
    for N in [4, 8, 16]:
        insert_arr = insert2(N)
        printerr(N, insert_arr)

    