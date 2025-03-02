class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)

        # Create an adjacency list where courses -> prerequisites
            # crs is pointing to pre because it answers "what do I need to complete before taking the course"
                # Allows us to check what we need to complete first before taking a course
                # *Think about how it "backtracks", we complete the course when we backtrack so it goes backwards*
            # If we flip it around, it answers instead "what courses does this unlock"
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited, completed = set(), set()
        order = []
        
        def dfs(crs):
            # Base case 1: Found a visited node in current path, cycle detected
            if crs in visited:
                return False

            # Base case 2: Found an already completed course
            if crs in completed:
                return True
            
            # Visit the course node
            visited.add(crs)

            # Explore all neighbours (prereqs) for current course node
            for pre in preMap[crs]:
                # Found an invalid path, pop the stack and return False
                if not dfs(pre):
                    return False
            
            # Unvisit the course node
                # Essentially "completing" the course, so we go backwards and explore other courses
            visited.remove(crs)
            completed.add(crs)

            # Add the ordering during unvisit, remember when we backtrack, we "complete" that course
            order.append(crs) 

            # All current paths valid return a True
            return True
            
        
        # Traverse all courses because there may be disconnected components
            # 1 DFS is not enough, this is why when we backtrack we unvisit the node so we can test the other courses in the case that its part of another graph
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return order