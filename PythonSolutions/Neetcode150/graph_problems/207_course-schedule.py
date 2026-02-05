class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        # Create the adjacent list graph where course is pointing to pre-req
            # This tells us: "To find what courses we need to complete for this course"
            # If we flip it (pre -> course): "What courses will this unlock?"
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set() # Current path
        done = set()  # Nodes that have been fully visited

        def dfs(crs):
            # Base case 1: Cycle detected
            if crs in visit:
                return False
            # Base case 2: Already visited in another cycle
            if crs in done:
                return True
            
            # Visit the course node and add it to current path
            visit.add(crs)

            # Go through all pre-requisites for the course and see if it can be completed
            for pre in preMap[crs]:
                # Check if a the pre-requisite is found in a visit making it impossible to finish the course
                if not dfs(pre):
                    return False
            
            # Remove course from visit after we have visited all nodes for this course
            visit.remove(crs)
            # Mark it as done since we have visited all pre-requisite nodes for this course
            done.add(crs)

            # Course was able to be completed, mark as true
            return True

        # Go through each node in the schedule
        for crs in range(numCourses):
            # If a cycle was detected then we just couldn't finish the course plan
            if not dfs(crs):
                return False
        
        return True