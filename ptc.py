import math
import os
import random
import re
import sys
# Complete the 'countingSort' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
def countingSort(arr):
    # Write your code here
    ar = [0]*100
    A = []
    for i in arr:
        ar[i] += 1
    for i in range(len(ar)):
        for k in range(ar[i]):
            A.append(i)
    return A
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()