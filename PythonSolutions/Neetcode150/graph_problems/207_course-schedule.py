class BetterSolution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Cycle is used to save nodes for the current path we are exploring
        # Completed is used to save nodes that are fully explored
            # Allows us to explore the last node during backtracking
            # For example, we can still go through the visit and unvisit of the DFS
        cycle, completed = set(), set()
        def dfs(crs):
            # Course has been completed, no cycles
            if crs in completed:
                return True
            # Cycle detected
            if crs in cycle:
                return False
            
            # Visit
            cycle.add(crs)
            # Explore
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # Unvisit (backtrack)
            cycle.remove(crs)
            completed.add(crs)

            return True
        
        ''' Topological Sorting, need to begin traversal through all nodes in adjacency list. Not just one node
         This is due to the need of checking if the beginning course can be completed and all prereqs can finish '''
        # Explore paths for all courses
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a mapping from each course to its list of prerequisites.
        preMap = defaultdict(list)
        # Set to keep track of courses visited during DFS to detect cycles.
        visited = set()

        # Build the prerequisite map.
            # Prerequisite is first in the array
            # Course is second
        # Rule states: must take course b1 first if you want to take course ai [a1, b1]
        for pre, crs in prerequisites:
            preMap[crs].append(pre)
        
        # Helper function to perform DFS on the course graph.
        def dfs(crs):
            # If a course has no more prerequisites, it can be completed.
            if preMap[crs] == []:
                return True
            # If we're visiting a course we've already visited, we've found a cycle.
            if crs in visited:
                return False
            
            # Mark the current course as visited.
            visited.add(crs)
            # Recursively visit all the prerequisites for the current course.
            for pre in preMap[crs]:
                if not dfs(pre):
                    # If any prerequisite can't be completed, this course can't be completed.
                    return False
            # After visiting all prerequisites for this course, remove it from visited
                # Allows us to backtrack to other paths (topological sorting)
            visited.remove(crs)
            # Clear the prerequisites to mark this course as "completable" since there are no more prerequisites left
            preMap[crs] = []

            return True

        ''' Topological Sorting, need to begin traversal through all nodes in adjacency list. Not just one node
         This is due to the need of checking if the beginning course can be completed and all prereqs can finish '''
        # Try to complete all courses. If any course can't be completed, return False.
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        # If we can complete all courses, return True.
        return True