#!/usr/bin/python3

"""function to return how meny coins need to get to the target"""


def makeChange(coins, total):

    """Returns: fewest number of coins needed to get to the total"""
    if not coins or coins is None:
        return -1
    if(total <= 0):
        return 0
    sum = 0
    maxi = max(coins)
    ans = 0
    while sum < total:
        if(sum == total):
            return ans
        while(sum + maxi > total):
            coins.remove(maxi)
            maxi = max(coins)
        sum += maxi
        ans += 1

    return -1
