import unittest
import Census

class Test_tests_Census(unittest.TestCase):
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

    # Tests for avg population by region is calculated correctly  
    def test_whenValidRegionEnteredCorrectNumberOfStatesIsReturned(self):
        self.assertEqual(Census.getNumOfStatesByRegion("Great_Lakes"), 5)
        self.assertEqual(Census.getNumOfStatesByRegion("Far_West"), 6)
    
   

    def test_numberOfStatesInRegionIsCorrect(self):
        self.assertEqual(Census.getNumOfStatesByRegion("Great_Lakes"),5)
        self.assertEqual(Census.getNumOfStatesByRegion("Far_West"), 6)
        self.assertEqual(Census.getNumOfStatesByRegion("Plains"),7)
 

    def test_avgRegionalPopulationIsCorrect(self):
        self.assertAlmostEqual(Census.getAvgRegionalPopulation("Great_Lakes"),9.2872)
        self.assertAlmostEqual(Census.getAvgRegionalPopulation("Far_West"),8.78306667)
 

    


        #Build three dictionaries for the region for the population, GDP, and personal income. 
        #The key for each dictionary is the State. 
        #In the case where the user entered an invalid region, 
        #an appropriate error message should be displayed. 
        def test_reginalPopulationIsCorrect(self):
            self.assertAlmostEqual(Census.getRegionalPopulationn("Great_Lakes"),46.436)
            self.assertAlmostEqual(Census.getRegionalPopulationn("Far_West"),52.6984)

        def test_GDPisCorrect(self):
            self.assertEqual(Census.getRegionalGDP("Great_Lakes"),1776.04)
            self.assertEqual(Census.getRegionalGDP("Far_West"),2367.11)

        def test_PersonalIncomeIsCorrect(self):
            self.assertEqual(Census.getPI("Plains"),811.1269)

if __name__ == '__main__':
    unittest.main()
