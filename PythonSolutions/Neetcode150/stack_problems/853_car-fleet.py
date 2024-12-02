class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sorted, sorts an iterable list, in this case it is a tuple
        # Zip position and speed, combines the two arrays on the same index and creates a tuple
        # E.g. position = [10,8,0,5,3], speed = [2,4,1,1,3]
        # Result: [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
            # Array is reversed so its more readable
            # Could loop normally but then we would have to iterate in reverse which is less readable
        # If we started from left to right, its hard to know if we can join the car in the front since we don’t know if it already joined a fleet thats even more ahead.
        cars = sorted(zip(position, speed), reverse=True)

        # Stores the time, and each time stored symbolizes a fleet
        fleets = []
        
        for pos, spd in cars:
            # Calculate the time it takes for the car to reach the target
            timeToTarget = (target - pos) / spd

            # If the stack is empty then it means we can add one fleet
            # If not empty, compare the current time to the top of the stack (which is the car fleet at the front)

            # If the time is greater, that means the fleet would not likely join the fleet in the front as its too slow
            # So we append a new time (a new fleet) to the stack as it will be its own fleet
            if not fleets or timeToTarget > fleets[-1]:
                fleets.append(timeToTarget)
            # If the time is less than or equal to the fleet at the front, then its likely to join the fleet as it will intersect
            # Therefore, no need to add it to the stack as its joining the fleet at the front.
            else:
                continue
        
        return len(fleets)  # The stack size is the number of fleets