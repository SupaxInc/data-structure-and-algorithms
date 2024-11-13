class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 1

        maxProfit = 0

        while end < len(prices):
            # Check if previous day price is less than the future date price
            # This means we were able to buy low and sell high
            if prices[start] < prices[end]:
                # Calculate profit
                maxProfit = max(maxProfit, prices[end] - prices[start])
            else:
                # If the previous day price is greater than the future date price
                # Then this means we are not able to buy low and sell high

                # So we update the price to the future date price since we found a better buy price as future date is lower
                start = end
            
            # Move to the next day
            end += 1
        
        return maxProfit