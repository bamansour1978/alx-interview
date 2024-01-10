#!/usr/bin/python3
"""
main
"""


def canUnlockAll(boxes):
    """function """
    unlocked = {}
    position = 0

    for b in boxes:
        if len(b) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for ky in b:
            if ky < len(boxes) and ky != position:
                unlocked[ky] = ky
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
