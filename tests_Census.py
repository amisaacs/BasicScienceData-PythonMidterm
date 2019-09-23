import unittest
import Census

class Test_tests_Census(unittest.TestCase):
    def test_whenRegionNotFoundFalseReturned(self):
        self.assertFalse(Census.lookupRegion('Xela'))

    def test_whenRegionIsFoundRegionReturned(self):
        self.assertEqual(Census.lookupRegion('Great_Lakes'),"Great_Lakes")
        self.assertEqual(Census.lookupRegion('Far_West'),"Far_West")


if __name__ == '__main__':
    unittest.main()
