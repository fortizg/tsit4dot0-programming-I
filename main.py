# [creative title goes here]
# fog - 20220801

# A multidimensional list or matrix as placeholder so as to register detailed temperatures,  
# every 1 hour @ 31 days ==> 744 samples 
# detailed_temps = [[0.0 for h in range (24)] for d in range (31)]
# much more complex than needed, so maybe later. KISS!

import random
# from this import ---> The Zen of Python, by Tim Peters - A Python Poem full of magic

# simplified list for daily samples
daily_temps = []  #[0.0 for d in range (31)]

def randomTemps(daily_temps):
    # del daily_temps[:]
    if len(daily_temps) >= 31:
        daily_temps.clear()
    for i in range(31):
        n = round(random.uniform(-1.5,24.0),1)
        daily_temps.insert(i,n)
    tempList = daily_temps
    return tempList

def showTemps(daily_temps):
    print("The number of samples is:", len(daily_temps))
    # using enumerate to get index and value
    for index, value in enumerate(daily_temps, start=1):
        print("day", index, "---> temperature:", value)
    return

# def changeTemp():
#     changeTemp=input("Do you want to change any record?\n 1 - Yes \n 2 - No")
#     if changeTemp == 1 or changeTemp == "Yes":
#         changeTempDay = int(input("Input day number:\n"))
#         changeTempValue = float(input("Provide new value [float]:\n")
#         daily_temps[0] = changeTempValue
#     # listDays = [(i+1, daily_temps[i]) for i in range(len(daily_temps))]
#     # print("day"+listDays[0]+1)

def freshTemp(daily_temps):
    freshDaysCount = 0
    freshDays = []
    for day, temp in enumerate(daily_temps, start=1):
        if temp < 20:
            freshDays.append([day,temp])
            freshDaysCount += 1
    return freshDays

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

def banner():
    print(
        """
        +==========================================+
        | Python functions to analyze temperatures |
        |                                          |
        | Select an operation:                     |
        | 1 - Generate temperature dataset         |
        | 2 - Read number of samples taken         |
        | 3 - Find "Highest" and "Lowest" temps    |
        | 4 - Return a list of temps below 20ºC    |
        | 0 - Exit this program                    |
        +==========================================+
        """)
    print()
    menu= int(input("Select an operation:\n"))
    
    while menu != 0:
        
        if menu == 1:
            tempList = randomTemps(daily_temps)
            print("created fake entries for July", tempList)
        
        elif menu == 2:
            showTemps(tempList)
            #print("Se tomaron Mediciones de temperatura ")

        elif menu == 3:
            # Highest
            print("Highest temperature recorded for July:", maxTemp(daily_temps))
            # Lowest
            print("Lowest temperature recorded for July:", minTemp(daily_temps))

        elif menu == 4:
            # Chilly-Fresh
            print("Temperatures below 20.0º:\n", freshTemp(daily_temps))

        else:
            print(
                """
                +===================================+
                | Try again using some valid option | 
                +===================================+
                """)
        menu= int(input("Select an operation:\n"))

banner()
