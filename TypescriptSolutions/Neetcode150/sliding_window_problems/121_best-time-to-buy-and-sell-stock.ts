const maxProfit = (prices: number[]): number => {
    const n = prices.length;
    let start = 0;
    let end = 1;

    let maxProfit = 0;

    while (end < n) {
        // We are able to buy the stock for profit
        if (prices[start] < prices[end]) {
            maxProfit = Math.max(prices[end] - prices[start], maxProfit);
        }
        // There will be no profit, cheaper price in the future so wait for that day
        else {
            start = end;
        }

        // Keep incrementing the day to check for all larger priced days
        end++;
    }

    return maxProfit;
};

const readableDynamicWindowMaxProfitSolution = (prices: number[]): number => {
    let start = 0;
    let maxProfit = 0;

    for (let end = 1; end < prices.length; end++) {
        if (prices[start] < prices[end]) {
            maxProfit = Math.max(prices[end] - prices[start], maxProfit);
        } else {
            // Found a smaller stock price in the future so close dynamic window
            start = end;
        }
    }

    return maxProfit;
};