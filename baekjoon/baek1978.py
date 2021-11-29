''' 
백준 1978번
소수구하기

'''
def getPrimes(n):
    lis = set()
    primes = []
    for i in range(2,n+1):
        if not i in lis:
            primes.append(i)
        else:
            continue
        for j in range(2,n+1):
            res = i * j
            if res > n :
                break
            lis.add(res)
            
    return primes

N = int(input())
li = list(map(int, input().split()))
primes = getPrimes(max(li))

count = 0
for i in li:
    if i in primes:
        count+=1
        
        
print(count)        