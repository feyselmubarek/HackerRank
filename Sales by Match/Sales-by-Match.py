#!/bin/python3
# 
# link : https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# 
# Time complexity : O(N), where N is size of the given socks
# Space cimplexity : O(1)

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count_arr = [0] * 101
    pairs = 0
    
    for num in ar:
        pairs += count_arr[num] % 2;
        count_arr[num] += 1;
    
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
