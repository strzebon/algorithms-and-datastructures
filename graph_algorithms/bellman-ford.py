def b_f(G, s, n):
    D = [10**10 for _ in range(n)]
    Parent = [None for _ in range(n)]
    D[s] = 0
    for _ in range(n-1):
        for w,u,v in G:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                Parent[v] = u
    for w,u,v in G:
        if D[v] > D[u] + w: return False

    print(D)
    return True

G = [(-1,1,3), (1,5,6), (2,6,7), (1,0,1), (2,2,0), (3,4,1), (4,4,5), (-1,3,4), (2,3,5), (100,6,8), (5,5,7), (3,3,2)]
print(b_f(G,0, 9))