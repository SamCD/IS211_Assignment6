# -*- coding: utf-8 -*-

import unittest
import conversions

class KnownValues(unittest.TestCase):
        
        cel = [0.0,5.0,17.0,-13.0,100.0]
        fah = [32.0,41.0,62.6,8.6,212.0]
        kel = [273.15,278.15,290.15,260.15,373.15]

        def testCelciustoKelvin(self):
                """convertCelciusToKelvin should work for all known
                value pairs"""
                for i in range(len(self.cel)):
                        kelvin = conversions.convertCelciusToKelvin(
                                self.cel[i])
                        self.assertEqual(self.kel[i],kelvin,msg=
                                '{}K != {}K'.format(
                                        kelvin,self.kel[i]))

        def testCelciustoFahrenheit(self):
                """convertCelciusToFahrenheit should work for all known
                value pairs"""
                for i in range(len(self.cel)):
                        fahr = conversions.convertCelciusToFahrenheit(
                                self.cel[i])
                        self.assertEqual(self.fah[i],fahr,msg=
                                '{}F != {}F'.format(
                                        fahr,self.fah[i]))

        def testFahrenheittoCelcius(self):
                """convertFahrenheitToCelcius should work for all known
                value pairs"""
                for i in range(len(self.fah)):
                        celcius = conversions.convertFahrenheitToCelcius(
                                self.fah[i])
                        self.assertEqual(self.cel[i],celcius,msg=
                                '{}C != {}C'.format(
                                        celcius,self.cel[i]))

        def testFahrenheittoKelvin(self):
                """convertFahrenheitToKelvin should work for all known
                value pairs"""
                for i in range(len(self.fah)):
                        kelvin = conversions.convertFahrenheitToKelvin(
                                self.fah[i])
                        self.assertEqual(self.kel[i],kelvin,msg=
                                '{}K != {}K'.format(
                                        kelvin,self.kel[i]))

        def testKelvintoCelcius(self):
                """convertKelvinToCelcius should work for all known
                value pairs"""
                for i in range(len(self.kel)):
                        celcius = conversions.convertKelvinToCelcius(
                                self.kel[i])
                        self.assertEqual(self.cel[i],celcius,msg=
                                '{}C != {}C'.format(
                                        celcius,self.cel[i]))

        def testKelvintoFahrenheit(self):
                """convertKelvinToFahrenheit should work for all known
                value pairs"""
                for i in range(len(self.kel)):
                        fahr = conversions.convertKelvinToFahrenheit(
                                self.kel[i])
                        self.assertEqual(self.fah[i],fahr,msg=
                                '{}F != {}F'.format(
                                        fahr,self.fah[i]))

if __name__ == '__main__':
        unittest.main()
