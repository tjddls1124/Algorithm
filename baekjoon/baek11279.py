'''
최대 힙
'''

import heapq
import sys
from heapq import *
N = int(input())
arr = []
for _ in range(N):
    inp = int(sys.stdin.readline())
    inp *= -1
    if inp == 0:
        if len(arr)==0:
            print(0)
        else:
            print(-1*heappop(arr))
            
    else:
        heappush(arr,inp)


