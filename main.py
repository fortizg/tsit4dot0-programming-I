# [creative title goes here]
# fog - 20220801

# A multidimensional list or matrix as placeholder so as to register detailed temperatures,  
# every 1 hour @ 31 days ==> 744 samples 
# detailed_temps = [[0.0 for h in range (24)] for d in range (31)]
# much more complex than needed, so maybe later. KISS!

import random

# simplified list for daily samples
daily_temps = []  #[0.0 for d in range (31)]

""" - Generar aleatoriamente las temperaturas medias registradas en el último mes de julio del año 2022.
- Conocer cantidad de temperaturas generadas y dar la posibilidad de ingresar una manualmente.
- Encontrar la temperatura máxima y mínima.
- Generar un arreglo que contenga las temperaturas menores de 20°.
- Dar la posibilidad de salir del programa en cualquier momento.
 """

print(len(daily_temps))

def randomTemps(daily_temps):
    # del daily_temps[:]
    if len(daily_temps) >= 31:
        del daily_temps[:]
    else:
        for i in range(31):
            n = round(random.uniform(-1.5,24.0),1)
            daily_temps.insert(i,n)
    return daily_temps

def showTemps(daily_temps):
    # using enumerate to get index and value
    # print ("List index-value are : ")
    for index, value in enumerate(daily_temps, start=1):
        print("day", index, "---> temperature:", value)
    return
    # listDays = [(i+1, daily_temps[i]) for i in range(len(daily_temps))]
    # print("day"+listDays[0]+1)

def chillTemp(daily_temps):
    chillDaysCount = 0
    chillDays = []
    chillDays2 = []
    for day in daily_temps:
        if day < 20.0:
            chillDaysCount += 1
            chillDays.append(day)
    return chillDays
    # for index, value in enumerate(daily_temps):
    #     if value < 20:
    #         chillDays2.append(daily_temps[index][value])
    #     # print("day", int(str(index))+1, "---> temperature:", value)
    # return chillDays2

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

# populate random temperatures
randomTemps(daily_temps)
print(daily_temps)
showTemps(daily_temps)


# Highest
print("Highest temperature was:", maxTemp(daily_temps))
# Lowest
print("Lowest temperature was:", minTemp(daily_temps))
# Chill
print("Temperatures below 20.0º:\n", chillTemp(daily_temps))