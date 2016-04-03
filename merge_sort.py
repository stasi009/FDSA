
def merge_sort_basic_idea(ar):
    if len(ar) == 1:
        return

    middle = len(ar)//2
    left = ar[:middle]
    right = ar[middle:]

    merge_sort_basic_idea(left)
    merge_sort_basic_idea(right)

    index = leftindex = rightindex = 0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            ar[index] = left[leftindex]
            index +=1
            leftindex +=1
        else:
            ar[index] = right[rightindex]
            index +=1
            rightindex += 1

    while leftindex < len(left):
        ar[index] = left[leftindex]
        index +=1
        leftindex +=1

    while rightindex < len(right):
        ar[index] = right[rightindex]
        index += 1
        rightindex += 1

    assert index == len(ar)

a = [4,1,7,5,8,2,6,3,9]
a = [65, 92, 77, 47,  5, 40,  1, 59, 70, 92]
merge_sort_basic_idea(a)
print a
