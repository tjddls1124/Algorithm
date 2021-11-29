N , K = map(int,input().split())

arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))
    
dp = [0] * (K+5)

for ma in arr:
    weight = ma[0]
    val = ma[1]
    i = K+1
    while i > 0:
        if i+weight <=K+1:
            dp[i+weight] = max(dp[i+weight], dp[i]+val)
        i-=1
    # print(dp)
print(dp[K+1])

