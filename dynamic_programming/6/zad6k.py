from zad6ktesty import runtests 

def f(S, F, i):
    if i == -1: return 1
    if F[i] != -1: return F[i]
    F[i] = 0
    if S[i] != '0': F[i] += f(S, F, i-1)
    if S[i-1] != '0' and int(S[i-1:i+1]) <= 26: F[i] += f(S, F, i-2)
    return F[i]


def haslo ( S ):
    n = len(S)
    if S[0] == '0': return 0
    # for i in range(n-1):
    #     if S[i] == S[i+1] == '0': return 0
    F = [-1 for _ in range(n)]
    F[0] = 1
    # if S[1] == '0' or int(S[0:2]) > 26: F[1] = 1
    # else: F[1] = 2
    return f(S, F, n-1)

runtests ( haslo )