class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)

        # Map course -> pre-req as the adjacency list
            # Think about how it backtracks when call stack pops
            # We visit courses as deep as possible after visiting it pops, and we add that deepest pre-req node first
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()
        done = set()
        #! Sets aren't ordered in Python so we use a list
        order = []

        def dfs(crs):
            if crs in visit:
                return False
            if crs in done:
                return True
            
            visit.add(crs)

            # visit the pre-requisites as deep as possible
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            # We backtrack here. Pre-requisites will be added first in the order.
            visit.remove(crs)
            done.add(crs)
            order.append(crs)

            return True
        
        # Visit all courses in course schedule
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return order
