#!/bin/python3

import math
import os
import random
import re
import sys


def breakingRecords(scores):
    highest_score = []
    high_cnt = 0

    lowest_score  = []
    low_cnt = 0

    highest_score.append(scores[0])
    lowest_score.append(scores[0])

    for i in range(1,len(scores)):

        if (scores[i] > highest_score[-1]):
            lowest_score.append(lowest_score[-1])
            highest_score.append(scores[i])
            high_cnt+=1

        elif (scores[i] < lowest_score[-1]):
            highest_score.append(highest_score[-1])
            lowest_score.append(scores[i])
            low_cnt+=1
    
    print(high_cnt, end=' ')
    print(low_cnt)
    
if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    breakingRecords(scores)

