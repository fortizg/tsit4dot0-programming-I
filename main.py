# [creative title goes here]
# fog - 20220801

# A multidimensional list or matrix as placeholder so as to register detailed temperatures,  
# every 1 hour @ 31 days ==> 744 samples 
# detailed_temps = [[0.0 for h in range (24)] for d in range (31)]
# much more complex than needed, so maybe later. KISS!

import random

# simplified list for daily samples
daily_temps = [0.0 for d in range (31)]

""" - Generar aleatoriamente las temperaturas medias registradas en el último mes de julio del año 2022.
- Conocer cantidad de temperaturas generadas y dar la posibilidad de ingresar una manualmente.
- Encontrar la temperatura máxima y mínima.
- Generar un arreglo que contenga las temperaturas menores de 20°.
- Dar la posibilidad de salir del programa en cualquier momento.
 """

def randomTemps(daily_temps):
    for i in range(31):
        n = random.randint(-1,24)
        daily_temps.insert(i,n)

randomTemps(daily_temps)

# temperatures: min, max and avg
highest_temp: 100.0
lowest_temp: -20

def chillTemp(daily_temps):
    chillDays = 0
    for day in daily_temps:
        if day < 20.0:
            chillDays += 1
    return chillDays

def maxTemp(daily_temps):
    # Assume first number in list is largest initially and assign it to variable "max"
    max = daily_temps[0]
    # Now traverse through the list and compare each number with "max" value. Whichever is
    # largest assign that value to "max'.
    for x in daily_temps:
        if x > max:
            max = x
    # after complete traversing the list return the "max" value
    return max

def minTemp(daily_temps):
    min_temps = daily_temps[:]
    min_temps.sort()
    return min_temps[0]

print(daily_temps)
# Highest
print("Highest temperature was:", maxTemp(daily_temps))
# Lowest
print("Lowest temperature was:", minTemp(daily_temps))
# Chill
print("Number of days with temp below 20.0º:", chillTemp(daily_temps))