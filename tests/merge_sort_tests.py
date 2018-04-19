from merge_sort import merge_sort
import unittest

class TestMergeSort(unittest.TestCase):

    def test_functional(self):
        self.assertEquals(merge_sort([1,2,3,4]),[1,2,3,4])

    def test_functional2(self):
        self.assertEquals(merge_sort([7,8,8,3]),[3,7,8,8])

    def test_functional3(self):
        self.assertEquals(merge_sort([4,3,2,1]),[1,2,3,4])
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMergeSort)
    unittest.TextTestRunner(verbosity=2).run(suite)
