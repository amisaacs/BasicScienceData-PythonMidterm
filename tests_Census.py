import unittest
import Census

class Test_tests_Census(unittest.TestCase):
    def test_whenRegionNotFoundFalseReturned(self):
        self.assertFalse(Census.lookupRegion())

if __name__ == '__main__':
    unittest.main()
