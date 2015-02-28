'''
initial mock request to build interface
from LHR to AMS
'''
import unittest, logging
import vcr

from batiercalc import BATierCalculator

my_vcr = vcr.VCR(
	serializer = 'yaml',
	cassette_library_dir = 'tests/fixtures/cassettes',
	record_mode = 'once',
)

#@unittest.skip("temp disabled")
class TestBATCLHRAMS(unittest.TestCase):
    def setUp(self):
        self.baTC = BATierCalculator()

    def test_OneWayBusinessIs40(self):
    	airline = self.baTC.chooseAirline("BA")
    	passengerTier = self.baTC.chooseTier("Silver")
    	fromLocation = "LHR"
    	toLocation = "AMS"
    	serviceClass = self.baTC.chooseFareClass("J")
    	with my_vcr.use_cassette('LHR-AMS_request.json'):
        	points = self.baTC.calculate(airline, passengerTier, fromLocation, toLocation, serviceClass)
        self.assertEqual(points['tier_points'], "40")
        self.assertEqual(points['avios'], "1250")

    def test_OneWayEconomyIs40(self):
    	airline = self.baTC.chooseAirline("BA")
    	passengerTier = self.baTC.chooseTier("Silver")
    	fromLocation = "LHR"
    	toLocation = "AMS"
    	serviceClass = self.baTC.chooseFareClass("G")
    	with my_vcr.use_cassette('LHR-AMS_economy_request.json'):
        	points = self.baTC.calculate(airline, passengerTier, fromLocation, toLocation, serviceClass)
        self.assertEqual(points['tier_points'], "10")
        self.assertEqual(points['avios'], "1000")

    def test_PremierFirstLHRLAXCathay(self):
    	airline = self.baTC.chooseAirline("Cathay Pacific")
    	passengerTier = self.baTC.chooseTier("Premier")
    	fromLocation = "LHR"
    	toLocation = "LAX"
    	serviceClass = self.baTC.chooseFareClass("F")
    	with my_vcr.use_cassette('LHR-LAX_first_request.json'):
        	points = self.baTC.calculate(airline, passengerTier, fromLocation, toLocation, serviceClass)
        self.assertEqual(points['tier_points'], "0")
        self.assertEqual(points['avios'], "0")

	def test_PremierFirstLHRLAXBA(self):
		airline = self.baTC.chooseAirline("BA")
		passengerTier = self.baTC.chooseTier("Premier")
		fromLocation = "LHR"
		toLocation = "LAX"
		serviceClass = self.baTC.chooseFareClass("F")
		with my_vcr.use_cassette('LHR-LAX_first_BA_request.json'):
			points = self.baTC.calculate(airline, passengerTier, fromLocation, toLocation, serviceClass)
		self.assertEqual(points['tier_points'], "16326")
		self.assertEqual(points['avios'], "210")
