# Write a function named add_time that takes in two required parameters and one optional parameter:
from typing import Union, Any


# a start time in the 12-hour clock format (ending in AM or PM)
# a duration time that indicates the number of hours and minutes
# (optional) a starting day of the week, case insensitive
# The function should add the duration time to the start time and return the result.

# If the result will be the next day, it should show (next day) after the time. 
# If the result will be more than one day later, it should show (n days later) after the time,
#  where "n" is the number of days later.

# If the function is given the optional starting day of the week parameter, then the output 
# should display the day of the week of the result. The day of the week in the output should
#  appear after the time and before the number of days later.

# Below are some examples of different cases the function should handle. Pay close attention 
# to the spacing and punctuation of the results.
# /////////////////////////////////////////////////////////////////////////////////
def add_time(start_time, duration, day = None):
    # split the time string i.e "02:30 AM"
    startTime = start_time
    startTime = startTime.split(" ")  # this will split the string where it encounters a white space
    startTimeMeridian = startTime[1]  # assigning the meridian time AMPM
    startTimeFirstElement = startTime[0]
    startTime = startTimeFirstElement.split(":")
    startTimeHour = startTime[0]
    startTimeMinutes = startTime[1]

    # converting start time to 24 hours format
    if startTimeMeridian == "AM":
        startTimeHour = startTimeHour + 12

    # splitting Duration string
    duration = duration
    duration = duration.split(":")
    durationHour = duration[0]
    durationMinutes = duration[1]

    # converting startTime to minutes
    # converting hours to minutes
    startTimeInMinutes = startTimeMinutes + (startTimeHour * 60)

    # converting duration to minutes
    durationInMinutes = durationMinutes + (durationHour * 60)

    totalMinutes = startTimeInMinutes + durationInMinutes

    # calculating the total hours
    hours = totalMinutes / 60
    # calculating the total minutes
    minutes = totalMinutes % 60

    # calculating days
    # there are 24 hours per day the total number of hours divided by 24 gives us the total number of days
    day = hours / 24
    # the modulus gives us the number of hours left
    hour = hours % 24

    