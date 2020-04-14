# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:05:52 2020

@author: karavi01
"""

#scores = [55,66,77,88,99]
#score = 77

#def getPercentiles(scores,score):
#arr = [ 10,16,8,12,15,6,3,9,5] 
#orig_arr = arr
def swap(y,i,j):
    temp = y[j]
    y[j] = y[i]
    y[i] = temp    
    return y

def partition(x,l,r):
    pivotPos = l
    i,j = l,r
    
    while i<j:        
        while x[i] <= x[pivotPos]:
            i = i+1            
        while x[j] > x[pivotPos]:
            j = j-1
        if i < j:
            x = swap(x,i,j)
    x = swap(x,pivotPos,j)
    return j

def kthSmallestElement(arr,l,r,k):
    if l==r:
        return arr[l]
    partition_index = partition(arr,l,len(arr)-1)
    if k==partition_index:
        return arr[k]
       
    if k-1<partition_index:
        return(kthSmallestElement(arr, l,partition_index, k))
    else:
        return(kthSmallestElement(arr, partition_index+1, r, k))
#kthSmallest = kthSmallestElement(arr,0,len(arr)-1,9)