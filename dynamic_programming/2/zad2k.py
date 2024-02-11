from zad2ktesty import runtests

# def f(S,F,i,j):
#     if F[i][j] != -1: return F[i][j]
#     if i==j:
#         F[i][j] = 1
#         return 1
#     if i+1 == j:
#         if S[i] == S[j]:
#             F[i][j] = 2
#             return 2
#         else:
#             F[i][j] = -10**10
#             return -10**10
#
#     F[i][j] = max(f(S,F,i+1,j), f(S,F,i,j-1))
#     if S[i] == S[j]: F[i][j] = max(F[i][j], 2 + f(S,F,i+1,j-1))
#     return F[i][j]

def f(S,F,i,j):
    if F[i][j] != -1: return F[i][j]
    if i==j:
        F[i][j] = True
        return True
    if i+1 == j and S[i] == S[j]:
            F[i][j] = True
            return True
    if S[i] == S[j]:
        return f(S,F,i+1,j-1)
    else:
        F[i][j] = False
        return False


def palindrom( S ):
    #Tutaj proszę wpisać własną implementację
    n = len(S)
    F = [[-1 for j in range(n)] for i in range(n)]
    a = None
    b = None
    maks = 0
    for i in range(n):
        for j in range(i+1,n):
            if f(S, F, i, j) and j-i+1 > maks:
                maks = j-i+1
                a = i
                b = j
    if maks == 0: return ""
    return S[a:b+1]

runtests ( palindrom )