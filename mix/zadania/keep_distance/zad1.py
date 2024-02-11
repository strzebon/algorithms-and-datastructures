from zad1testy import runtests
from collections import deque

def f_w(M):
    n = len(M)
    D = [[10**10 for j in range(n)] for i in range(n)]
    for i in range(n):
        D[i][i] = 0
    for i in range(n):
        for j in range(n):
            if M[i][j] != 0: D[i][j] = M[i][j]

    for k in range(n):
        for u in range(n):
            for v in range(n):
                D[u][v] = min(D[u][v], D[u][k] + D[k][v])
    return D

def keep_distance(M, x, y, d):
    n = len(M)
    #print(M)
    D = f_w(M)
    #print(D)
    Visited = [[False for j in range(n)] for i in range(n)]
    Parent = [[None for j in range(n)] for i in range(n)]
    Q = deque()
    Q.appendleft((x,y))
    Visited[x][y] = True
    while Q:
        u, v = Q.pop()
        #print(u, v)
        if u == y and v == x: break
        for i in range(n):
            if not Visited[i][v] and M[u][i] != 0 and D[i][v] >= d:
                Visited[i][v] = True
                Parent[i][v] = (u,v)
                Q.appendleft((i,v))

            if not Visited[u][i] and M[v][i] != 0 and D[u][i] >= d:
                Visited[u][i] = True
                Parent[u][i] = (u, v)
                Q.appendleft((u,i))

        for i in range(n):
            for j in range(n):
                if not Visited[i][j] and (i,j) != (v,u) and M[u][i] != 0 and M[v][j] != 0 and D[i][j] >= d:
                    Visited[i][j] = True
                    Parent[i][j] = (u, v)
                    Q.appendleft((i, j))

    #else: return []

    tab = []
    a = (y, x)
    while a is not None:
        tab.append(a)
        a = Parent[a[0]][a[1]]

    tab.reverse()
    return tab

runtests( keep_distance )