from zad1testy import runtests
from collections import deque

def bfs(G, s):
    n = len(G)
    Visited = [False for _ in range(n)]
    Parent = [None for _ in range(n)]
    D = [10**10 for _ in range(n)]
    D[s] = 0
    Visited[s] = True
    Q = deque()
    Q.appendleft(s)
    while Q:
        u = Q.pop()
        for v in G[u]:
            if not Visited[v]:
                Visited[v] = True
                D[v] = D[u] + 1
                Parent[v] = u
                Q.appendleft(v)

    return D, Parent


def best_root( L ):
    # tu proszę zaimplementować zadanie
    n = len(L)
    D, _ = bfs(L, 0)
    maks = 0
    s = - 1
    for i in range(n):
        if maks < D[i]:
            maks = D[i]
            s = i

    D, Parent = bfs(L, s)
    maks = 0
    s = - 1
    for i in range(n):
        if maks < D[i]:
            maks = D[i]
            s = i

    maks = maks // 2
    for i in range(maks):
        s = Parent[s]

    return s



runtests( best_root ) 
