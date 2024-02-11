time = 0

def dfs(G):
    n = len(G)
    Visited = [False for _ in range(n)]
    T = [-1 for _ in range(n)]

    for u in range(n):
        if not Visited[u]:
            dfs_visit(G, Visited, T, u)

    return T

def dfs_visit(G, Visited, T, u):
    global time
    Visited[u] = True

    for v in G[u]:
        if not Visited[v]:
            dfs_visit(G, Visited, T, v)

    T[time] = u
    time += 1


def dfs_2(G, T):
    n = len(G)
    Visited = [False for _ in range(n)]
    S = []

    for i in range(n-1, -1, -1):
        u = T[i]
        if not Visited[u]:
            s = []
            dfs_visit_2(G, Visited, s, u)
            S.append(s)

    return S


def dfs_visit_2(G, Visited, s, u):
    Visited[u] = True
    s.append(u)

    for v in G[u]:
        if not Visited[v]:
            dfs_visit_2(G, Visited, s, v)


def s_s_s(G):
    T = dfs(G)
    #print(T)
    n = len(G)
    G_2 = [[] for _ in range(n)]

    for i in range(n):
        for j in G[i]:
            G_2[j].append(i)

    return dfs_2(G_2, T)


G = [[1], [2,4], [0,9], [4,6], [5], [3], [5], [9], [7,3], [10], [8,5]]
print(s_s_s(G))
