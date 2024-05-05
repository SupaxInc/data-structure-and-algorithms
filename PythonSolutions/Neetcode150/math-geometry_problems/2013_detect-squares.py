class DetectSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int) # Count occurrences of each point
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1 # Finds possible duplicates
        self.points.append(point) # Allows us to iterate through all points including duplicates
        

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point # Query points

        # Iterate through all points added
        for x, y in self.points:
            # Check if the current point we are on is not diagonal to query point
                # Diagonals helps us find squares by: getting the difference of x, px and y, py
            # The point should also not be the same as the query point since it has to a positive area
            if (abs(qx - x) != abs(qy - y)) or qx == x or qy == y:
                continue
            # Check the opposite points
            # Count a square as one but look for duplicates as well
            res += (self.pointsCount[(x, qy)] * self.pointsCount[(qx, y)])
        
        return res



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)