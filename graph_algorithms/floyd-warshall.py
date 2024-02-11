def f_w(G):
    n = len(G)
    D = [G[i].copy() for i in range(n)]
    print(D)
    for k in range(n):
        for u in range(n):
            for v in range(n):
                D[u][v] = min(D[u][v], D[u][k] + D[k][v])

    return D

G = [[0,111,2,5], [3,0,99,3], [22,10**10,0,13],[10**10,10**10,100,0]]
print(f_w(G))