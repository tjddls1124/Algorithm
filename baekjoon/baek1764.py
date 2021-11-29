'''
백준 1764
듣보잡
'''

a, b = map(int,input().split())
set_a = set()
set_b = set()
for _ in range(a):
    set_a.add(input())

for _ in range(b):
    set_b.add(input())
    
print(len(set_a.intersection(set_b)))
for i in sorted(list(set_a.intersection(set_b))):
    print(i)