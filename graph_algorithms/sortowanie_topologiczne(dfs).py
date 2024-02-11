def dfs(G):
    n = len(G)
    Visited = [False for _ in range(n)]
    T = []
    for u in range(n):
        if not Visited[u]:
            dfs_visit(G, Visited, T, u)
    T.reverse()
    return T


def dfs_visit(G, Visited, T, u):
    Visited[u] = True
    for v in G[u]:
        if not Visited[v]:
            dfs_visit(G, Visited, T, v)
    T.append(u)

# a=0 b=1 c=2 d=3 e=4 f=5 g=6
G = [[5,1,2], [4,2], [], [], [3,6], [4], []]
print(dfs(G))
