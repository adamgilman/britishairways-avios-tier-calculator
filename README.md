# British Airways Avios/Tier API [![Build Status](https://travis-ci.org/adamgilman/britishairways-avios-tier-calculator.svg?branch=master)](https://travis-ci.org/adamgilman/britishairways-avios-tier-calculator)

Python API for British Airways Avios / Tier Point Calculator

```pyhon
>>> from batiercalc import BATierCalculator
>>> baTC = BATierCalculator()
>>> airline = baTC.chooseAirline("BA")
>>> passengerTier = baTC.chooseTier("Premier")
>>> fromLocation = "LHR"
>>> toLocation = "LAX"
>>> serviceClass = baTC.chooseFareClass("F")
>>> baTC.calculate(airline, passengerTier, fromLocation, toLocation, serviceClass)
{'avios': u'16326', 'tier_points': u'210'}
```
