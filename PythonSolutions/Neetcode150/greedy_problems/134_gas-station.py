class BruteForceSolution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        # Try every station as a starting point
        for start in range(n):
            fuel = 0
            completed = True
            
            # Try to make a full circle starting from 'start'
            for i in range(n):
                index = (start + i) % n  # Circular route
                fuel += gas[index] - cost[index]
                
                # Check if we run out of fuel
                if fuel < 0:
                    completed = False
                    break
            
            # If we made it around the circuit
            if completed:
                return start
        
        # If no starting point was valid
        return -1

class GreedySolution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        currentTank = 0
        startStation = 0

        # Cumulutive total to help figure out if we can actually complete the circuit at all
            # sum(gas) >= sum(cost) means we can actually complete a circuit
        totalTank = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            totalTank += diff
            currentTank += diff

            # Greedy choice (local optima): Reset starting point if current gas is negative
                # This means that we ran out of fuel already from prev start station
            if currentTank < 0:
                # Starting point becomes next station
                startStation = i + 1
                # Reset gas as we are going to a new station
                currentTank = 0
        
        return startStation if totalTank >= 0 else -1
