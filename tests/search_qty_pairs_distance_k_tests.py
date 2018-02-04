from search_qty_pairs_distance_k import pairs
import unittest

class TestPairs(unittest.TestCase):

    def test_functional(self):
        self.assertEquals(pairs([1,2,3,4],1),3)

    def test_functional2(self):
        self.assertEquals(pairs([1,2,3,5],2),2)

    def test_functional3(self):
        self.assertEquals(pairs([1,7,9,3],6),2)
        



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPairs)
    unittest.TextTestRunner(verbosity=2).run(suite)
