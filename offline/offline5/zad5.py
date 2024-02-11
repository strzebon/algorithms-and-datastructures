# Witold Strzeboński
# Żeby przejechać całą trasę, potrzebuję zebrać co najmniej n-1 litrów ropy. Zbieram ropę z pola nr 0.
# Następnie, dopóki p (sumaryczna ilość zebranej ropy) nie będzie wynosić n-1, wstawiam do kolejki wszystkie pola z ropami do których aktualnie mogę dojechać
# i wyjmuję pole z maksymalną ilością ropy. Dodaję indeks tego pola do tablicy i zwiększam p. Po zakończeniu pętli sortuję tablicę indeksów.
# Złożoność czasowa: O(nlogn)

import queue

from zad5testy import runtests

def plan(T):
    n = len(T)
    q = queue.PriorityQueue()
    tab = [0]
    p = T[0]
    i = 1
    while p < n-1:
        while i < p+1:
            if T[i] > 0: q.put((-T[i], i))
            i += 1
        x = q.get()
        p -= x[0]
        tab.append(x[1])
    tab.sort()
    return tab

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )
