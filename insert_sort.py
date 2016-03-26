
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

class SortTest(unittest.TestCase):

    def test_insert_sort(self):
        a = [4,1,7,5,8,2,6,3,9]
        insert_sort(a)
        self.assertEqual([1,2,3,4,5,6,7,8,9],a)