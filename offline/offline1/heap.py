from zad1testy import Node, runtests

def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return (i-1)//2

def heapify(A, n, i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and A[l].val < A[max_ind].val: max_ind = l
    if r < n and A[r].val < A[max_ind].val: max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind)

def build_heap(A):
    n = len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A, n, i)

def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1,0,-1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)

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
    # if k<10:
    #     first = Node()
    #     a = merge_sort(p, k)
    #     first.next = a[0]
    #     p = a[1]
    #     r = first
    #     while p is not None:
    #         q = r
    #         while q.next is not None and q.next.val < p.val:
    #             q = q.next
    #         temp = p.next
    #         p.next = q.next
    #         q.next = p
    #         p = temp
    #         r = r.next
    #
    #     return first.next


    A = [0 for _ in range(k+1)]
    for i in range(k+1):
        if p is None:
            A = A[:i]
            break
        A[i] = p
        p = p.next

    build_heap(A)
    # for x in A:
    #     print(x.val, end=' ')
    first = A[0]
    q = first
    #print(p.val)
    while p is not None:
        A[0] = p
        p = p.next
        heapify(A, k+1, 0)
        q.next = A[0]
        q = q.next

    for i in range(len(A)-1,0,-1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)
        q.next = A[0]
        q = q.next

    q.next = None

    return first


runtests(SortH)