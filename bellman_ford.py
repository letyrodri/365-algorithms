from math import floor

def bellman_ford_valid(ady_list, w, s):
    '''
    Description: Bellman-Ford Algorithm
                 (simple version, asumming valid application)
    Input: ady_list
           w      weights
           s      starting node

    Return: the position of e in sl
    
    '''
    N = len(ady_list)

    dist =[float("inf")]*N
    parent = [None]*N

    dist[s] = 0

    for i in range(N):
        for u in range(N):
            for v in ady_list[u]:
                if dist[v] > dist[u]+w[u][v]:
                    dist[v] = dist[u]+w[u][v]
                    parent[v] = u
    return dist, parent




