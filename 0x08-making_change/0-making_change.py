#!/usr/bin/python3

"""function to return how meny coins need to get to the target"""

def makeChange(coins, total):

    """Returns: fewest number of coins needed to get to te total"""
    if(total <= 0):
        return 0
    sum = 0
    maxi = max(coins)
    ans = 0
    while sum < total:
        sum += maxi
        ans += 1
        if(sum == total):
            return ans
        if(sum + maxi > total):
            coins.remove(maxi)
            maxi = max(coins)

    return -1
