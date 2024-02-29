class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) < 2:
            return [0]
        
        output = [0] * len(temperatures)
        stack = [] # Pair of [temp, index]

        for i, temp in enumerate(temperatures):
            # Monotonic decreasing stack to preserve descending order to find the next greater element
            while stack and temp > stack[-1][0]:
                tempIndex = stack.pop()[1]
                # Finds the day difference between a previous temperature and current temperature
                output[tempIndex] = i - tempIndex

            # 2d array to help keep track of the previous temps index
            stack.append([temp, i])

        return output 