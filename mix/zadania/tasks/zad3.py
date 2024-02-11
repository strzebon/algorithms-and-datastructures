from zad3testy import runtests

def dfs_visit(Visited, tab, G, u):
    n = len(G)
    Visited[u] = True
    for v in range(n):
        if G[u][v] == 1 and not Visited[v]:
            dfs_visit(Visited, tab, G, v)
    tab.append(u)

def tasks(T):
    n = len(T)
    Visited = [False for _ in range(n)]
    tab = []
    for u in range(n):
        if not Visited[u]:
            dfs_visit(Visited, tab, T, u)

    tab.reverse()
    return tab

runtests( tasks )
