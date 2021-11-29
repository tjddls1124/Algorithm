N = int(input())

blocks = []

import sys
prev_arr_min = [0,0,0]
prev_arr_max = [0,0,0]
import copy
arr_max = [0,0,0]
arr_min = [0,0,0]
for _ in range(N):
    arr = (list(map(int,sys.stdin.readline().split())))
    
    arr_max[0] = max(prev_arr_max[0], prev_arr_max[1]) + arr[0]
    arr_max[1] = max(prev_arr_max) + arr[1]
    arr_max[2] = max(prev_arr_max[1], prev_arr_max[2]) + arr[2]
    
    arr_min[0] = min(prev_arr_min[0], prev_arr_min[1]) + arr[0]
    arr_min[1] = min(prev_arr_min[0], prev_arr_min[1], prev_arr_min[2]) + arr[1]
    arr_min[2] = min(prev_arr_min[1], prev_arr_min[2]) + arr[2]
    
    prev_arr_max = copy.deepcopy(arr_max)
    prev_arr_min = copy.deepcopy(arr_min)

print(max(arr_max))
print(min(arr_min))
