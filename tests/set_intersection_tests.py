from set_intersection import set_intersection
import unittest

class TestSeetIntersection(unittest.TestCase):

    def test_functional(self):
        self.assertEquals(set_intersection({1,2,3},{3,4,5,8}),{3})

    def test_functional2(self):
        self.assertEquals(set_intersection({1,2,3},{9,4,5,8}),set())

    def test_functional3(self):
        self.assertEquals(set_intersection({5,8,3},{3,4,5,8}),{5,8,3})
        



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSeetIntersection)
    unittest.TextTestRunner(verbosity=2).run(suite)
