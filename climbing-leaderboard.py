#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    aliceRanks = []
    sortedScores = sorted(list(set(scores)))
    length = len(sortedScores)
    for aliceScore in alice:
        aliceRanks.append(length - bisect.bisect_right(sortedScores, aliceScore) + 1)
    return aliceRanks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
