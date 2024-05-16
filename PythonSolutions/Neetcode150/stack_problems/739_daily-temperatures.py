class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) < 2:
            return [0]

        res = [0] * len(temperatures)
        descStack = [] # Pair of [temp, index]

        for i, currTemp in enumerate(temperatures):
            # Maintains decreasing order by checking if top of stack is smaller than curr temp
                # E.g. [73, 72] -> curr temp is 74 -> pop all elements -> [74] is left
            while descStack and currTemp > descStack[-1][0]:
                # Pop the previous smallest temp
                prevTempIndex = descStack.pop()[1]
                # Grab the difference between current day and smallest temp day
                res[prevTempIndex] = i - prevTempIndex
            
            # 2D array helps keep track of index for pushed temp
            descStack.append([currTemp, i])
        
        return res