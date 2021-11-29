'''
백준 1074번
Z
'''


N,r,c, = map(int,(input().split()))


def n_plate(r,c,N):
    if N==0:
        return 0
    offset = 0
    if c >= 2**(N-1):
        offset+=1
        c -= 2**(N-1)
        
    if r >= 2**(N-1):
        r -= 2**(N-1)
        offset+=2
    return offset * ( 2 ** (N-1) ) ** 2 + n_plate(r,c,N-1)
    
        
print(n_plate(r,c,N))