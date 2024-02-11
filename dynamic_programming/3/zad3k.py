from zad3ktesty import runtests

def f(T, k, F, i):
    if F[i] != -1:
        return F[i]
    minn = 10**10
    for j in range(1, k+1):
        minn = min(minn, f(T, k, F, i-j))

    F[i] = T[i] + minn
    return F[i]

def ksuma( T, k ):
    #Tutaj proszę wpisać własną implementację
    n = len(T)
    F = [-1 for _ in range(n)]
    for i in range(k):
        F[i] = T[i]

    wynik = 10**10
    for i in range(n-k, n):
        wynik = min(wynik, f(T, k, F, i))

    return wynik
    
runtests ( ksuma )