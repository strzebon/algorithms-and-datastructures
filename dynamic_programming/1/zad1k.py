from zad1ktesty import runtests

def roznica( S ):
    #Tutaj proszę wpisać własną implementację
    # maks = -1
    # s = 0
    # for x in S:
    #     if x == '0':
    #         s += 1
    #         maks = max(maks, s)
    #     else:
    #         s -= 1
    #         if s < 0: s = 0

    n = len(S)
    F = [-1 for _ in range(n)]
    if S[0] == '0': F[0] = 1
    for i in range(1, n):
        if S[i] == '0': x = 1
        else: x = -1
        F[i] = max(x, x + F[i-1])

    return max(F)

runtests ( roznica )