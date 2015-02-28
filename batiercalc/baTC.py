import requests

class BATierCalculator(object):
	def calculate(self, airline, passengerTier, fromLocation, toLocation, fareClass):
		#establish cookies
		sess = requests.Session()
		sess.get("http://www.britishairways.com")
		
		params = {	
			"eId":"199001",
			"marketingAirline": airline,
			"tier": passengerTier,
			"departureAirport":fromLocation,
			"arrivalAirport":toLocation,
			"airlineClass":fareClass,
		}
		url = "http://www.britishairways.com/travel/flight-calculator/public/en_gb"
		response = sess.post(url, params=params)
		raw = response.text 
		table = raw.split("<table class=\"genericTableCalculator\">")[1].split("</table>")[0]
		avios = table.split("<td>")[1].split("</td>")[0]
		tier_points = table.split("<td>")[2].split("</td>")[0]
		return {'avios':avios, 'tier_points':tier_points}

	def _getKeyFromDictByKeyOrValue(self, keyOrValue, sourceDict):
		#see if it's a code;
		if keyOrValue.upper() in sourceDict.keys():
			return keyOrValue.upper()

		#see if it's a name;	
		if keyOrValue in sourceDict.values():
			for key, value in sourceDict.iteritems():
			    if value == keyOrValue:
			        return key

		return None

	def chooseAirline(self, airlineNameOrCode):
		airlines = {
						"EI" : "Aer Lingus",
						"AB" : "Airberlin",
						"AS" : "Alaska Airlines",
						"AA" : "American Airlines",
						"BD" : "BMI",
						"BA" : "British Airways",
						"CX" : "Cathay Pacific",
						"AY" : "Finnair",
						"IB" : "Iberia",
						"JL" : "JAL",
						"LA" : "Lan",
						"MH" : "Malaysia Airlines",
						"IG" : "Meridiana",
						"MX" : "Mexicana",
						"EC" : "OpenSkies",
						"QF" : "Qantas",
						"QR" : "Qatar Airways",
						"RJ" : "Royal Jordanian",
						"S7" : "S7 Airlines",
						"UL" : "SriLankan Airlines",
						"JJ" : "TAM Airlines",
						"US" : "US Airways",
				 }
		return self._getKeyFromDictByKeyOrValue(airlineNameOrCode, airlines)

	def chooseTier(self, tier):
		tiers = {
						"Blue" : "Blue",
						"Silver" : "Silver",
						"Bronze" : "Bronze",
						"Gold" : "Gold",
						"Premier" : "Premier",
		}

		return self._getKeyFromDictByKeyOrValue(tier, tiers)

	def chooseFareClass(self, fareClass):
		classes = {
						"G":"Economy (Lowest)",
						"Y":"Economy (Flexible)",
						"W":"Premium Economy",
						"J":"Business/Club",
						"F":"First",
		}
		return self._getKeyFromDictByKeyOrValue(fareClass, classes)


'''
Allow_BA_Cookies	accepted	www.britishairways.com	/	28 February 2016 12:07:49 GMT	24 B		
http://www.britishairways.com/travel/flight-calculator/public/en_gb

eId=199001&marketingAirline=BA&tier=Silver&departureAirportFull=London%2C+United+Kingdom%2C+LHR%2C+Heathrow&departureAirport=LHR&arrivalAirportFull=Amsterdam%2C+Netherlands%2C+AMS%2C+Amsterdam&arrivalAirport=AMS&airlineClass=J&Calculate+Avios+and+Tier+Points=Calculate+Avios+and+Tier+Points
'''