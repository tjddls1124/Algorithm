'''
백준 1927번
최소 힙

'''

from heapq import *
import sys


arr = []

N = int(sys.stdin.readline())
for i in range(N):
    inp = int(sys.stdin.readline())
    if inp==0:
        if len(arr)==0:
            print('0')
        else:
            print(heappop(arr))
    else:
        heappush(arr, inp)
    