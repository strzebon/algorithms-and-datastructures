from kol2btesty import runtests

def f(A, T, L, F, used, i):
    if F[used][i] != -1: return F[used][i]

    if A[i][0] + T >= L:
        F[used][i] = 0
        return 0
    if not used and A[i][0] + 2*T >= L:
        F[used][i] = 0
        return 0

    minn = 10**10
    for j in range(i+1, len(A)):
        if A[j][0] > A[i][0] + T: break
        minn = min(minn, A[j][1] + f(A, T, L, F, used, j))

    if not used:
        for k in range(j, len(A)):
            if A[k][0] > A[i][0] + 2*T: break
            minn = min(minn, A[k][1] + f(A, T, L, F, 1, k))

    F[used][i] = minn
    return minn




def min_cost( O, C, T, L ):
    # tu prosze wpisac wlasna implementacje
    n = len(O)
    A = [0 for _ in range(n+1)]
    for i in range(n):
        A[i+1] = (O[i], C[i])
    A[0] = (0, 0)
    A.sort()
    F = [[-1 for i in range(n+1)] for used in range(2)]


    return f(A, T, L, F, 0, 0)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
