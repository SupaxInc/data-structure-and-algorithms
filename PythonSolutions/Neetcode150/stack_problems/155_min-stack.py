class SimplestMinStack:

    def __init__(self):
        self.stack = [] # Uses a 2d array (val, minVal) (can just use a tuple too)

    def push(self, val: int):
        # If stack is empty, then current min is the val we are pushing
        # If it is not empty, then get the previous min from top of the stack and compare with current value
        minVal = val if not self.stack else min(val, self.stack[-1][1])

        # Push an array with structure of: [value, minimum value]
        self.stack.append([val, minVal])
    
    def pop(self):
        self.stack.pop()
    
    def top(self):
        # Peeks at the last array in the stack just for its value
        return self.stack[-1][0]
    
    def getMin(self):
        # Peeks at the last array in the stack just for its min value
        return self.stack[-1][1]

class SimplerMinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.getMin()))
    
    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> None:
        return self.minStack[-1]

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minNum = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minNum = min(self.minNum, val) 
        # Append a min num per push so that we don't lose track of what the min number is per index
            # Therefore, every push will have the current min num associated with the index of normal stack
        self.minStack.append(self.minNum)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

        # If the minStack is empty, it means the original stack is empty as well
        # This means there are no more numbers in the array so there are no more mins
        # We will need to initialize it back to positive infinity
        if len(self.minStack) == 0:
            self.minNum = float("inf")
        else:
            # If it is not empty, initialize it to the top of the min stack
            self.minNum = self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # Return top of the min stack as that is the current min for current index of normal stack
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()