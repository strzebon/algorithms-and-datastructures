from zad1testy import runtests

def b_s(E, x):
    l = 0
    p = len(E)-1
    while l <= p:
        i = (l+p) // 2
        if E[i][0] < x: l = i+1
        elif E[i][0] > x: p = i-1
        else: break
    else: return None
    while i >= 0 and E[i][0] == x: i -= 1
    return i+1

def dfs(E, Visited, n, u):
    #print(u)
    if u == n-1:
        Visited[u] = 1
        return
    Visited[u] = -1
    #i = 0
    #while i < len(E) and E[i][0] < u: i += 1
    i = b_s(E, u)
    if i is not None:
        while i < len(E) and E[i][0] == u:
            v = E[i][1]
            if Visited[v] == 0:
                dfs(E, Visited, n, v)

            if Visited[v] == 1: Visited[u] = 1
            i += 1

def intuse(I, x, y):
    n = y - x + 1
    E = []
    for a, b in I:
        if x <= a and b <= y:
            E.append((a-x, b-x))
    E.sort()
    Visited = [0 for _ in range(n)]
    dfs(E, Visited, n, 0)
    #print(44)
    tab = []
    for i in range(len(I)):
        a, b = I[i]
        if x <= a and b <= y and Visited[a-x] == 1 and Visited[b-x] == 1:
            tab.append(i)

    return tab

runtests(intuse)


