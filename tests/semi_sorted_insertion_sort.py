from partial_sorted_insertion_sort import partial_sorted_insertion_sort
import unittest

class TestSemiSortedInsertionSort(unittest.TestCase):

    def test_functional(self):
        self.assertEquals(partial_sorted_insertion_sort([1,2,3,4]),[1,2,3,4])

    def test_functional2(self):
        self.assertEquals(partial_sorted_insertion_sort([1,2,3,-4]),[-4,1,2,3])

    def test_functional3(self):
        self.assertEquals(partial_sorted_insertion_sort([1,2,9,4]),[1,2,4,9])
        



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSemiSortedInsertionSort)
    unittest.TextTestRunner(verbosity=2).run(suite)
