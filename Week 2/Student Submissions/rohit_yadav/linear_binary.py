import time
import math

def linear_search(A,item):
    start_time=time.time()
    i=0
    for x in A:
        if(item==x):
            ls_time=time.time()-start_time
            print ("Linear search time to find",item,"in",A,"is:",ls_time)
            break

def binary_search(A,item):
    start_time=time.time()
    f=0
    l=len(A)
    mid = math.floor((f+l)/2)

    while l >= f:
        if A[mid] > item:
            l = mid-1
        elif A[mid] < item:
            f = mid+1
        elif A[mid]==item:
            bs_time = time.time()-start_time()
            print("Binary search time to find",item,"in",A,"is:",bs_time)
            return mid
        mid = math.floor((f+l)/2)
    return -1

A=[10, 15, 2, 4, 8, 9, 45, 1, 5]

linear_search(A, 4)
binary_search(A, 4)