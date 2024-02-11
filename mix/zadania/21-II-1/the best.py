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

def b_s2(E, x):
    l = 0
    p = len(E)-1
    while l <= p:
        #print(0)
        i = (l+p) // 2
        if E[i][0] < x: l = i+1
        elif E[i][0] > x: p = i-1
        else: return i

    return None

def dfs(E, Visited, y, u):
    #print(u)
    u_ = b_s2(Visited, u)
    if u == y:
        Visited[u_][1] = 1
        return

    Visited[u_][1] = -1
    #i = 0
    #while i < len(E) and E[i][0] < u: i += 1
    i = b_s(E, u)
    if i is not None:
        while i < len(E) and E[i][0] == u:
            v = E[i][1]
            v_ = b_s2(Visited, v)
            if v_ is None:
                i += 1
                continue
            if Visited[v_][1] == 0:
                dfs(E, Visited, y, v)

            if Visited[v_][1] == 1: Visited[u_][1] = 1
            i += 1

def intuse(I, x, y):
    E = []
    for a, b in I:
        if x <= a and b <= y:
            E.append((a, b))
    E.sort()
    prev = -1
    Visited = []
    for a,b in E:
        if a != prev: Visited.append([a,0])
        prev = a
    Visited.append([y,0])

    dfs(E, Visited, y, x)
    #print(44)
    tab = []
    for i in range(len(I)):
        a, b = I[i]
        if x <= a and b <= y:
            a_ = b_s2(Visited, a)
            b_ = b_s2(Visited, b)
            if a_ is not None and b_ is not None and Visited[a_][1] == 1 and Visited[b_][1] == 1: tab.append(i)

    return tab

runtests(intuse)


