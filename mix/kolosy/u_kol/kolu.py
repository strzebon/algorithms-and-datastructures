from kolutesty import runtests

def swaps( disk, depends ):
    # tu prosze wpisac wlasna implementacje
    n = len(disk)
    counter = 0
    Z = [False for _ in range(n)]
    d = 'A'
    c = 0
    while counter < n:
        i = 0
        while i < n:
            if not Z[i] and disk[i] == d:
                for j in depends[i]:
                    if not Z[j]:
                        i += 1
                        break
                else:
                    #print(i)
                    Z[i] = True
                    counter += 1
                    i = 0
            else:
                i += 1

        c += 1
        if d == 'A':
            d = 'B'
        else:
            d = 'A'

    minn = c

    counter = 0
    Z = [False for _ in range(n)]
    d = 'B'
    c = 0
    while counter < n:
        i = 0
        while i < n:
            if not Z[i] and disk[i] == d:
                for j in depends[i]:
                    if not Z[j]:
                        i += 1
                        break
                else:
                    Z[i] = True
                    counter += 1
                    i = 0
            else:
                i += 1

        c += 1
        if d == 'A':
            d = 'B'
        else:
            d = 'A'

    minn = min(minn, c)

    return minn-1

disk = ['A','A','B','B']
depends = [[2,3],[],[1,3],[1]]
#print(swaps(disk, depends))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( swaps, all_tests = True )

