from anagram_palindrome import anagram_palindrome
import unittest

class TestAnagramPalindrome(unittest.TestCase):

    def test_functional(self):
        self.assertEquals(anagram_palindrome("aa"),True)

    def test_functional2(self):
        self.assertEquals(anagram_palindrome("aab"),True)

    def test_functional3(self):
        self.assertEquals(anagram_palindrome("abc"),False)
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAnagramPalindrome)
    unittest.TextTestRunner(verbosity=2).run(suite)
