time = 0

def dfs(G, D, Low, P):
    n = len(G)
    Visited = [False for _ in range(n)]
    for u in range(n):
        if not Visited[u]:
            dfs_visit(G, D, Low, P, Visited, u)

def dfs_visit(G, D, Low, P, Visited, u):
    global time
    time += 1
    Visited[u] = True
    D[u] = time
    Low[u] = time
    for v in G[u]:
        if not Visited[v]:
            P[v] = u
            dfs_visit(G, D, Low, P, Visited, v)
            Low[u] = min(Low[u], Low[v])
        else:
            if v != P[u]:
                Low[u] = min(Low[u], D[v])


def mosty(G):
    n = len(G)
    D = [-1 for _ in range(n)]
    Low = [10**10 for _ in range(n)]
    P = [None for _ in range(n)]
    dfs(G, D, Low, P)
    tab = []
    for v in range(1, n):
        if D[v] == Low[v]:
            tab.append((v, P[v]))
    print(D)
    print(Low)
    print(tab)
    return tab
# a=0 b=1 c=2 d=3 e=4 f=5 g=6 h=7
G = [[1,6], [0,2], [1,3,6], [2,4,5], [3,5], [3,4], [0,2,7], [6]]
mosty(G)