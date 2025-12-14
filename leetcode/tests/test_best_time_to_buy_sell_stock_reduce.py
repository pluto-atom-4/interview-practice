import pytest

from leetcode.best_time_to_buy_sell_stock_reduce import max_profit_reduce


@pytest.mark.parametrize("prices, expected", [
    ([7,1,5,3,6,4], 5),   # Example 1
    ([7,6,4,3,1], 0),     # Example 2
    ([1], 0),             # Single day
    ([2,4,1], 2),         # Buy at 2, sell at 4
    ([3,3,3], 0),         # No profit
])
def test_max_profit_reduce(prices, expected):
    assert max_profit_reduce(prices) == expected
