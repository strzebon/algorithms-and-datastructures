def dfs(G):
    n = len(G)
    Visited = [[0 for j in range(n)] for i in range(n)]
    T = []
    dfs_visit(G, Visited, T, 0)
    T.reverse()
    return T


def dfs_visit(G, Visited, T, u):
    for v in G[u]:
        if not Visited[u][v]:
            Visited[u][v] = 1
            Visited[v][u] = 1
            dfs_visit(G, Visited, T, v)
    T.append(u)

# a=0 b=1 c=2 d=3 e=4 f=5
G = [[1,2], [0,2,3,5], [0,1,3,5], [1,2,4,5], [3,5], [1,2,3,4]]
print(dfs(G))
