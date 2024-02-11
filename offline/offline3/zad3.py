# Witold Strzeboński
# zwykły bucket sort
# złożoność czasowa O(n)
# złożoność pamięciowa O(n)

from zad3testy import runtests

def bucket_sort(T):
    n = len(T)
    A = [[] for _ in range(n)]
    for x in T:
        A[int(x)-1].append(x)
    i = 0
    for tab in A:
        for k in range(len(tab)):
            minn = n+1
            j_min = -1
            for j in range(k, len(tab)):
                if tab[j] < minn:
                    minn = tab[j]
                    j_min = j
            tab[k], tab[j_min] = tab[j_min], tab[k]
            T[i] = minn
            i += 1

def SortTab(T,P):
    bucket_sort(T)
    return T

runtests( SortTab )