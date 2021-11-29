a = [10,5,8,7,6,4,3,2,9]
N = len(a)

def swap(i,j):
    a[i],a[j] = a[j],a[i]

#insertion sort
def insertion():
    for i in range(N):
        for j in range(i,N):
            if a[i] > a[j] :
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
    print(a)

#selection Sort
def selection(a):
    for i in range(N):
        minV = 100
        tj = -1
        for j in range(i,N):
            if minV > a[j]:
                tj = j
                minV= a[j]
        swap(i,tj)
    
#bubble sort
def bubble(a):
    for i in range(N):
        for j in range(N-1):
            if a[j]>a[j+1]:
                swap(j,j+1)
        print(a)


def qsort(a,left,right):
    if left >= right:
        return
    
    pivot = (left+right)//2
    i = left
    j = right
    
    while i <= j:
        while a[i] < a[pivot]:
            i+=1
        while a[j] > a[pivot]:
            j-=1

        swap(i,j)
        i+=1
        j-=1
    
    qsort(a,i,right)
    qsort(a,left,j)
    
qsort(a,0,N-1)
print(a)