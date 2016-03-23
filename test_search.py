
import unittest
import fa_search

class BinarySearchTest(unittest.TestCase):

    def test_found(self):
        a = [1,2,3,4,5,6,9,10,18,20]

        for realindex,e in enumerate(a):
            found,findindex = fa_search.binary_search(a,e)
            self.assertTrue(found)
            self.assertEqual(realindex,findindex)

    def test_not_found(self):
        a = [1,2,3,4,5,6,9,10,18,20]

        found,index = fa_search.binary_search(a,-1)
        self.assertFalse(found)
        self.assertEqual(0,index)

        found,index = fa_search.binary_search(a,21)
        self.assertFalse(found)
        self.assertEqual(10,index)

        found,index = fa_search.binary_search(a,8)
        self.assertFalse(found)
        self.assertEqual(6,index)

        found,index = fa_search.binary_search(a,15)
        self.assertFalse(found)
        self.assertEqual(8,index)


