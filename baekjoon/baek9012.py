'''
백준 9012
괄호
'''


from collections import deque
def vps(s):
    stack = deque()
    for c in s:
        if c=='(':
            stack.append(c)
        if c==')':
            if len(stack)==0:
                return False
            if not stack.pop()=='(':
                return False
    if len(stack) == 0:
        return True
    return False

t = int(input())
for i in range(t):
    s = input()
    if vps(s):
        print("YES")
    else:
        print("NO")
    