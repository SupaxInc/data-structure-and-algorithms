class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { c: [] for c in range(0, numCourses) }

        # Using a completed will allow us to know which paths have been fully explored
            # Allows us to also add the last node when we backtrack
        cycle, completed = set(), set()

        order = []

        for pre, crs in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            # Check if there's a loop in the current DFS exploration stack
            if crs in cycle:
                return False
            # Check if the course has been completed
                # No prerequisites
                # Or course has been completed as we have already visited all prereqs and found no issues
            if crs in completed:
                return True

            cycle.add(crs) # Add to current cycle of the recursive stack 
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # Remove current cycle because we have backtracked
                # And need to traverse to another prerequisite path
            cycle.remove(crs) 
            completed.add(crs) # Add the course as completed since we've traversed to all prereqs
            order.append(crs)
            return True

        ''' Topological Sorting, need to begin traversal through all nodes in adjacency list. Not just one node
         This is due to the need of checking if the beginning course can be completed and all prereqs can finish '''
        for num in range(0, numCourses):
            if not dfs(num):
                return []
        
        # Reverse the order since the topological ordering is backwards
            # prerequisites[i] = [ai, bi] indicates that you must take course b1 first if you want to take course a1.
            # So our backtrack consists of popping the last course of the order
        return order[::-1]