#!/usr/bin/python3

"""function to return how meny coins need to get to the target"""


def makeChange(coins, total):

    """Returns: fewest number of coins needed to get to the total"""
    if not coins or coins is None:
        return -1
    if(total <= 0):
        return 0
    maxi = max(coins)
    sumi = 0
    ans = 0
    while sumi <= total:
        while(sumi + maxi > total):
            coins.remove(maxi)
            maxi = max(coins)
        sumi += maxi
        ans += 1
        if(sumi == total):
            return ans

    return -1
