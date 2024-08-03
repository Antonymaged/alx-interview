#!/usr/bin/python3
""" 0x01. Lockboxes """


def canUnlockAll(boxes):
    if(type(boxes) is not list or len(boxes) == 0):
        return False
    for i in range(1,len(boxes)-1):
        for j in range(len(boxes)-1):
            flag = False
            if(i in boxes[j] and i != j):
                flag = True
                break
        if flag is not True:
            return flag
    return True
