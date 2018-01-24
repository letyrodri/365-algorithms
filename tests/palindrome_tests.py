from palindrome import is_palindrome
import unittest

class TestPalindrome(unittest.TestCase):

    def test_functional(self):
        self.assertEquals(is_palindrome("cat"),False)

    def test_functional2(self):
        self.assertEquals(is_palindrome("level"),True)

    def test_functional3(self):
        self.assertEquals(is_palindrome("mom"),True)
        
    def test_functional4(self):
        self.assertEquals(is_palindrome("noon"),True)

    def test_functional5(self):
        self.assertEquals(is_palindrome("morning"),False)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPalindrome)
    unittest.TextTestRunner(verbosity=2).run(suite)
