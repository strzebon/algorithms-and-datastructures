# Witold Strzeboński
# Znajduję najkrótszą ścieżkę z s do t (bfs). Visited(v) oznacza liczbę krawędzi dochodzących do v zawierających się w najkrótszych ścieżkach z s do t.
# Kandydaci na rozwiązanie to krawędź (parent(v), v), gdzie visited(v) = 1 i visited(child) = 1. Za pomocą bfs sprawdzam czy najkrótsza ścieżka w grafie bez kandydata będzie dłuższa.
# Jeżeli tak to kandydat jest rozwiązaniem.
# Złożoność czasowa O((V+E)*E)

from zad6testy import runtests
from collections import deque

def bfs(G,s,t):
    n = len(G)
    Visited = [False for _ in range(n)]
    D = [-1 for _ in range(n)]
    D[s] = 0
    Parent = [[] for _ in range(n)]
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not Visited[v]:
                Visited[v] = True
                Parent[v].append(u)
                D[v] = D[u] + 1
                Q.append(v)
            elif D[v] == D[u] + 1: Parent[v].append(u)
    return Parent

def longer( G, s, t ):
    Parent = bfs(G,s,t)
    n = len(G)
    Visited = [False for _ in range(n)]
    D = [-1 for _ in range(n)]
    D[t] = 0
    Q = deque()
    Q.append(t)
    fala = 0
    counter = 0
    prev = t
    while Q:
        u = Q.popleft()
        if D[u] > fala:
            if counter == 1: return prev, u
            fala += 1
            prev = u
            counter = 0
        counter += len(Parent[u])
        for v in Parent[u]:
            if not Visited[v]:
                Visited[v] = True
                D[v] = D[u] + 1
                Q.append(v)

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )