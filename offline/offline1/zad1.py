# Witold Strzeboński
# Dla k>9 wykorzystuję algorytm sortowania przez scalanie. Najpierw sortuję (merge sort) k pierwszych elementów. Póżniej w pętli sortuję k następnych elementów
# i scalam z k elementami poprzedzającymi.
# Dla k <=9 wykorzystuję algorytm sortowania przez wstawianie. Napierw sortuję (merge sort) k pierwszych elementów. Później w pętli każdy następny element wstawiam
# w odpowiednie miejsce w ciągu k elmentów poprzedzających
# Złożoność:
# dla k = Θ(1) - Θ(n)
# dla k = Θ(log n) - Θ(n*log(logn))
# dla k = Θ(n) - Θ(n*logn)

from zad1testy import Node, runtests

def merge(l1, l2):
    first = Node()
    p = first
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    if l1 is None:
        p.next = l2
    else:
        p.next = l1
    return first.next

def merge_sort(p,k):
    heads = [p]
    for _ in range(k-1):
        if p.next is None:
            break
        if p.val > p.next.val:
            heads.append(p.next)
            temp = p.next
            p.next = None
            p = temp
        else:
            p = p.next
    x = p.next
    p.next = None
    while len(heads) > 1:
        heads2 = []
        while len(heads) > 1:
            merged = merge(heads[0], heads[1])
            heads2.append(merged)
            heads = heads[2:]
        heads2.extend(heads)
        heads = heads2

    return heads[0], x

def SortH(p,k):
    if k > 9:
        a = merge_sort(p,k+1)
        p1 = a[0]
        p2 = a[1]
        first = a[0]

        while p2 is not None:
            a = merge_sort(p2,k)
            p2 = a[0]
            p1 = merge(p1,p2)
            for _ in range(k):
                p1 = p1.next
            p2 = a[1]
        return first

    else:
        first = Node()
        a = merge_sort(p, k)
        first.next = a[0]
        p = a[1]
        r = first
        while p is not None:
            q = r
            while q.next is not None and q.next.val < p.val:
                q = q.next
            temp = p.next
            p.next = q.next
            q.next = p
            p = temp
            r = r.next

        return first.next

runtests( SortH )
