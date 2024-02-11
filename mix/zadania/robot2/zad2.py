from zad2testy import runtests
from queue import PriorityQueue

def robot( L, A, B ):
    b, a = A
    y, x = B
    w = len(L)
    k = len(L[0])
    Visited = [[[[False for p in range(3)] for o in range(4)] for j in range(k)] for i in range(w)]
    D = [[[[10**10 for p in range(3)] for o in range(4)] for j in range(k)] for i in range(w)]
    D[a][b][0][0] = 0
    Q = PriorityQueue()
    Q.put((0,a,b,0,0))
    T = [60, 40, 30]

    while not Q.empty():
        d, i, j, o, p = Q.get()
        if i == x and j == y: return d
        if not Visited[i][j][o][p]:
            Visited[i][j][o][p] = True
            if D[i][j][(o+1)%4][0] > d + 45:
                D[i][j][(o+1)%4][0] = d + 45
                Q.put((d+45, i, j, (o+1)%4, 0))
            if D[i][j][(o-1)%4][0] > d + 45:
                D[i][j][(o-1)%4][0] = d + 45
                Q.put((d+45, i, j, (o-1)%4, 0))

            p_ = min(2, p+1)
            if o == 0 and L[i][j+1] != 'X' and D[i][j+1][o][p_] > d + T[p]:
                D[i][j + 1][o][p_] = d + T[p]
                Q.put((d+T[p], i, j+1, o, p_))

            if o == 1 and L[i+1][j] != 'X' and D[i+1][j][o][p_] > d + T[p]:
                D[i+1][j][o][p_] = d + T[p]
                Q.put((d+T[p], i+1, j, o, p_))

            if o == 2 and L[i][j-1] != 'X' and D[i][j-1][o][p_] > d + T[p]:
                D[i][j-1][o][p_] = d + T[p]
                Q.put((d+T[p], i, j-1, o, p_))

            if o == 3 and L[i-1][j] != 'X' and D[i-1][j][o][p_] > d + T[p]:
                D[i-1][j][o][p_] = d + T[p]
                Q.put((d+T[p], i-1, j, o, p_))

    return None

    
runtests( robot )


