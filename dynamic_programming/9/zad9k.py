from zad9ktesty import runtests

def f(F, Parent, P, g, d, i):
    if i == -1: return True
    if F[g][d][i] is not None: return F[g][d][i]
    if P[i] <= g and f(F, Parent, P, g-P[i], d, i-1):
        #Parent[g][d][i] = (g-P[i], d, i-1, "g")
        Parent[i] = "g"
        F[g][d][i] = True
        return True
    if P[i] <= d and f(F, Parent, P, g, d-P[i], i-1):
        #Parent[g][d][i] = (g, d-P[i], i-1, "d")
        Parent[i] = "d"
        F[g][d][i] = True
        return True

    F[g][d][i] = False
    return False

def prom(P, g, d):
    n = len(P)
    F = [[[None for i in range(n)] for d_ in range(d+1)] for g_ in range(g+1)]
    #Parent = [[[[None for x in range(2)] for i in range(n)] for d_ in range(d+1)] for g_ in range(g+1)]
    Parent = [None for _ in range(n)]
    for i in range(n-1, -1, -1):
        if f(F, Parent, P, g, d, i): break
    else: return []
    #print(i)
    x = Parent[i]
    tab = []
    for j in range(i,-1,-1):
        #print(i)
        #print(Parent[g][d][i])
        if Parent[j] == x: tab.append(j)
        #g, d, i = Parent[g][d][i]

    tab.reverse()
    return tab

runtests ( prom )