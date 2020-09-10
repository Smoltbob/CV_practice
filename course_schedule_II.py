class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
      
        def dfs(graph, course):
            color[course] = GRAY
            for n in graph[course]:
                if color[n] == WHITE:
                    dfs(graph, n)
                # found a cycle!
                if color[n] == GRAY:
                    return False
            color[course] = BLACK
            order.append(course)
            return True
            
        """
        Make graph structure
        """
        graph = defaultdict(list)
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
        
        """
        Initialize the traversal
        """
        WHITE = 1
        GRAY = 2
        BLACK = 3
        color = {n:WHITE for n in range(numCourses)}
        
        order = []
        for course in range(numCourses):
            if color[course] == WHITE:
                # if we found a cycle, break
                if not dfs(graph, course):
                    return []
                
       
        return order[::-1]
