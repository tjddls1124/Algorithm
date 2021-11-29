'''
백준 11444번
피보나치 수 6
'''
import sys

N = int(input())
MOD = 1000000007
p1= 1
p2 =1
n1 = 0
n2 = 0


            
def sqFibo(n):
    if n==1:
        return 0,1
    
    if n%2==0:
        return mult(*sqFibo(n//2)) 
    else:
        n1,n2 = mult(*sqFibo(n//2))  
        return n2, (n1+ n2) % MOD

def mult(p1,p2):
    
    n1 = (p1 * p1 + p2 * p2) % MOD
    n2 = (p1 * p2 + p2 * (p1+p2) ) % MOD
    
    return n1,n2

print(sqFibo(N)[1])