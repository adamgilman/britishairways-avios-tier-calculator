import unittest
from batiercalc import BATierCalculator

class TestBATierCalcObject(unittest.TestCase):
    def setUp(self):
        pass

    def test_BATierCalc(self):
        baTC = BATierCalculator()
        self.assertTrue( type(baTC) is BATierCalculator)

        