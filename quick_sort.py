
def simple_quick_sort(ar):   
    """
    assume all elements are unique
    """ 
    if len(ar) <= 1:
        return

    # ------------------------ partition
    p = ar[0]
    left = []
    right = []
    for index in xrange(1,len(ar)):
        if ar[index] < p: 
            left.append(ar[index])
        elif ar[index] > p:
            right.append(ar[index])
        else:
            raise Exception("violate the constraints that each number is unique")
                
    # ------------------------ recursive sort subarray
    quick_sort(left)
    quick_sort(right)
                
    # ------------------------ assemble together
    index = 0
    for e in left:
        ar[index] = e
        index += 1
        
    ar[index] = p
    index += 1
        
    for e in right:
        ar[index] = e
        index += 1
        
    # ------------------------ print progress
    print " ".join((str(e) for e in ar))

def swap(ar,i,j):
    temp = ar[i]
    ar[i] = ar[j]
    ar[j] = temp 

def partition(ar,low,high):
    """
    partition algorithm see: https://www.youtube.com/watch?v=MZaf_9IZCrc
    """
    pivot = ar[high]
    i = low - 1
    
    for j in xrange(low,high):# from low to high-1
        if ar[j] < pivot:
            i += 1
            swap(ar,i,j)        
    swap(ar,i+1,high)
    
    print " ".join( (str(e) for e in ar))
    return i+1

def quick_sort(ar,low,high):
    """
    in-place quick sort
    """
    if high > low:
        pindex = partition(ar,low,high)
        quick_sort(ar,low,pindex-1)
        quick_sort(ar,pindex+1,high)
        

