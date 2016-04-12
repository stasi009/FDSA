
def rotate(arr,pivot):
    return arr[pivot:]+arr[:pivot]

def __binary_search(arr,low,high,x):

    if x < arr[low]:
        return -1
    elif x > arr[high]:
        return -1

    while low <= high:
        middle = (low+high)//2

        if arr[middle] == x:
            return middle
        elif x < arr[middle]:
            high = middle-1
        else:# x> arr[middle]
            low = middle+1 

    return -1# indicates not found

def binary_search(arr,x):
    return __binary_search(arr,0,len(arr)-1,x)

def find_pivot(arr):
    low = 0
    high = len(arr)-1

    while high - low > 1:
        middle = (low+high)//2
        
        if arr[middle-1] > arr[middle]:
            return middle
        elif arr[middle] < arr[high]:# right is sorted
            high = middle-1
        else:
            assert arr[middle] > arr[low]
            low = middle+1

    assert arr[low] > arr[high]
    return high

def binary_search_rotated(arr,x):
    """
    a sorted array is rotated
    both left subarray and right subarray are sorted
    """
    pivot = find_pivot(arr)

    if x == arr[pivot]:
        return pivot

    index = __binary_search(arr,0,pivot-1,x)
    if index >=0:
        return index
    else:
        return __binary_search(arr,pivot+1,len(arr)-1,x)

################################ test
def test_normal_binsearch():
    arr = [1,2,3,4,5,6,9,10,18,20]
    binary_search(arr,1)
    binary_search(arr,9)
    binary_search(arr,20)

def test_find_pivot():
    arr = range(30)

    pivot = 6
    rotated = rotate(arr,pivot)

    find_pivot(rotated)

def test_binsearch_rotated():
    pivot = 6
    rotated = rotate(range(30),pivot)

    x = 24
    index = binary_search_rotated(rotated,x)
    if index >=0:
        assert rotated[index] == x
        print "find array[%d]=%d"%(index,rotated[index])
    else:
        print "not exist"


if __name__ == "__main__":
    test_binsearch_rotated()



