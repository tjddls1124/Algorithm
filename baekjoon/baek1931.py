'''
백준 1931번
회의실 배정

Greedy (DP로 풂)
'''
from bisect import bisect_left ,bisect_right, bisect
maxV = 0
N = int(input())
timetable = []
meetings = []
ends = []
ends.append(0)
for i in range(N):
    l = list(map(int,input().split()))
    maxV = max(maxV, max(l))
    meetings.append(l)
    
meetings = sorted(meetings,key=lambda x: (x[1],x[0]))

dp = [0] * (maxV+5)
ans = 0
# print("******")
for meeting in meetings:

    start = meeting[0]
    end = meeting[1]
    bi_start = ends[bisect(ends, start)-1]
    bi_end= ends[bisect(ends,end)-1]
    # print(bi_start,bi_end)
    dp[end] = max(dp[bi_start]+1, dp[bi_end])
    ends.append(end)

print(dp[maxV])