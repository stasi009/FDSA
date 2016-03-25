
import unittest
import fa_sort

class SortTest(unittest.TestCase):

    def test_bubble_sort(self):
        a = [4,1,7,5,8,2,6,3,9]
        fa_sort.bubble_sort(a)
        self.assertEqual([1,2,3,4,5,6,7,8,9],a)

    def test_insert_sort(self):
        a = [4,1,7,5,8,2,6,3,9]
        fa_sort.insert_sort(a)
        self.assertEqual([1,2,3,4,5,6,7,8,9],a)