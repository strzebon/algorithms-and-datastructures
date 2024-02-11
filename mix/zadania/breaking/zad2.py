from zad2testy import runtests

time = 0

def dfs(G):
    n = len(G)
    D = [-1 for _ in range(n)]
    Low = [10**10 for _ in range(n)]
    P = [None for _ in range(n)]
    Visited = [False for _ in range(n)]
    tab = []
    dfs_visit(G, D, Low, P, Visited, 0, tab)
    return tab, P

def dfs_visit(G, D, Low, P, Visited, u, tab):
    global time
    time += 1
    Visited[u] = True
    D[u] = time
    Low[u] = time
    flag = False
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

def p_a(G):
    tab, P = dfs(G)
    counter = 0
    for v in G[0]:
        if P[v] == 0: counter += 1
    if counter >= 2: tab.append(0)
    return tab

def dfs2(G, s):
    n = len(G)
    Visited = [False for _ in range(n)]
    Visited[s] = True
    counter = 0
    for u in range(n):
        if not Visited[u]:
            dfs_visit2(Visited, G, u)
            counter += 1

    return counter

def dfs_visit2(Visited, G, u):
    Visited[u] = True
    for v in G[u]:
        if not Visited[v]:
            dfs_visit2(Visited, G, v)

def breaking(G):
    n = len(G)
    S = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if G[u][v]: S[u].append(v)

    G = S
    tab = p_a(G)
    print(tab)
    maks = 1
    w = None
    for x in tab:
        counter = dfs2(G, x)
        if maks < counter:
            maks = counter
            w = x

    return w



runtests( breaking )