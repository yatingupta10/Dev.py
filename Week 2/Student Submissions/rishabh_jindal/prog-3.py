import time
from random import randint

def linear_search(A,item):
    start_time=time.time()
    i=0
    for x in A:
        if(item==x):
            ls_time=time.time()-start_time
            print "Linear search time:",ls_time

            return i;
        i+=1
    return -1

def binary_search(A,item):
    start_time=time.time
    f=0
    l=len(A)
    mid= (f+l)/2

    while l>=f:

        if A[mid]>item:
            l=mid-1
        elif A[mid]<item:
            f=mid+1
        elif A[mid]==item:
            bs_time=time.time()-start_time()
            print "Binary search Time:",bs_time
            return mid
        mid= (f+l)/2
    return -1


A=[1,2,3,4,5,6]
print A
linear_search(A,2)
binary_search(A,2)
