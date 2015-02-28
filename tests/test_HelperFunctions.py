import unittest, logging

from batiercalc import BATierCalculator

#@unittest.skip("temp disabled")
class TestBATCHelpers(unittest.TestCase):
    def setUp(self):
        self.baTC = BATierCalculator()

    def test_SelectAirline(self):
    	airline = self.baTC.chooseAirline("BA")
    	self.assertEqual(airline, "BA")

    	airline = self.baTC.chooseAirline("British Airways")
    	self.assertEqual(airline, "BA")

    	airline = self.baTC.chooseAirline("Aer Lingus")
    	self.assertEqual(airline, "EI")


    def test_FareClass(self):
		fareclass = self.baTC.chooseFareClass("First")
		self.assertEqual(fareclass, "F")

		fareclass = self.baTC.chooseFareClass("W")
		self.assertEqual(fareclass, "W")

		fareclass = self.baTC.chooseFareClass("Business/Club")
		self.assertEqual(fareclass, "J")