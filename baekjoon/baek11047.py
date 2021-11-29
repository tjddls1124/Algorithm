'''
백준 11047번
동전 0

Greedy
'''

N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))

coins.reverse()
count=0
for coin in coins:
    if coin > K:
        continue
    val = K // coin
    count+=val
    K -= val * coin 

print(count)