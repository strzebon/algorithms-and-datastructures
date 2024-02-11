from zad2testy import runtests

def f(F, G, i, j, o, prev):
    if F[i][j][o][prev] != -1: return F[i][j][o][prev]
    w = len(G)
    k = len(G[0])
    A = [60, 40, 30]
    F[i][j][o][prev] = 10**10

    if o == 0 and j+1 < k and G[i][j+1] != 'X':
        F[i][j][o][prev] = min(F[i][j][o][prev], A[prev] + f(F, G, i, j+1, o, min(2, prev+1)))

    if o == 1 and i+1 < w and G[i+1][j] != 'X':
        F[i][j][o][prev] = min(F[i][j][o][prev], A[prev] + f(F, G, i+1, j, o, min(2, prev+1)))

    if o == 2 and j-1 >= 0 and G[i][j-1] != 'X':
        F[i][j][o][prev] = min(F[i][j][o][prev], A[prev] + f(F, G, i, j-1, o, min(2, prev+1)))

    if o == 3 and i-1 >= 0 and G[i-1][j] != 'X':
        F[i][j][o][prev] = min(F[i][j][o][prev], A[prev] + f(F, G, i-1, j, o, min(2, prev+1)))

    F[i][j][o][prev] = min(F[i][j][o][prev], 45 + f(F, G, i, j, (o + 1) % 4, 0), 45 + f(F, G, i, j, (o - 1) % 4, 0))

    return F[i][j][o][prev]


def robot( G, A, B ):
    w = len(G)
    k = len(G[0])
    F = [[[[-1 for prev in range(3)] for o in range(4)] for j in range(k)] for i in range(w)]
    b, a = A
    d, c = B
    for o in range(4):
        for prev in range(3):
            F[c][d][o][prev] = 0

    x = f(F, G, a, b, 0, 0)
    if x >= 10**10:
        return None
    return x

runtests( robot )