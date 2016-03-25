
def bubble_sort(a,comparer=lambda x1,x2:x1 - x2):
    N = len(a)
    swapped = False
    for loop_index in xrange(N - 1):# from 0 to N-2

        swapped = False # reset

        for index in xrange(0,N - 1 - loop_index): 
            if comparer(a[index],a[index + 1]) > 0: # a[index]>a[index+1]
                temp = a[index]
                a[index] = a[index + 1]
                a[index + 1] = temp
                swapped = True

        if not swapped:
            return # already sorted, no need to continue

def insert_sort(a,comparer=lambda x1,x2 : x1 - x2):
    N = len(a)
    for unsorted_index in xrange(1,N):
        # need to copy to variable, since a[unsorted_index] will be overwritten soon
        element_to_sort = a[unsorted_index]

        sorting_index = unsorted_index - 1
        while sorting_index >= 0 and a[sorting_index] > element_to_sort:
            a[sorting_index + 1] = a[sorting_index]
            sorting_index -= 1

        a[sorting_index + 1] = element_to_sort

            

