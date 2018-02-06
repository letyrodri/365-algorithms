from recursive_fibonacci_sequence import recursive_fibonacci_sequence
import unittest

class TestRecursiveFibonacci(unittest.TestCase):

    def test_functional(self):
        self.assertEquals(recursive_fibonacci_sequence(1),1)


    def test_functional2(self):
        self.assertEquals(recursive_fibonacci_sequence(2),1)

    
    def test_functional3(self):
        self.assertEquals(recursive_fibonacci_sequence(3),2)


    def test_functional4(self):
        self.assertEquals(recursive_fibonacci_sequence(7),13)
        

    def test_functional5(self):
        self.assertEquals(recursive_fibonacci_sequence(10),55)            

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRecursiveFibonacci)
    unittest.TextTestRunner(verbosity=10).run(suite)
