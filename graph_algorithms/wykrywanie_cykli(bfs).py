from collections import deque


def is_cyclic(G):
    n = len(G)
    Q = deque()
    Visited = [False for _ in range(n)]
    Parent = [None for _ in range(n)]
    Visited[0] = True
    Q.appendleft(0)
    while Q:
        u = Q.pop()
        for v in G[u]:
            if Visited[v]:
                if v != Parent[u]:
                    return True
            else:
                Visited[v] = True
                Parent[v] = u
                Q.appendleft(v)
    return False


G = [[1,2], [0,4], [0,3], [2], [1,5], [4,6], [5,7], [6]]
print(is_cyclic(G))