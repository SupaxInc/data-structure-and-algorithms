class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
            else:
                # The current car joins the fleet of the car in front of it
                continue  # This car's time is not pushed onto the stack as it joins a previous fleet
        
        return len(stack)  # The stack size is the number of fleets