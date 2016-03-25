#!/bin/python
def insertionSort(ar):    
    element_to_sort = ar[len(ar)-1]
    
    index = len(ar)-2
    while index >=0 and ar[index] > element_to_sort:
        ar[index+1] = ar[index]
        print " ".join( (str(e) for e in ar))
        index -= 1
        
    ar[index+1] = element_to_sort
    print " ".join( (str(e) for e in ar) )

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
