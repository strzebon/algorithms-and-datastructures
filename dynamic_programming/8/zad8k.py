from zad8ktesty import runtests 

def f(F, s, t, i, j):
    if i == len(s): return len(t) - j
    if j == len(t): return len(s) - i
    if F[i][j] != -1: return F[i][j]
    if s[i] == t[j]:
        F[i][j] = f(F, s, t, i+1, j+1)
        return F[i][j]
    F[i][j] = 1 + min(f(F, s, t, i, j+1), f(F, s, t, i+1, j), f(F, s, t, i+1, j+1))
    return F[i][j]




def napraw ( s, t ):
    F = [[-1 for j in range(len(t))] for i in range(len(s))]
    return f(F, s, t, 0, 0)

runtests ( napraw )