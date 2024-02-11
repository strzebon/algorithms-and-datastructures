from collections import deque


def czy_dwudzielny(G):
    n = len(G)
    Q = deque()
    Visited = [-1 for _ in range(n)]
    Visited[0] = 1
    Q.appendleft(0)
    while Q:
        u = Q.pop()
        c = (Visited[u]+1) % 2
        for v in G[u]:
            if Visited[v] != -1:
                if Visited[v] != c:
                    return None
            else:
                Visited[v] = c
                Q.appendleft(v)
    return Visited


G = [[1,2], [0,4], [5,3,0], [2,4], [3,1,5], [4,6,2], [5,7], [6]]
print(czy_dwudzielny(G))