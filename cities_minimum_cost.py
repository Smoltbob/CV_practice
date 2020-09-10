def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        
        parent = [x for x in range(N)]
        
        def find(u):
            while u != parent[u]:
                u = parent[u]
            return u
        
        def union(u,v):
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return False
            parent[root_u] = root_v
            return True
        
        connections = sorted(connections, key = lambda x: x[2]) # nlogn + n^2
        total_cost = 0
        for city1, city2, cost in connections: 
            if union(city1-1, city2-1):
                total_cost += cost
                
        nb_cp = len({find(x) for x in range(N)})
        
        if nb_cp > 1:
            return -1
        else:
            return total_cost
