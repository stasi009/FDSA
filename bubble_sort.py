
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

class SortTest(unittest.TestCase):

    def test_bubble_sort(self):
        a = [4,1,7,5,8,2,6,3,9]
        bubble_sort(a)
        self.assertEqual([1,2,3,4,5,6,7,8,9],a)



            

