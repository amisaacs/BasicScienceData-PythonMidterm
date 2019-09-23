import unittest
import Census

class Test_tests_Census(unittest.TestCase):
    #Region 
    #"Tests for 'Prompt the user for a region name. '"

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

    #End Region

#TODO: #Range or #Region

    #Range "Tests for 'Read the data from the file selecting only the data for the region. '"
    def test_whenValidRegionEnteredNumOfRecordForRegionReturned(self):
        self.assertEqual(Census.getNumOfRecordsForRegion("Great_Lakes"), 5)
        self.assertEqual(Census.getNumOfRecordsForRegion("Far_West"), 6)
    #End Range

    # Range Tests for ' Total population for the region (sum of the column value)
    def test_populationIsCorrect(self):
        self.assertEqual(Census.getPopulation(),309.3264)
        self.assertEqual(Census.getPopulation("Great_Lakes"),46.436)

    #End Range

    #Range Tests for 'Total GDP for the region (sum of the fourth column) '
    def test_GDPisCorrect(self):
        self.assertEqual(Census.getGDP(),12894.973)
        self.assertEqual(Census.getGDP("Great_Lakes"),1776.04)
 

if __name__ == '__main__':
    unittest.main()
