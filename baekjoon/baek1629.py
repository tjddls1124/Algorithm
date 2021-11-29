
def sqmult(a,b,c):
    if b==0:
        return 1
    if b==1:
        return a%c
    if b%2==0:
        return (sqmult(a, b//2, c) * sqmult(a, b//2, c)) % c
    else:
        return ((sqmult(a, b//2, c) * sqmult(a, b//2, c)) % c * a ) % c

a,b,c = map(int,input().split())

print(sqmult(a, b, c))