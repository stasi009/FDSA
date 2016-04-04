
"""
An inversion is defined, if i<j, but a[i]>a[j]. 
"""

def __count_inversion(results,ar,temp,low,high):
    """include both low and high"""
    if low == high:
        return

    # divide and conqure
    middle = (low+high)//2
    __count_inversion(results,ar,temp,low,middle)
    __count_inversion(results,ar,temp,middle+1,high)

    # combine
    index = leftindex = low
    rightindex = middle+1
    while leftindex <= middle and rightindex <= high:
        if ar[leftindex] <= ar[rightindex]:
            temp[index] = ar[leftindex]
            leftindex += 1
            index += 1
        else:
            for jj in xrange(leftindex,middle+1):
                results.append((ar[jj],ar[rightindex]))

            temp[index] = ar[rightindex]
            rightindex += 1
            index += 1
            
    while leftindex <= middle:
        temp[index] = ar[leftindex]
        index += 1
        leftindex +=1

    while rightindex <= high:
        temp[index] =ar[rightindex]
        index += 1
        rightindex +=1

    assert index == high+1

    # copy back
    for i in xrange(low,high+1):
        ar[i] = temp[i]


def count_inversion(ar):
    results = []
    temp = [0 for _ in ar]
    __count_inversion(results,ar,temp,0,len(ar)-1)
    return results


a = [4,1,7,5,8,2,6,3,9]
print count_inversion(a)

