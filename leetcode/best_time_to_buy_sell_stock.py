"""
Best Time to Buy and Sell Stock Algorithm Explained Step-by-Step
-----------------------------------------------------------------
The Best Time to Buy and Sell Stock problem is a classic greedy algorithm that finds the maximum profit
from buying and selling a stock once. Given an array of daily prices, you must find the best buy-sell pair
to maximize profit. This problem demonstrates the greedy approach, one-pass iteration, and is fundamental
for understanding optimization problems, market analysis algorithms, and real-world trading systems.

Here is how the process works:

1. **Problem Understanding**: Buy once, sell once (in that order).
   - You must buy before you sell
   - You want to maximize profit = sell_price - buy_price
   - If no profit is possible, return 0
   - Key insight: maximize the difference between current price and minimum past price

2. **Greedy Strategy**: Track minimum price and maximum profit as you iterate.
   - Maintain min_price: the smallest price seen so far
   - Maintain best_profit: the maximum profit achievable so far
   - At each price, calculate profit if we sell at current price
   - Update min_price when we find a lower price (better buying opportunity)
   - This works because we only need one buy-sell pair

3. **Why Greedy Works**: Optimal substructure property holds.
   - At each position, only the minimum price before matters, not where it occurred
   - Future minimum prices won't help with past positions
   - We never need to reconsider earlier buy prices once we find a lower one
   - Selling at the current best price is always optimal given current min_price

4. **Algorithm Execution**: Single pass through prices.
   - Initialize min_price to infinity and best_profit to 0
   - For each price in prices:
     - Update min_price if current price is lower
     - Calculate potential profit: current_price - min_price
     - Update best_profit if potential profit is higher
   - Continue until all prices are processed

5. **State Tracking**: Only two variables needed.
   - min_price: represents the best buying opportunity seen so far
   - best_profit: represents the answer we're building incrementally
   - No need for additional data structures (unlike some other variants)
   - Space-efficient and time-efficient approach

6. **Final Result**: best_profit contains the answer.
   - Represents the maximum difference between any sell price and prior buy price
   - If no profitable transaction exists, best_profit remains 0
   - This is the optimal solution for the entire input
   - Return this value as the maximum profit

Example: prices = [7, 1, 5, 3, 6, 4]
- Iteration 1: price=7, min_price=7, profit=0, best_profit=0
- Iteration 2: price=1, min_price=1, profit=0, best_profit=0
- Iteration 3: price=5, min_price=1, profit=4, best_profit=4
- Iteration 4: price=3, min_price=1, profit=2, best_profit=4
- Iteration 5: price=6, min_price=1, profit=5, best_profit=5
- Iteration 6: price=4, min_price=1, profit=3, best_profit=5
- Result: 5 (buy at 1, sell at 6)

Time Complexity: O(n) where n = len(prices), single pass through the array
Space Complexity: O(1) only using two variables regardless of input size

Why This Matters for Interviews:
- Tests understanding of greedy algorithms vs dynamic programming
- Common follow-up: handling multiple transactions (requires different approach)
- Demonstrates optimization thinking: minimize memory while maximizing speed
- Foundation for stock trading problems and real-world optimization scenarios
- Shows ability to identify optimal substructure in problems
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Greedy implementation of Best Time to Buy and Sell Stock.
    Tracks the minimum price seen so far and the best profit achievable.
    """
    min_price = float("inf")
    best_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        best_profit = max(best_profit, price - min_price)

    return best_profit
