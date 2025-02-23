class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        # Create an adjacency list where courses -> prerequisites
            # crs is pointing to pre because it answers "what do I need to complete before taking the course"
                # Allows us to check what we need to complete first before taking a course
                # *Think about how it "backtracks", we complete the course when we backtrack so it goes backwards*
            # If we flip it around, it answers instead "what courses does this unlock"
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        completed, visited = set(), set()

        def dfs(crs):
            # Base case 1: Course has already been visited, cycle detected
            if crs in visited:
                return False
            
            # Base case 2: Course has already been completed, check for another course
            if crs in completed:
                return True
            
            # Visit the node
            visited.add(crs) # Add it to current visited path

            # Explore the neighbours (prereqs) of current course node
            for pre in preMap[crs]:
                # Pop stack entirely if a cycle is detected
                if not dfs(pre):
                    return False
            
            # Unvisit the node
            visited.remove(crs) # Remove it from current path
            completed.add(crs) # Add the course as completed now since we just visited it, "finishing" the course

            # Pop a true in the stack when no problems were found after backtracking
            return True
        
        # Run a topological sort on the adjacency list
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
        
        