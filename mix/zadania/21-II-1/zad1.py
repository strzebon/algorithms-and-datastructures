from zad1testy import runtests

def f(P, Temp, W, a, k):
    b, i = P[a][k]
    Temp.append(i)
    if b == len(P):
        for j in Temp:
            if j not in W: W.append(j)
        return
    for j in range(len(P[b])):
        f(P, Temp, W, b, j)
        Temp.pop()

def intuse( I, x, y ):
    n = y-x
    P = [[] for _ in range(n)]
    for i in range(len(I)):
        a, b = I[i]
        if x <= a and b <= y:
            P[a-x].append((b-x, i))

    W = []
    for j in range(len(P[0])):
        f(P, [], W, 0, j)
    print(W)
    return W

    
runtests( intuse )


