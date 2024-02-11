from queue import PriorityQueue

def prim(G):
    n = len(G)
    Visited = [False for _ in range(n)]
    Parent = [None for _ in range(n)]
    W = [10**10 for _ in range(n)]
    W[0] = 0
    Q = PriorityQueue()
    Q.put((0,0))
    counter = 0
    while not Q.empty():
        _, t = Q.get()
        #print(_,t)
        if not Visited[t]:
            Visited[t] = True
            counter += 1
            for w, u in G[t]:
                if not Visited[u] and W[u] > w:
                    W[u] = w
                    Parent[u] = t
                    Q.put((w,u))
            if counter == n-1: break

    tab = []
    for v in range(1,n):
        tab.append((v,Parent[v]))
    return tab

A = [(1,1,3), (1,5,6), (2,6,7), (1,0,1), (2,2,0), (3,4,1), (4,4,5), (1,3,4), (2,3,5), (100,6,8), (5,5,7), (3,3,2)]
n = 9
G = [[] for _ in range(n)]
for w, u, v in A:
    G[u].append([w,v])
    G[v].append([w,u])
#print(G)
print(prim(G))
#[(0, 1), (1, 3), (3, 4), (5, 6), (2, 0), (3, 5), (6, 7), (6, 8)]