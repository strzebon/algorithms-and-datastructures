from zad1testy import runtests

def dfs(G, Visited, n, u):
    #print(u)
    if u == n-1:
        Visited[u] = 1
        return
    Visited[u] = -1
    for v in G[u]:
        if Visited[v] == 0:
            dfs(G, Visited, n, v)

        if Visited[v] == 1: Visited[u] = 1


def intuse(I, x, y):
    n = y - x + 1
    G = [[] for _ in range(n)]
    for a, b in I:
        if x <= a and b <= y:
            G[a - x].append(b - x)
    #print(G)
    Visited = [0 for _ in range(n)]
    dfs(G, Visited, n, 0)
    #print(44)
    tab = []
    for i in range(len(I)):
        a, b = I[i]
        if x <= a and b <= y and Visited[a-x] == 1 and Visited[b-x] == 1:
            tab.append(i)

    return tab

runtests(intuse)


