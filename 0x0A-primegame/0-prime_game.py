#!/usr/bin/python3
""" Module for solving prime game question """


def isWinner(x, nums):
    """function that checks the winner between ben and maria"""
    if not nums or x < 1:
        return None
    maxn = max(nums)

    fil = [True for _ in range(max(maxn + 1, 2))]
    for i in range(2, int(pow(maxn, 0.5)) + 1):
        if not fil[i]:
            continue
        for j in range(i * i, maxn + 1, i):
            fil[j] = False
    fil[0] = fil[1] = False
    y = 0
    for i in range(len(fil)):
        if fil[i]:
            y += 1
        fil[i] = y
    player1 = 0
    for x in nums:
        player1 += fil[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
