
def buty(G, s, w):
    #print(G)
    n = len(G)
    Visited = [[False for j in range(2)] for i in range(n)]
    D = [[10**10 for j in range(2)] for i in range(n)]
    D[s][0] = 0
    D[s][1] = 0

    d = 0
    u = s
    used = 0
    while u is not None:
        Visited[u][used] = True
        for v in range(n):
            if G[u][v] != 0 and D[v][0] > d + G[u][v]:
                D[v][0] = d + G[u][v]

        if not used:
            for v in range(n):
                if G[u][v] != 0:
                    for x in range(n):
                        if G[v][x] != 0 and D[x][1] > d + max(G[u][v], G[v][x]):
                            D[x][1] = d + max(G[u][v], G[v][x])

        d = 10**10
        u = None
        used = -1
        for i in range(n):
            for j in range(2):
                if not Visited[i][j] and d > D[i][j]:
                    d = D[i][j]
                    u = i
                    used = j


    #print(D)
    return min(D[w][0], D[w][1])



G=[[0, 1, 200, 200, 200, 200],
 [1, 0, 2, 200, 200, 200],
 [200, 2, 0, 40, 200, 200],
 [200, 200, 40, 0, 40, 200],
 [200, 200, 200, 40, 0, 117],
 [200, 200, 200, 200, 117, 0]]

# G = [
#     [0,1,0,0,0],
#     [1,0,1,0,0],
#     [0,1,0,7,0],
#     [0,0,7,0,8],
#     [0,0,0,8,0],
#      ]

print(buty(G, 0, 3))

