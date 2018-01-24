from binary_search import binary_search
import unittest

class TestBinarySearch(unittest.TestCase):

    def test_functional(self):
        self.assertEquals(binary_search([1,2,3,4], 3),2)

    def test_functional2(self):
        self.assertEquals(binary_search([1,2,3,4], 2),1)

    def test_functional3(self):
        self.assertEquals(binary_search([1,2,3,4,7,8,9], 7),4)
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBinarySearch)
    unittest.TextTestRunner(verbosity=2).run(suite)
