#!/usr/bin/python3

"""function to return how meny coins need to get to the target"""


def makeChange(coins, total):

    """Returns: fewest number of coins needed to get to the total"""
     dp = [float('inf')] * (total + 1)

    # Base case: 0 coins are needed to make a total of 0
    dp[0] = 0

    # Fill the DP array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, return -1 (total cannot be met)
    return dp[total] if dp[total] != float('inf') else -1
