from zad3testy import runtests

def f(T, V, q, l, P, F, i, p):
    if F[i][p] != -1: return F[i][p]
    p_ = min(q, p + V[i])
    if T[i] + p_ >= l: return 1
    minn = 10**10
    index = None
    for j in range(i+1, len(T)):
        d = T[j] - T[i]
        if d > p_: break
        if minn > f(T, V, q, l, P, F, j, p_-d):
            minn = f(T, V, q, l, P, F, j, p_-d)
            index = j
    F[i][p] = 1 + minn
    P[i][p] = index
    return F[i][p]


def iamlate(T, V, q, l):
    """tu prosze wpisac wlasna implementacje"""
    n = len(T)
    F = [[-1 for p in range(q+1)] for i in range(n)]
    P = [[None for p in range(q+1)] for i in range(n)]
    #print(f(T, V, q, l, P, F, 0, 0))
    if f(T, V, q, l, P, F, 0, 0) >= 10**10: return []
    #if n < 10 and q<10: print(F)
    tab = [0]
    x = P[0][0]
    p = 0
    prev = 0
    while x is not None:
        #print(x)
        tab.append(x)
        d = T[x] - T[prev]
        p = min(q, p + V[prev])
        p -= d
        prev = x
        x = P[x][p]



    return tab



runtests( iamlate )
