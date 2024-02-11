time = 0

def dfs(G, D, Low, P):
    n = len(G)
    Visited = [False for _ in range(n)]
    tab = []
    dfs_visit(G, D, Low, P, Visited, 0, tab)
    return tab

def dfs_visit(G, D, Low, P, Visited, u, tab):
    global time
    time += 1
    Visited[u] = True
    D[u] = time
    Low[u] = time
    flag  = False
    if u == 0: flag = True
    for v in G[u]:
        if not Visited[v]:
            P[v] = u
            dfs_visit(G, D, Low, P, Visited, v, tab)
            Low[u] = min(Low[u], Low[v])
            if not flag and Low[v] >= D[u]:
                tab.append(u)
                flag = True
        else:
            if v != P[u]:
                Low[u] = min(Low[u], D[v])


def punkty_artykulacji(G):
    n = len(G)
    D = [-1 for _ in range(n)]
    Low = [10**10 for _ in range(n)]
    P = [None for _ in range(n)]
    tab = dfs(G, D, Low, P)
    counter = 0
    for v in G[0]:
        if P[v] == 0: counter += 1
    if counter >= 2: tab.append(0)
    return tab

# a=0 b=1 c=2 d=3 e=4 f=5 g=6 h=7
G = [[1,6], [0,2], [1,3,6], [2,4,5], [3,5], [3,4], [0,2,7], [6]]
punkty_artykulacji(G)