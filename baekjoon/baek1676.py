N = int(input())

fac = [1] * (N+1)

for i in range(2,N+1):
    fac[i] = fac[i-1] * i
cnt = 0
for c in reversed(str(fac[N])):
    if c=='0':
       cnt+=1
    else:
        break
    
print(cnt)