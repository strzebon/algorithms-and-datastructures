from zad12ktesty import runtests 

def f(F, T, i, k):
    #if i == -1: return 0
    if F[i][k] != -1: return F[i][k]
    minn = T[i]
    for j in range(1,i+1):
        minn = min(minn, max(f(F, T, j-1, k-1), T[i] - T[j-1]))
    F[i][k] = minn
    return F[i][k]
def autostrada( T, k ):
    #Tutaj proszę wpisać własną implementację
    n = len(T)
    for i in range(1, n):
        T[i] += T[i-1]

    F = [[-1 for j in range(k+1)] for i in range(n)]
    for i in range(n):
        F[i][0] = 10**10


    return f(F, T, n-1, k)

runtests ( autostrada,all_tests=True )