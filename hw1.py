

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

def driver1():
    X=[]
    sigma=5
    mu=0
    for _ in range(10000):
        X.append(random.normalvariate(sigma=sigma,mu=mu))
    plt.hist(X,bins=20)
    plt.title('gaussian distribution mu:%0.2f, sigma: %0.2f'%(mu,sigma))
    plt.xlabel('x')
    plt.ylabel('count')
    plt.show()
    plt.close()

    Y=problem1(X)
    if Y <0:
        l='negative'
    elif Y>0:
        l='positive'
    else:
        l='zero'
    print('majority of numbers in gaussian distribution are : %s'%l)

def problem1(x):
    n=np.array([x])
    sum=np.sum(n)
    if sum <0:
        return -1
    elif sum ==0 :
        return 0
    elif sum > 0:
        return 1

def driver3():
    N=np.array([1e2,1e3,1e4],dtype='float64')
    df=pd.DataFrame(dtype='float32')
    for n,i in zip(N,range(3)):
        s=problem3(n)
        print(s.dtype)
        df.loc[i,'N']=n
        df.loc[i,'first']=s[0]
        df.loc[i,'second']=s[1]
        df.loc[i,'third']=s[2]

    print(df)
def problem3(N):

    print('finding sum 3 different ways N:%i'%int(N))
    sum=np.array([0,0,0],dtype='float32')
    for n in range(int(N)*2):
        n=n+1
        sum[0]=sum[0]+(-1)**n*(n/(n+1))
        if n <=N:
            sum[1]=sum[1]-((2*n-1)/(2*n))+(2*n/(2*n+1))
            sum[2]=sum[2]+1/(2*n*(2*n+1))

    print(sum)
    return sum

def driver4(abs=True):
    X=[]
    for _ in range(1000):
        X.append(random.randint(-1000,1000))
    X=problem4(X,abs=abs)

def problem4(X,abs=False):
    Y=X.copy()
    # implementation of bubblesort
    print(X)
    unsorted=True
    while unsorted:
        b=[]
        for i in range(len(X)-1):
            if abs:
                g=np.abs(X[i])
                d=np.abs(X[i+1])
            else:
                g=X[i]
                d=X[i+1]
            if g >d :
                c=X[i]
                X[i]=X[i+1]
                X[i+1]=c
                b.append(True)
            else:
                b.append(False)
        unsorted=np.array(b).any()
    print(X)

    if abs:
        #sketch statement , sorry
        if (np.sort(np.abs(Y))==np.abs(X)).all():
            print('absolute value properly sorted')
    else:
        if (np.sort(Y)==X).all():
            print('its sorted properly by non ab ')


if __name__ ==  '__main__':
    # driver1()
    driver3()
    # driver4()
