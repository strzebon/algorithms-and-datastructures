# Witold Strzeboński
# Dla każdej pary miast dodaję do grafu wierzchołek, który pełni rolę ujścia, dodaję krawędzie z tych 2 miast do ujścia o przepustowości inf
# i wykonuję algorytm Edmondsa - Karpa. Rozwiązaniem jest maksimum z wszystkich maksymalnych przepływów.
# Złożoność czasowa: O(V^3 * E^2)


from zad9testy import runtests
from collections import deque

def bfs(S,R,s,n):
    Visited = [False for _ in range(n+1)]
    Parent = [-1 for _ in range(n+1)]
    Visited[s] = True
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in S[u]:
            if not Visited[v] and R[u][v] > 0:
                Visited[v] = True
                Parent[v] = u
                if v == n: return Parent
                Q.append(v)
    #print(2)
    return None

def maxflow( G,s ):
    #print(G)
    maks = 0
    n = -1
    for u,v,_ in G:
        n = max(n,u,v)
    n += 1
    S = [[] for _ in range(n+1)]
    R_original = [[0 for v in range(n+1)] for u in range(n+1)]
    for u,v,c in G:
        S[u].append(v)
        S[v].append(u)
        R_original[u][v] = c

    #print(S)
    #print(R_original)
    for u in range(n):
        if u == s: continue
        for v in range(u+1,n):
            if v==s: continue
            S[u].append(n)
            S[v].append(n)
            #R = deepcopy(R_original)
            R = [t.copy() for t in R_original]
            #R = [R_original[i].copy() for i in range(n+1)]
            #R = [[R_original[a][b] for b in range(n + 1)] for a in range(n + 1)]
            # for a, b, c in G:
            #     R[a][b] = c
            R[u][n] = 10**10
            R[v][n] = 10**10
            capacity = 0
            Parent = bfs(S, R, s, n)
            #print(1)
            while Parent is not None:
                #print(0)
                minn = 10**10
                x = n
                while x != s:
                    minn = min(minn, R[Parent[x]][x])
                    x = Parent[x]
                x = n
                while x != s:
                    R[Parent[x]][x] -= minn
                    R[x][Parent[x]] += minn
                    x = Parent[x]
                capacity += minn
                Parent = bfs(S, R, s, n)

            maks = max(maks, capacity)

    return maks

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )