from min_max_sum import min_max_sum
import unittest

class TestMinMaxSumBasic(unittest.TestCase):

    def test_functional(self):
        self.assertEquals(min_max_sum([1,2,3,4,5]),(10,14))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMinMaxSumBasic)
    unittest.TextTestRunner(verbosity=10).run(suite)
