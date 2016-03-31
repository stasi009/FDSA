
def selection_sort_method(ar,k):
    N = len(ar)

    for i in xrange(k):

        smallest = i
        for j in xrange(i+1,N):
            if ar[j] < ar[smallest]:
                smallest = j

        if smallest != i:
            temp = ar[i]
            ar[i] = ar[smallest]
            ar[smallest] = temp

    return ar[:k]

lst = [54,26,93,17,77,31,44,55,20]
k = 4
print selection_sort_method(lst,k)




