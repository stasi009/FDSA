
"""
Given an unsorted array of non-negative integers, find the first continous subarray which adds to a given number.
"""

def subarray_sum_k(arr,k):
    low = 0
    while arr[low] > k and low < len(arr):
        low += 1
    if low == len(arr):
        return -1,-1 # cannot find

    high = low
    sum = arr[low]
    if sum == k:
        return low,high

    direction = 1
    while (direction >0 and high < len(arr)-1) or (direction<0 and low < len(arr)-1):
        if direction > 0:# expand
            high +=1
            sum += arr[high]
        else: # shrink
            sum -= arr[low]
            low +=1

        if sum == k:
            return low,high
        elif sum < k:                 
            direction = 1 # expand
        else:
            direction = -1 # shrink

    return -1,-1# not found

def test(line,k):
    arr = [int(e) for e in line.split()]
    low,high = subarray_sum_k(arr,k)
    if low < 0:
        print "not exist"
    else:
        temp = (str(e) for e in arr[low:high+1])
        print "%s=%d"%("+".join(temp),k)

test("3 4 7 9 1",7)

test("135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134  ",468)

test("135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134  ",134)


            
            