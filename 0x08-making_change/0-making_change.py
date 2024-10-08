#!/usr/bin/python3

"""function to return how meny coins need to get to the target"""


def makeChange(coins, total):

    """Returns: fewest number of coins needed to get to the total"""
    if not coins or coins is None:
        return -1
    if(total <= 0):
        return 0
    coins = [x for x in coins if x <= total]
    maxi = max(coins)
    sum = 0
    ans = 0
    while sum <= total:
        while(sum + maxi > total):
            coins.remove(maxi)
            if coins == []:
                return -1
            maxi = max(coins)
        sum += maxi
        ans += 1
        if (sum == total):
            return ans
    return -1
