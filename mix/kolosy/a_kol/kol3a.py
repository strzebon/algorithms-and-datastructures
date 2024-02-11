from kol3atesty import runtests
from queue import PriorityQueue

def spacetravel( n, E, S, a, b ):
    G = [[] for _ in range(n+1)]
    for u,v,t in E:
        G[u].append([v,t])
        G[v].append([u,t])
    for v in S:
        G[v].append([n,0])
        G[n].append([v,0])

    Visited = [False for _ in range(n+1)]
    D = [10**10 for _ in range(n+1)]
    D[a] = 0
    Q = PriorityQueue()
    Q.put((0,a))

    while not Q.empty():
        d,u = Q.get()
        if u == b:
            return d
        if not Visited[u]:
            Visited[u] = True
            for v, w in G[u]:
                if D[v] > d + w:
                    D[v] = d + w
                    Q.put((D[v],v))

    return None
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )