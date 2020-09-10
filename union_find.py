"""
Detect connected components using union-find
"""
def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]] # path compression
        u = parent[u]
    return u

def union(u,v):
    root_u = find(u)
    root_v = find(v)
    # if they are equal, then they were already linked
    if root_u != root_v:
        parent[root_u] = root_v
    return True

graph  = [[1,2],[1,3],[2,3]]
parent = [x for x in range(3)]

#graph = [[2,1],[2,3],[4,2],[5,3]]
#parent = [x for x in range(5)]

def count_components(graph):
    for edge in graph:
        union(edge[0]-1, edge[1]-1)

    return len({find(x) for x in parent})

print(count_components(graph))


