def find(x, Parent):
    if Parent[x] != x:
        Parent[x] = find(Parent[x], Parent)
    return Parent[x]

def union(x, y, Parent, Rank):
    if Rank[x] > Rank[y]:
        Parent[y] = x
    else:
        Parent[x] = y
        if Rank[x] == Rank[y]:
            Rank[y] += 1

def Kruskal(G, n):
    Parent = [x for x in range(n)]
    Rank = [0 for _ in range(n)]
    G.sort()
    counter = 0
    tab = []
    for _, x, y in G:
        a = find(x, Parent)
        b = find(y, Parent)
        if a != b:
            union(a, b, Parent, Rank)
            tab.append((x, y))
            counter += 1
            if counter == n-1:
                return tab

G = [(1,1,3), (1,5,6), (2,6,7), (1,0,1), (2,2,0), (3,4,1), (4,4,5), (1,3,4), (2,3,5), (100,6,8), (5,5,7), (3,3,2)]
print(Kruskal(G, 9))

#[(0, 1), (1, 3), (3, 4), (5, 6), (2, 0), (3, 5), (6, 7), (6, 8)]