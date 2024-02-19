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

        # SLow and fast pointer to detect a cycle
        slow, fast = n, getNextNumber(n)
        # If n is already 1 then don't look
        # If slow = fast, then a cycle was detected
        while n != 1 and slow != fast:
            slow = getNextNumber(slow)
            # Fast pointer moves twice as fast
            fast = getNextNumber(getNextNumber(fast))
        
        # Check if its a happy number when the cycle was detected
        return slow == 1
    
class BruteForceSolution:
    def isHappy(self, n: int) -> bool:
        mySet = set()
        total = n

        while True:
            if total == 1:
                break

            total = int(sum([math.pow(int(digit),2) for digit in str(total)]))

            if total in mySet:
                return False
            
            mySet.add(total)

        return True
