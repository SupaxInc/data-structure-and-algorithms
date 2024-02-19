class OptimizedSolution:
    def isHappy(self, n: int) -> bool:
        def getNextNumber(number):
            total = 0
            while number > 0:
                # number is the quotient (number without last digit), divide by 10
                # remainder is the remainder (last digit), mod by 10
                number, remainder = divmod(number, 10)
                total += remainder ** 2
            return total


        slow, fast = n, getNextNumber(n)
        while n != 1 and slow != fast:
            slow = getNextNumber(slow)
            fast = getNextNumber(getNextNumber(fast))
        
        return slow == 1
