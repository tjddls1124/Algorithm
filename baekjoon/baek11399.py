'''
백준 11399번
ATM

greedy
'''

N = int(input())
arr = list(map(int, input().split() ))
arr = sorted(arr)
acc = 0
for i,v in enumerate(arr):
    acc += v
    arr[i] = acc 
print(sum(arr))  