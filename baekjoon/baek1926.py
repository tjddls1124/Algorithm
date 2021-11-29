

def getPrime(n):
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


if __name__ == '__main__':
    a,b = input().split()
    a = int(a)
    b = int(b)
    for p in getPrime(b):
        if p >= a:
            print(p)
