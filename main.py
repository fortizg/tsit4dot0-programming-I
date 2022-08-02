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
    if len(daily_temps) >= 31:
        daily_temps.clear()
    for i in range(31):
        n = round(random.uniform(-1.5,24.0),1)
        daily_temps.insert(i,n)
    return daily_temps


def showTemps(daily_temps):
    print("The number of samples is:", len(daily_temps))
    # using enumerate to get index and value
    for index, value in enumerate(daily_temps, start=1):
        print("day", index, "---> temperature:", value)
    return


def changeTemp():
    changeTemp = input("Do you want to change any record?\n 1 - Yes \n 2 - No\n")
    if changeTemp == "1" or changeTemp == "Yes":
        changeTempDay = int(input("Input day number:\n"))
        changeTempValue = float(input("Provide new value [float]:\n"))
        daily_temps[changeTempDay-1] = changeTempValue


def freshTemp(daily_temps):
    freshDaysCount = 0
    freshDays = []
    for day, temp in enumerate(daily_temps, start=1):
        if temp < 20:
            freshDays.append([day,temp])
            freshDaysCount += 1
    return freshDays


def maxTemp(daily_temps):
    # Assume first number in list is largest initially and assign it to variable "max"
    max = daily_temps[0]
    # Traverse through the list and compare each number with "max" value. Whichever is
    # largest assign that value to "max'
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
        +===============================================+
        | Python functions to analyze temperatures      |
        |                                               |
        | Select an operation:                          |
        | 1 - Generate temperature dataset              |
        | 2 - Show and count samples taken              |
        | 3 - Find "Highest" and "Lowest" temps         |
        | 4 - Return a list of temps below 20ºC         |
        | 5 - Manually enter a new record (day, value)  |
        | 9 - Display "Main Menu"                       |
        | 0 - Exit this program                         |
        +===============================================+
        """)
    print()

def mainMenu():
    menu= int(input("Select an operation:\n"))
    
    while menu != 0:
        
        if menu == 1:
            # Add random records to dataset/list
            print("New records have been added to July dataset\n", randomTemps(daily_temps))
        
        elif menu == 2:
            # Show temps and counts
            showTemps(daily_temps)

        elif menu == 3:
            # Highest
            print("Highest temperature recorded for July:", maxTemp(daily_temps))
            # Lowest
            print("Lowest temperature recorded for July:", minTemp(daily_temps))

        elif menu == 4:
            # Chilly-Fresh days
            print("Temperatures below 20.0º -- Format like '[day, temp]'\n", freshTemp(daily_temps))

        elif menu == 5:
            # In case you want to get something changed/corrected (manually)
            changeTemp()

        elif menu == 9:
            # Menu
            banner()

        else:
            print(
                """
                +===================================+
                | Try again using some valid option |
                |                                   | 
                |      Tip: Hit 9 to see Main Menu  | 
                |           or 0 to Exit            | 
                +===================================+
                """)
        menu= int(input("Select an operation:\n"))

banner()
mainMenu()
