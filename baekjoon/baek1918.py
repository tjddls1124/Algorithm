'''
백준 1918번

'''

s = input()

st = []


def rec(s):
    if len(s)==1:
        return s[0]
    st = []
    op_stack = []
    i = 0
    while True:
        if i >= len(s):
            break
        c = s[i]
        if c=='*' or c=='/':
            p = st.pop()
            st.append(p+s[i+1]+c)
            i+=2
            continue
        elif c=='+' or c=='-':
            op_stack.append(c)
        else:
            st.append(c)
        
        i+=1
    res = ""
    while True:
        if len(op_stack)==0:
            break
        res = st.pop() + op_stack.pop() + res
    return st.pop() + res

for c in s:
    li = []
    t = ""
    if c==')':
        while True:
            t = st.pop()
            if t=='(':
                st.append(rec(li))
                break
            li.insert(0,t)
        continue
    st.append(c)
print(rec(st))