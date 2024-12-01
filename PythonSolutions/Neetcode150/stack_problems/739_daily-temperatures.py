class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n < 2:
            return [0]
        
        res = [0] * n
        stack = [] # Pair of (temp, index)

        for currIndex, currTemp in enumerate(temperatures):
            # Helps find the smallest previous temp in the decreasing stack 
                # The stack already has temperatures that we've seen
            # If theres a smaller temp than the current temp
                # That means those smaller temps have found a larger temperature
            while stack and currTemp > stack[-1][0]:
                prevIndex = stack.pop()[1]

                # Then count the different between current warmer day and previous colder day
                    # In the index of the previous colder day
                res[prevIndex] = currIndex - prevIndex
            stack.append([currTemp, currIndex])
        
        return res
    
# Monotonic Decreasing Stack Example
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
#  index:       0   1   2   3   4   5   6   7

# Stack shows [temp, index]. Let's walk through it:

# 1) Push 73: stack = [[73,0]]
#    73 is first element

# 2) See 74: stack = [[74,1]]
#    74 > 73, so pop 73 and calculate: 1-0 = 1 day wait
#    Push 74

# 3) See 75: stack = [[75,2]]
#    75 > 74, so pop 74 and calculate: 2-1 = 1 day wait
#    Push 75

# 4) See 71: stack = [[75,2], [71,3]]
#    71 < 75, so just push it

# 5) See 69: stack = [[75,2], [71,3], [69,4]]
#    69 < 71, so just push it

# 6) See 72: stack = [[75,2], [72,5]]
#    72 > 69, pop 69 and calculate: 5-4 = 1 day wait
#    72 > 71, pop 71 and calculate: 5-3 = 2 days wait
#    72 < 75, so push it

# Result array: [1,1,4,2,1,1,0,0]
#               ^ days to wait for warmer temperature