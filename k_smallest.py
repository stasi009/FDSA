
def swap(ar,i,j):
    temp = ar[i]
    ar[i] = ar[j]
    ar[j] = temp

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

def selection_not_sort(ar,k):
    def find_kmax():
        kmax = 0
        for i in xrange(1,k):
            if ar[i] > ar[kmax]:
                kmax = i
        return kmax

    kmax = find_kmax()
    for i in xrange(k,len(ar)):
        if ar[i] < ar[kmax]:
            swap(ar,kmax,i)# by now, first k are smallest within the range [0,i]
            kmax = find_kmax()

    return ar[:k]


lst = [54,26,93,17,77,31,44,55,20]
k = 4
print selection_sort_method(lst,k)
print selection_not_sort(lst,k)
print selection_not_sort( [1, 9, 2, 4, 7, 6, 3],3)




