from zad7ktesty import runtests 

def f(Z, K, F, i, l):
    if F[i][l] != -1: return F[i][l]
    F[i][l] = f(Z, K, F, i-1, l)
    if K[i] <= l:
        F[i][l] = max(F[i][l], Z[i] + f(Z, K, F, i-1, l-K[i]))
    return F[i][l]

def dfs(T, D):
    n = len(D)
    K = [0 for _ in range(n)]
    N = len(T)
    M = len(T[0])
    Visited = [[False for j in range(M)] for i in range(N)]
    for i in range(n):
        j = D[i]
        K[i] = dfs_visit(T, Visited, 0, j)
    return K


def dfs_visit(T, Visited, i, j):
    Visited[i][j] = True
    N = len(T)
    M = len(T[0])
    if T[i][j] == 0: return 0
    s = T[i][j]
    if i-1 >= 0 and not Visited[i-1][j]: s += dfs_visit(T, Visited, i-1, j)
    if i + 1 < N and not Visited[i + 1][j]: s += dfs_visit(T, Visited, i + 1, j)
    if j - 1 >= 0 and not Visited[i][j-1]: s += dfs_visit(T, Visited, i, j-1)
    if j+1 < M and not Visited[i][j+1]: s += dfs_visit(T, Visited, i, j+1)
    return s

def ogrodnik (T, D, Z, l):
    n = len(D)
    # K = [0 for _ in range(n)]
    # for j in range(n):
    #     j_ = D[j]
    #     for i in range(N):
    #         for k in range(j_-1,-1,-1):
    #             if T[i][k] == 0: break
    #             K[j] += T[i][k]
    #         for k in range(j_, M):
    #             if T[i][k] == 0: break
    #             K[j] += T[i][k]

    # F = [[-1 for _ in range(l+1)] for i in range(n)]
    # for j in range(K[0]):
    #     if j == l+1: break
    #     F[0][j] = 0
    # for j in range(K[0], l+1):
    #     F[0][j] = Z[0]
    K = dfs(T, D)
    F = [[0 for _ in range(l+1)] for i in range(n)]
    for j in range(K[0], l+1):
        F[0][j] = Z[0]

    for j in range(l+1):
        for i in range(1, n):
            F[i][j] = F[i-1][j]
            if K[i] <= j:
                F[i][j] = max(F[i][j], Z[i] + F[i-1][j-K[i]])



    return F[n-1][l]

runtests( ogrodnik, all_tests=True )
