#!/usr/bin/python3

"""function to return how meny coins need to get to the target"""

def makeChange(coins, total):

    """Returns: fewest number of coins needed to get to the total"""

    if(total <= 0):
        return 0
    sum = 0
    coins = coins[::-1]
    i = 0
    ans = 0
    while (sum + coins[i] <= total):
        sum += coins[i]
        ans += 1
        print(sum)
        if(sum == total):
            return ans
        while(sum + coins[i] > total):
            i += 1
            print(i)

    return -1
