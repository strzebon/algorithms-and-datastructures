from kol2atesty import runtests

# 0 - Jacek
# 1 - Marian
def f(F, C, o, i):
    if F[o][i] != -1:
        return F[o][i]
    if o == 0: F[o][i] =  min(f(F, C, 1, i+1), f(F, C, 1, i+2), f(F, C, 1, i+3))
    else: F[o][i] = min(C[i+1]-C[i] + f(F, C, 0, i+1), C[i+2]-C[i] + f(F, C, 0, i+2), C[i+3]-C[i] + f(F, C, 0, i+3))
    return F[o][i]

def drivers( P, B ):
    n = len(P)
    for i in range(n):
        x, w = P[i]
        if w: P[i] = (x, w, i)
    P.sort()
    Z = [-1]
    C = [0]
    counter = 0
    for i in range(n):
        if P[i][1]:
            Z.append(P[i][2])
            C.append(counter)
        else: counter += 1

    n = len(Z)
    for _ in range(3): C.append(counter)

    F = [[-1 for i in range(len(C))] for o in range(2)]
    for o in range(2):
        for i in range(3):
            F[o][n+i] = 0
    f(F,C,0,0)
    tab = []
    o = 0
    i = 0

    while i < n:
        if o == 0:
            if F[o][i] == F[1][i+1]:
                i += 1
                if i < n: tab.append(Z[i])
            elif F[o][i] == F[1][i+2]:
                i += 2
                if i < n: tab.append(Z[i])
            else:
                i += 3
                if i < n: tab.append(Z[i])
            o = 1
        else:
            if F[o][i] == C[i+1] - C[i] + F[0][i+1]:
                i += 1
                if i < n: tab.append(Z[i])
            elif F[o][i] == C[i+2] - C[i] + F[0][i+2]:
                i += 2
                if i < n: tab.append(Z[i])
            else:
                i += 3
                if i < n: tab.append(Z[i])
            o = 0

    return tab

runtests( drivers, all_tests = True )