"""
Product Cutting problem
---
- Problem: Given a rope of length n, cut it into at least two integer-length parts such that the product of the parts is maximized.
- Greedy Insight: The optimal strategy is to cut as many 3’s as possible, with special handling for remainders.
"""
def max_product_cutting(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    # Cut as many 3s as possible
    times_of_3 = n // 3

    # If remainder is 1, convert one 3 into two 2s
    if n - times_of_3 * 3 == 1:
        times_of_3 -= 1

    times_of_2 = (n - times_of_3 * 3) // 2

    return (3 ** times_of_3) * (2 ** times_of_2)
