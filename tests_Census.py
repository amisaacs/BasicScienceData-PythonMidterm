import unittest
import Census

class Test_tests_Census(unittest.TestCase):
    #Range "Tests for 'Prompt the user for a region name. '"

    def test_whenRegionNotFoundFalseReturned(self):
        self.assertFalse(Census.lookupRegion('Xela'))

    def test_whenRegionIsFoundRegionReturned(self):
        self.assertEqual(Census.lookupRegion('Great_Lakes'),"Great_Lakes")
        self.assertEqual(Census.lookupRegion('Far_West'),"Far_West")

    #I want to add the following test, but I really have no idea how to write
    # a unit test that tests for a displayed message.
    #However, I will write the functionality into lookupRegion()
    #def test_whenRegionNotFoundErrorMessageDisplayed(self):

    #Same here, I don't know how to test for this.
    #However, still coding the functionality
    #def test_whenRegionNotFoundPromptForAnotherRegion(self):

    #End Range

#TODO: #Range or #Region

    #Range "Tests for 'Read the data from the file selecting only the data for the region. '"
    def test_whenValidRegionEnteredNumOfRecordForRegionReturned(self):
        self.assertEqual(Census.getNumOfRecordsForRegion("Great_Lakes"), 5)
        self.assertEqual(Census.getNumOfRecordsForRegion("Far_West"), 6)
 

if __name__ == '__main__':
    unittest.main()
