from kol3btesty import runtests


def airports( G, A, s, t ):
    n = len(A)
    M = [[A[i]+A[j] for j in range(n)] for i in range(n)]
    for i in range(n):
        M[i][i] = 0
    for u in range(n):
        for v,c in G[u]:
            if c < M[u][v]:
                M[u][v] = c
                M[v][u] = c

    Visited = [False for _ in range(n)]
    D = [10**10 for _ in range(n)]
    D[s] = 0
    Visited[s] = True
    min_i = s
    while min_i is not None:
        u = min_i
        if u == t: return D[t]
        min_i = None
        minn = 10**10

        for v in range(n):
            if not Visited[v]:
                if D[v] > D[u] + M[u][v]:
                    D[v] = D[u] + M[u][v]
                if D[v] < minn:
                    minn = D[v]
                    min_i = v

        Visited[min_i] = True

    return None





runtests(airports, all_tests=True)