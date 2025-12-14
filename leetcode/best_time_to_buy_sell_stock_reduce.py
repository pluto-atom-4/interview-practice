"""
Best Time to Buy and Sell Stock - Functional Reduce Implementation
------------------------------------------------------------------
This is an alternative functional approach to the Best Time to Buy and Sell Stock problem using Python's
functools.reduce() method. While the imperative version uses explicit loops and variable updates, this version
demonstrates functional programming paradigms with immutable state passing. The reduce() function accumulates
a tuple state (min_price, max_profit) across the entire price list in a single operation.

Functional Programming Approach: Using reduce() for accumulation.
- reduce() applies a function cumulatively to items in an iterable
- Transforms a sequence into a single accumulated value
- The accumulator is a tuple: (min_price_so_far, max_profit_so_far)
- Each price produces a new tuple state (immutable pattern)

How it works:

1. **Initial State Setup**: Start with (infinity, 0) accumulator.
   - min_price = infinity (any actual price will be lower)
   - max_profit = 0 (no profit initially)
   - This represents "no transactions considered yet"

2. **Reduce Function Design**: step() function processes each price.
   - Input: accumulator tuple (min_price, best_profit) and current price
   - Output: new tuple with updated min_price and best_profit
   - Immutable: doesn't modify the input, returns a new tuple
   - Pure function: same input always produces same output

3. **Per-Price Processing**: For each price iteration.
   - Unpack current accumulator: (min_price, best_profit)
   - Calculate new_min: min(min_price, price)
   - Calculate new_profit: max(best_profit, price - new_min)
   - Return new tuple (new_min, new_profit)
   - reduce() automatically uses this tuple for next iteration

4. **Accumulation Process**: reduce() chains all operations.
   - Applies step() to first two elements, producing intermediate state
   - Takes that state and next price, applies step() again
   - Continues until all prices are processed
   - Final accumulator contains the complete solution

5. **Result Extraction**: Unpack final tuple to get answer.
   - reduce() returns final accumulator: (final_min_price, final_profit)
   - We only need the second element: final_profit
   - Discard final_min_price using underscore: _, best_profit = ...
   - Return best_profit as the maximum profit achievable

Example: prices = [7, 1, 5, 3, 6, 4]
- Initial: (inf, 0)
- Price 7: (7, 0)
- Price 1: (1, 0)
- Price 5: (1, 4)  <- profit = 5 - 1
- Price 3: (1, 4)
- Price 6: (1, 5)  <- profit = 6 - 1
- Price 4: (1, 5)
- Result: 5

Time Complexity: O(n) where n = len(prices), one pass through reduce
Space Complexity: O(1) - only storing tuple state in reduce, no additional structures

Comparison with Imperative Approach:
- **Imperative**: Uses explicit loop and variable mutations (traditional)
- **Functional**: Uses reduce() with immutable state passing (declarative)
- **Performance**: Both O(n) time and O(1) space - identical efficiency
- **Readability**: Imperative often clearer for most developers; functional more elegant
- **Use Cases**: Functional approach is useful when chaining transformations

Why This Matters for Interviews:
- Shows understanding of functional programming paradigms in Python
- Demonstrates knowledge of reduce(), map(), filter(), and functional composition
- Illustrates how to solve problems in multiple styles (flexibility)
- Useful when discussing design patterns and code organization
- Relevant for teams using functional programming approaches (Scala, Haskell, etc.)
- Shows ability to think declaratively vs imperatively
"""

from functools import reduce
from typing import List, Tuple


def max_profit_reduce(prices: List[int]) -> int:
    """
    Functional implementation using functools.reduce.
    Accumulates state (min_price_so_far, max_profit_so_far) through the price list.
    """

    def step(acc: Tuple[int, int], price: int) -> Tuple[int, int]:
        min_price, best_profit = acc
        new_min = min(min_price, price)
        new_profit = max(best_profit, price - new_min)
        return (new_min, new_profit)

    # Initial accumulator: (infinite min price, zero profit)
    _, best_profit = reduce(step, prices, (float("inf"), 0))
    return best_profit
