
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
    
    assert x > arr[pivot]#pivot is the smallest
    if x <= arr[len(arr)-1]:
        return __binary_search(arr,pivot+1,len(arr)-1,x)
    else:
        return __binary_search(arr,0,pivot-1,x)    

def binsearch_ignore_unwanted(arr,unwanted,x):
    low = 0
    high = len(arr)-1

    while low <= high:
        while arr[high] == unwanted and high>=low:
            high -=1
        if high < low:
            return -1# this whole block is invalid

        middle = (low+high)//2
        while arr[middle] == unwanted:
            middle +=1 # since we have exluce "all invalid" case, middle will always find one

        if arr[middle] == x:
            return middle
        elif x < arr[middle]:
            high = middle-1
        else:# x> arr[middle]
            low = middle+1 

    return -1# indicates not found

def __binsearch_rotate(arr,low,high,x):
    if low > high:
        return -1

    middle = (low+high)//2
    if arr[middle] == x:
        return middle

    if arr[middle] >= arr[low]:# left subarray is sorted
        if x >= arr[low] and x < arr[middle]:# in left sorted subarray
            return __binary_search(arr,low,middle-1,x)
        else:
            return __binsearch_rotate(arr,middle+1,high,x)
    else:
        # right subarray is sorted
        assert arr[middle] < arr[len(arr)-1]
        if x > arr[middle] and x <= arr[high]:# in right sorted subarray
            return __binary_search(arr,middle+1,high,x)
        else:
            return __binsearch_rotate(arr,low,middle-1,x)

def binsearch_rotate2(arr,x):
    return __binsearch_rotate(arr,0,len(arr)-1,x)

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

def test_binsearch_rotated2():
    pivot = 6
    rotated = rotate(range(30),pivot)

    x = 24
    index = binsearch_rotate2(rotated,x)
    if index >=0:
        assert rotated[index] == x
        print "find array[%d]=%d"%(index,rotated[index])
    else:
        print "not exist"

def test_binsearch_ignore_invalid():
    arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]

    x = "ball"
    index = binsearch_ignore_unwanted(arr,"",x)

    if index >=0:
        assert arr[index] == x
        print "find array[%d]=%s"%(index,arr[index])
    else:
        print "not exist"

if __name__ == "__main__":
    # test_binsearch_rotated()
    test_binsearch_rotated2()
    # test_binsearch_ignore_invalid()



