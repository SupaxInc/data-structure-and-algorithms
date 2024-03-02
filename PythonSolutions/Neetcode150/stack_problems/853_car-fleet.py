class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sorted, sorts an iterable list, in this case it is a tuple
        # The tuple is the zip of position and speed, it combines the two arrays based on the same index and creates a tuple
        # It will be reversed so its easier to loop through and understand
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for pos, spd in cars:
            time = (target - pos) / spd
            # If the stack is empty then it means we can add one fleet
            # If not empty, compare the current time to the top of the stack (which is the car fleet at the front)
            # If the time is greater, that means the fleet would not likely join the fleet in the front as its too slow
            # So we append a new time (a new fleet) to the stack as it will be its own fleet
            if not stack or time > stack[-1]:
                stack.append(time)
            # If the time is less than or equal to the fleet at the front, then its likely to join the fleet as it will intersect
            # Therefore, no need to add it to the stack as its joining the fleet at the front.
            else:
                continue
        
        return len(stack)  # The stack size is the number of fleets