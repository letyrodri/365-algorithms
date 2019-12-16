from bubble_sort import bubble_sort
import unittest

class TestBubbleSort(unittest.TestCase):

    def test_functional(self):
        self.assertEquals(bubble_sort([1,2,3,4]),[1,2,3,4])

    def test_functional2(self):
        self.assertEquals(bubble_sort([7,8,8,3]),[3,7,8,8])

    def test_functional3(self):
        self.assertEquals(bubble_sort([3,2,1]),[1,2,3])
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBubbleSort)
    unittest.TextTestRunner(verbosity=2).run(suite)
