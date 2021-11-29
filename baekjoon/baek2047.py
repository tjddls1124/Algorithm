
fac = [1]*101

for i in range(1,101):
    fac[i] = i * fac[i-1]

# print(fac)


M,N = map(int,input().split())
res = fac[M]//fac[M-N]//fac[N]

print(res)