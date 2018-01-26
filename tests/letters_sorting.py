from sorting_letters_with_counting_sort import sort_letters
import unittest

class TestSortLetters(unittest.TestCase):

    def test_functional(self):
        self.assertEquals(sort_letters('a'),'a')

    def test_functional2(self):
        self.assertEquals(sort_letters('ba'),'ab')

    def test_functional3(self):
        self.assertEquals(sort_letters('abbabaab'),'aaaabbbb')
        
    def test_functional4(self):
        self.assertEquals(sort_letters('nowyouunderstandjustwhymyheadsnotbowedidontshoutorjumpaboutorhavetotalkrealloudwhenyouseemepassingitoughttomakeyouproud'),'aaaaaaaabbdddddddeeeeeeeeeegghhhhhhiiijjkklllmmmmnnnnnnnooooooooooooooooppprrrrrssssssstttttttttttuuuuuuuuuuuvwwwwyyyyy')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortLetters)
    unittest.TextTestRunner(verbosity=2).run(suite)
