# Witold Strzeboński
# Znajduję najkrótszą ścieżkę z s do t (bfs). Visited(v) oznacza liczbę krawędzi dochodzących do v zawierających się w najkrótszych ścieżkach z s do t.
# Kandydaci na rozwiązanie to krawędź (parent(v), v), gdzie visited(v) = 1 i visited(child) = 1. Za pomocą bfs sprawdzam czy najkrótsza ścieżka w grafie bez kandydata będzie dłuższa.
# Jeżeli tak to kandydat jest rozwiązaniem.
# Złożoność czasowa O((V+E)*E)

from zad6testy import runtests
import collections

class W:
    def __init__(self):
        self.d = -1
        self.visited = 0
        self.parent = None
def bfs(G,s,t):
    n = len(G)
    q = collections.deque()
    d = [-1 for i in range(n)]
    d[s] = 0
    q.append(s)
    while q:
        u = q.popleft()
        if u == t: break
        for v in G[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                q.append(v)
    return d[t]

def longer( G, s, t ):
    n = len(G)
    q = collections.deque()
    w = [W() for i in range(n)]
    w[s].d = 0
    w[s].visited = 1
    q.append(s)
    while q:
        u = q.popleft()
        if u == t: break
        for v in G[u]:
            if w[v].visited == 0:
                w[v].visited = 1
                w[v].d = w[u].d + 1
                w[v].parent = u
                q.append(v)
            elif w[u].d + 1 == w[v].d:
                w[v].visited += 1
    if w[t].visited == 0: return None
    x = t
    p = 1
    while x != s:
        if w[x].visited == 1 and p == 1:
            T = G.copy()
            T[x].remove(w[x].parent)
            T[w[x].parent].remove(x)
            d = bfs(T, s, t)
            if d > w[t].d or d == -1 : return w[x].parent, x
        p = w[x].visited
        x = w[x].parent
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )