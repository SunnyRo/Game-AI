import random
import time
number = int(input("enter the length of list/arry  "))
randomlist = random.sample(range(0,number*1000),number)

#merge sort
def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1

#quick sort
def partition(arr,low,high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] < pivot:
            i = i+1
            arr[i],arr[j]  = arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
#quickSort(randomlist,0,len(randomlist)-1)
start_time = time.time()
quickSort(randomlist,0,number-1)
print("--- %.8f seconds ---" % (time.time() - start_time))
