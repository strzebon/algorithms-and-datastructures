# Witold Strzeboński
# Najlepsza trasa będzie zawierać maksymalnie jeden lot, ponieważ gdyby były 2 loty, np. z A do B i z C do D to bardziej opłacałoby się
# wykonać jeden lot z A do D. Rozwiązaniem problemu jest algorytm Dijkstry z jedną modyfikacją. Jak wyjmiemy wierzchołek u z kolejki,
# to dodatkowo sprawdzamy, czy wykorzystaliśmy już jakiś lot, żeby się dostać do u. Jeżeli nie, to sprawdzamy dla każdego wierzchołka v,
# czy opłaca nam się lecieć z u do v (jeżeli tak to uwzględniamy to w tablicy lotów (Counter)). Wynikiem jest D[t].
# O(mlog(n))


from kol3btesty import runtests
from queue import PriorityQueue


def airports( G, A, s, t ):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    Visited = [False for _ in range(n)]
    #Parent = [None for _ in range(n)]
    Counter = [0 for _ in range(n)]
    D = [A[s] + A[i] for i in range(n)]
    D[s] = 0
    Q = PriorityQueue()
    for i in range(n):
        Q.put((D[i], i))
    while not Q.empty():
        _, u = Q.get()
        if u==t: return D[t]
        if not Visited[u]:
            Visited[u] = True
            for v, c in G[u]:
                if not Visited[v]:
                    if D[u]+c < D[v]:
                        D[v] = D[u]+c
                        #Parent[v] = u
                        Q.put((D[v], v))
            if Counter[u] == 0:
                for v in range(n):
                    if not Visited[v]:
                        if D[u] + A[u] + A[v] < D[v]:
                            D[v] = D[u] + A[u] + A[v]
                            #Parent[v] = u
                            Counter[v] = Counter[u] + 1
                            Q.put((D[v], v))
    # x = t
    # while x != None:
    #     print(x, " ")
    #     x = Parent[x]
    return D[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )