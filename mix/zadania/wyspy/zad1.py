from zad1testy import runtests
from queue import PriorityQueue

def f(x):
    T = [1, 5, 8]
    return T[x]

def g(x):
    if x == 1: return 0
    if x == 5: return 1
    return 2

def islands(G, A, B):
    n = len(G)
    Visited = [[False for k in range(3)] for i in range(n)]
    D = [[10**10 for k in range(3)] for i in range(n)]
    for k in range(3): D[A][k] = 0
    Q = PriorityQueue()
    for k in range(3):
        Q.put((0,A,k))

    while not Q.empty():
        d, u, s = Q.get()
        s_ = f(s)
        if not Visited[u][s]:
            Visited[u][s] = True
            for v in range(n):
                t_ = G[u][v]
                t = g(s_)
                if t_ != 0 and t_ != s_ and D[v][t] > d + t_:
                    D[v][t] = D[u][s] + t_
                    Q.put((D[v][t], v, t))

    return min(D[B][0], D[B][1], D[B][2])


        

runtests( islands ) 

def kintersect(A, k):
    interval = [(i, A[i][0], A[i][1]) for i in range(len(A))]
    interval.sort(key=lambda x: x[2], reverse=True)
    max_length = 0
    if k == 1:
        result = [0]
        for i in range(len(A)):
            if interval[i][2] - interval[i][1] > max_length:
                max_length = interval[i][2] - interval[i][1]
                result[0] = interval[i][0]
        return result
    result = []
    for i in range(len(A)):
        current = [interval[i][0]]
        for j in range(len(A)):
            if i != j and interval[j][1] <= interval[i][1] < interval[j][2]:
                current.append(interval[j][0])
                if len(current) == k:
                    actual_length = min(interval[j][2] - interval[i][1], interval[i][2] - interval[i][1])
                    if actual_length > max_length:
                        max_length = actual_length
                        result.clear()
                        result = [current[i] for i in range(k)]
                    break
    return result
