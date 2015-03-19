# -*- coding: utf-8 -*-

import decimal

def convertCelciusToKelvin(temp):
    ktemp = temp + 273.15
    return float("%.3f" % ktemp)
    
def convertCelciusToFahrenheit(temp):
    ftemp = (1.8 * temp) + 32
    return float("%.3f" % ftemp)


def convertFahrenheitToKelvin(temp):
    ktemp = ((temp - 32) / 1.8) + 273.15
    return float("%.3f" % ktemp)

def convertFahrenheitToCelcius(temp):
    ctemp = (temp - 32) / 1.8
    return float("%.3f" % ctemp)


def convertKelvinToFahrenheit(temp):
    ftemp = (temp - 273.15) * 1.8 + 32
    return float("%.3f" % ftemp)

def convertKelvinToCelcius(temp):
    ctemp = temp - 273.15
    return float("%.3f" % ctemp)
