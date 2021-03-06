
def __merge_sort(ar,temp,low,high):
    """include both low and high"""
    if low == high:
        return

    # divide and conqure
    middle = (low+high)//2
    __merge_sort(ar,temp,low,middle)
    __merge_sort(ar,temp,middle+1,high)

    # combine
    index = leftindex = low
    rightindex = middle+1

    while leftindex <= middle and rightindex <= high:
        if ar[leftindex] < ar[rightindex]:
            temp[index] = ar[leftindex]
            leftindex += 1
            index += 1
        else:
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


def merge_sort(ar):
    temp = [0 for _ in ar]
    __merge_sort(ar,temp,0,len(ar)-1)


a = [4,1,7,5,8,2,6,3,9]
a = [65, 92, 77, 47,  5, 40,  1, 59, 70, 92]
merge_sort(a)
print a
