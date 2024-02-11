# Witold Strzeboński
# Robię listę wszystkich możliwych krawędzi i sortuję po wagach.
# Dla każdej krawędzi wykonuję algorytm Kruskala, zakładając, że waga tej krawędzi jest minimalną wagą w minimalnym drzewie rozpinającym.
# Jeżeli znajdę mst to aktualizuję minn, a jeżeli nie, to kończę program, zwracając minn
# O(n^4*logn)

from zad8testy import runtests
from math import ceil, sqrt

def find(x, Parent):
    if Parent[x] != x:
        Parent[x] = find(Parent[x], Parent)
    return Parent[x]

def union(x, y, Rank, Parent):
    if Rank[x] > Rank[y]:
        Parent[y] = x
    else:
        Parent[x] = y
        if Rank[x] == Rank[y]:
            Rank[y] += 1

def b_time(x, y):
    return ceil(sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2))

def highway( A ):
    n = len(A)
    E = [(b_time(A[x],A[y]), x, y) for y in range(n) for x in range(y)]
    E.sort()
    minn = E[n-1][0]-E[0][0]
    for i in range(len(E)):
        Parent = [i for i in range(n)]
        Rank = [0 for _ in range(n)]
        x = E[i][1]
        y = E[i][2]
        union(x, y, Rank, Parent)
        first = i
        last = i
        licznik = 1
        for j in range(i+1,len(E)):
            if licznik == n-1:
                minn = min(minn, E[last][0] - E[first][0])
                break
            x = find(E[j][1],Parent)
            y = find(E[j][2],Parent)
            if x != y:
                union(x,y,Rank,Parent)
                licznik += 1
                last = j
        else: return minn
    return minn

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )