from zad11ktesty import runtests

# def f(F, T, b, i):
#     if F[b][i] != -1: return F[b][i]
#     F[b][i] = f(F, T, b, i-1)
#     if T[i] <= b:
#         F[b][i] = min(F[b][i], f(F, T, b-T[i], i-1))
#     return F[b][i]
#
# def kontenerowiec(T):
#     #Tutaj proszę wpisać własną implementację
#     n = len(T)
#     w = 0
#     for x in T:
#         w += x
#
#     F = [[-1 for i in range(n)] for b in range(w+1)]
#     for b in range(w+1):
#         F[b][0] = b
#     for b in range(T[0], w+1):
#         F[b][0] = b - T[0]
#
#     x = 2 * f(F, T, w//2, n-1)
#     if w % 2 == 1: x += 1
#
#     return x

def f(F, T, i, p1, p2):
    if i == -1: return abs(p1 - p2)
    if F[i][p1] != -1: return F[i][p1]
    F[i][p1] = min(f(F, T, i-1, p1 + T[i], p2), f(F, T, i-1, p1, p2 + T[i]))
    return F[i][p1]

def kontenerowiec(T):
    n = len(T)
    s = 0
    for x in T:
        s += x

    F = [[-1 for p in range(s+1)] for i in range(n)]
    return f(F, T, n-1, 0, 0)


runtests ( kontenerowiec )
    