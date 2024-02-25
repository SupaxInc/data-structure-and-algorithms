class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minNum = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minNum = min(self.minNum, val) # Compare what the min num is per append
        # We want to append a min num per push so that we don't lose track of what the min number is per position
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
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()