from zad3testy import runtests
from queue import PriorityQueue

def dijkstra(G, s):
    n = len(G)
    Visited = [False for _ in range(n)]
    D = [10**10 for _ in range(n)]
    D[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))
    while not Q.empty():
        d, u = Q.get()
        if not Visited[u]:
            Visited[u] = True
            for v, w in G[u]:
                if D[v] > d + w:
                    D[v] = d + w
                    Q.put((D[v], v))

    return D



def paths(G,s,t):
    n = len(G)
    D1 = dijkstra(G, s)
    D2 = dijkstra(G, t)
    d = D1[t]
    counter = 0
    for u in range(n):
        for v, w in G[u]:
            if D1[u] + w + D2[v] == d or D1[v] + w + D2[u] == d:
                counter += 1

    return counter//2

runtests( paths )


