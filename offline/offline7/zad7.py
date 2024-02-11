# Witold Strzeboński
# Stosując algorytm dfs sprawdzam wszystkie możliwe ścieżki spełniające warunki na bramy. Gdy znajdę rozwiązanie, kończę wszystkie wywołane funkcje i odtwarzam rozwiązanie, stosując tablicę parentów.
# u - w którym mieście aktualnie jestem; k - z której bramy mogę skorzystać wyjeżdżając z miasta; s - ile miast odwiedziłem w danej ścieżce
# O(V!)

from zad7testy import runtests

def dfs_visit_0(G, Visited, Parent, u, k, s):
    Visited[u] = True
    if s == len(G) and 0 in G[u][k] and u in G[0][1]:
        Parent[0] = u
        #print("sdfsf")
        return True
    for v in G[u][k]:
        if not Visited[v]:
            Parent[v] = u
            if u in G[v][0]:
                if dfs_visit_0(G, Visited, Parent, v, 1, s+1): return True
            else:
                if dfs_visit_0(G, Visited, Parent, v, 0, s+1): return True
            Visited[v] = False
            Parent[v] = None

# def dfs_visit_1(G, Visited, Parent, u, k, s):
#     Visited[u] = True
#     if s == len(G) and 0 in G[u][k] and u in G[0][0]:
#         Parent[0] = u
#         #print("sdfsf")
#         return True
#     for v in G[u][k]:
#         if not Visited[v]:
#             Parent[v] = u
#             if u in G[v][0]:
#                 if dfs_visit_1(G, Visited, Parent, v, 1, s+1): return True
#             else:
#                 if dfs_visit_1(G, Visited, Parent, v, 0, s+1): return True
#             Visited[v] = False
#             Parent[v] = None

def droga( G ):
    n = len(G)
    Visited = [False for _ in range(n)]
    Parent = [None for _ in range(n)]
    if dfs_visit_0(G, Visited, Parent, 0, 0, 1):
        tab = [0]
        a = Parent[0]
        while a != 0:
            #print(a)
            tab.append(a)
            a = Parent[a]
        return tab
    # if dfs_visit_1(G, Visited, Parent, 0, 1, 1):
    #     tab = [0]
    #     a = Parent[0]
    #     while a != 0:
    #         #print(a)
    #         tab.append(a)
    #         a = Parent[a]
    #     return tab

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )