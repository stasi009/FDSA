
def quick_sort(ar):    
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
