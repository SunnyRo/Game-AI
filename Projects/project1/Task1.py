"""
Name:           Son Vo
Course:         CS-3310-SPR20
Project:        1
Due:            03/06/20
Description:    Program Merge Sort and Quick Sort to sort a list of n elements 
with n = 10000, 20000, 50000, 100000, 200000, 500000, 1000000, ...
"""
import random
import time
# ask user to enter number of elements for creating a list.
n = int(input("Please enter the number of elements\n"))
# creating a list with n elements random value
randomlist1 = random.sample(range(0,n*1000),n)
randomlist2 = randomlist1.copy()
# merge sort
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
            k+=1
        while i < len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
# quick sort
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
# creating a menu enter 1 if we want to see the execution time, 2 if want to see if both functions actually sort the list
print("Enter 1 to see execution time")
print("Enter 2 to see list before and after sorting")
menu = int(input(""))
if menu == 1:
    start_time1 = time.time() # start time 
    mergeSort(randomlist1)
    print("--- Merge Sort: %.8f seconds ---" % (time.time() - start_time1)) # execution time = end time - start time 
    start_time2 = time.time()
    quickSort(randomlist2,0,n-1)
    print("--- Quick Sort: %.8f seconds ---" % (time.time() - start_time2))
else:
    print("\nunordered lists:")
    print(randomlist1)
    print("\nList 1 after Merge Sort:")
    mergeSort(randomlist1)
    print(randomlist1)
    print("\nList 2 after Quick Sort:")
    quickSort(randomlist2,0,len(randomlist2)-1)
    print(randomlist2)
