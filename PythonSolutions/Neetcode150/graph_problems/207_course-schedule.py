from collections import defaultdict

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
            # to allow for other paths to explore it anew.
            visited.remove(crs)
            # Clear the prerequisites to mark this course as "completable" since there are no more prerequisites left
            preMap[crs] = []

            return True

        # Try to complete all courses. If any course can't be completed, return False.
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        # If we can complete all courses, return True.
        return True