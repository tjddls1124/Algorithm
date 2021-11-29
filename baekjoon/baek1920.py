m = int(input())
arr = set()
for i in input().split():
    arr.add(i)

m = int(input())
for i in input().split():
    if i in arr:
        print('1')
    else:
        print('0')
