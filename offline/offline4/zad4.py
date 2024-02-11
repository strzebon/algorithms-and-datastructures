# Witold Strzeboński
# Sortuję rosnąco tablicę budynków względem "b" i tworzę tablicę indeksów, gdzie A[i] - numer indeksu i-tego elementu posortowanej tablicy w pierwotnej tablicy
# Implementuję funkcję rekurencyjną ze spamiętywaniem f(i,k), która wyznacza maksymalną pojemność budynków w zakresie od 0 do i, biorąc i-ty budynek, mając limit łącznej ceny k.
# Maksymalną pojemnością, jaką możemy uzyskać jest max{F[i]][p], gdzie 0 <= i <= n-1}
# Na koniec odtwarzam rozwiązanie zawierające odpowiednie numery indeksów
# Złożoność czasowa O(pn^2)

from zad4testy import runtests

def partition(T, p, r, A):
    x = T[r]
    i = p - 1
    for j in range(p,r):
        if T[j][2] < x[2]:
            i += 1
            T[i], T[j] = T[j], T[i]
            A[i], A[j] = A[j], A[i]
    T[i+1], T[r] = T[r], T[i+1]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(T, p, r, A):
    if p < r:
        q = partition(T, p, r, A)
        quick_sort(T, p, q-1, A)
        quick_sort(T, q+1, r, A)

def poj(x):
    return x[0]*(x[2]-x[1])

def f(i, k, T, F):
    if F[i][k] != -1: return F[i][k]
    maks = 0
    w = k-T[i][3]
    if w < 0:
        return 0

    for j in range(0, i):
        if T[j][2] < T[i][1]:
            maks = max(maks, f(j, w, T, F))
    F[i][k] = poj(T[i]) + maks
    return F[i][k]

def select_buildings(T,p):
    n = len(T)
    A = [i for i in range(n)]
    quick_sort(T, 0, n-1, A)
    F = [[-1 for k in range(p+1)] for i in range(n)]
    maks = 0
    index = -1
    for i in range(n):
        if maks < f(i, p, T, F):
            maks = f(i, p, T, F)
            index = i
    tab = [A[index]]
    while p - T[index][3] > 0:
        for i in range(index):
            if F[index][p] == F[i][p-T[index][3]] + poj(T[index]):
                p -= T[index][3]
                index = i
                tab.append(A[index])
                break
        else:
            break
    return tab

runtests(select_buildings)