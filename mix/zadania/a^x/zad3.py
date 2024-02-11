from zad3testy import runtests
import math

def bubble_sort(T):
    n = len(T)
    for i in range(n-1):
        changed = False
        for j in range(n-1-i):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
                changed = True
        if not changed: return

def insertion_sort(T):
    n = len(T)
    for i in range(1, n):
        key = T[i]
        j = i-1
        while j >= 0 and key < T[j]:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key
    
def fast_sort(tab, a):
    #bubble_sort(tab)
    #insertion_sort(tab)
    n = len(tab)
    T = [[] for _ in range(n)]
    step = 1/n
    for c in tab:
        x = math.log(c, a)
        if x == 1: T[n-1].append(c)
        else:
            j = int(x/step)
            T[j].append(c)

    i = 0
    for t in T:
        insertion_sort(t)
        for el in t:
            tab[i] = el
            i += 1
    #print(T)
    return tab



runtests( fast_sort )
