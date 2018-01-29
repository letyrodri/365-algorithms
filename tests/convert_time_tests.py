from convert_time import convert_time
import unittest

class TestConvertTime(unittest.TestCase):

    def test_12AM(self):
        self.assertEquals(convert_time("12:00:00AM"),"00:00:00")

    def test_12PM(self):
        self.assertEquals(convert_time("12:00:00PM"),"12:00:00")

    def test_seconds(self):
        self.assertEquals(convert_time("12:00:03AM"),"00:00:03")
        
    def test_minutes(self):
        self.assertEquals(convert_time("12:33:00PM"),"12:33:00")

    def test_any_time_PM(self):
        self.assertEquals(convert_time("05:07:33PM"),"17:07:33")

    def test_any_time_AM(self):
        self.assertEquals(convert_time("05:07:33AM"),"05:07:33")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestConvertTime)
    unittest.TextTestRunner(verbosity=2).run(suite)
