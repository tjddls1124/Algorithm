from heapq import *
import sys

def bsearch(low,high,weight):
    global check
    if low > high:
        return

    mid = (low+high) // 2
    if weight <= knaps[mid]:
        check = mid
        bsearch(low,mid-1,weight)
    else:
        bsearch(mid+1,high,weight)

N, K = map(int,sys.stdin.readline().split())

jews = []
knaps = []
for _ in range(N):
    jews.append(list(map(int,sys.stdin.readline().split())))

for _ in range(K):
    knaps.append(int(sys.stdin.readline()))



visited = [False] * K
jews = sorted(jews,key=lambda x: x[0])
knaps = sorted(knaps)
res = 0

index = 0
hq = []
for k in knaps:
    while index < N and jews[index][0] <= k :
        heappush(hq, ( (-1 * jews[index][1], jews[index][1] ) ))
        index+=1
    if hq:
        res+= heappop(hq)[1]
print(res)