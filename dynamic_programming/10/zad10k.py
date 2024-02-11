from zad10ktesty import runtests
from math import sqrt

def dywany ( N ):
    #Tutaj proszę wpisać własną implementację
    F = [0 for _ in range(N+1)]
    F[0] = 0
    Parent = [-1 for _ in range(N+1)]
    for n in range(1, N+1):
        i = 1
        minn = 10**10
        index = -1
        while i*i <= n:
            if F[n-i*i] < minn:
                minn = F[n-i*i]
                index = n-i*i
            i += 1
        F[n] = 1 + minn
        Parent[n] = index

    #print(F)
    #print(Parent)
    tab = []
    i = N
    while i > 0:
        #print(i)
        #print(Parent[i])
        x = sqrt(i - Parent[i])
        tab.append(x)
        i = Parent[i]

    return tab



runtests( dywany )

