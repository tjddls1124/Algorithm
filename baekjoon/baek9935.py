'''
백준 9935번
문자열 폭발
'''

a = input()
b = input()


res = ""

i = 0
l = ""
st = []

def check():
    if len(st) >= len(b):
        for i in range(1,len(b)+1):
            if st[-i] != b[-i]:
                return False
        return True
    else:
        return False    

while True:
    if i >= len(a):
        break
    st.append(a[i])
    if check():
        for _ in range(len(b)):
            st.pop()
    
    i+=1

if len(st)==0:
    print("FRULA")
for v in st:
    print(v,end='')
