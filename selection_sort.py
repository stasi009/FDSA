
def selection_sort(ar):
    N = len(ar)
    for i in xrange(N-1):

        lastpos = N-1-i
        highest = 0

        for j in xrange(1,lastpos+1):

            if ar[j] > ar[highest]:
                highest = j


        temp = ar[lastpos]
        ar[lastpos] = ar[highest]
        ar[highest] = temp

alist = [54,26,93,17,77,31,44,55,20]
selection_sort(alist)
print alist

