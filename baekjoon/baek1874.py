
def main():
    res = []
    n = int(input())
    st = []
    for i in range(n):
        st.append(int(input()))
        
    po = 0
    lis = [i+1 for i in range(n)]
    stack = []
    while True:
        sp = len(stack)-1
        if len(lis) == 0 and len(stack)==0:
            break
        
        if(len(stack)!=0 and stack[sp] > st[po]) :
            print("NO")
            return
        
        if len(stack)==0 or stack[sp] != st[po] :
            res.append("+") 
            stack.append(lis[0])
            lis.remove(lis[0])
        

        elif stack[sp]== st[po]:
            res.append("-")
            stack.pop()
            po+=1
        #push
        else:
            res.append("+")
            stack.append(lis[0])
            lis.remove(lis[0])
        
    for r in res:
        print(r)
 
if __name__ == '__main__':
    main()
    
    