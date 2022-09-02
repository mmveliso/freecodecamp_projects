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
def add_time(start_time, duration, day=None):
    new_time = ""
    # split the time string i.e "02:30 AM"
    startTime = start_time
    startTime = startTime.split(" ")  # this will split the string where it encounters a white space
    startTimeMeridian = startTime[1]  # assigning the meridian time AMPM
    startTimeFirstElement = startTime[0]
    startTime = startTimeFirstElement.split(":")
    startTimeHour = int(startTime[0])
    startTimeMinutes = int(startTime[1])

    # converting start time to 24 hours format
    if startTimeMeridian == "PM":
        startTimeHour = startTimeHour + 12

    # splitting Duration string
    duration = duration
    duration = duration.split(":")
    print(duration)
    durationHour = int(duration[0])
    durationMinutes = int(duration[1])

    # converting startTime to minutes
    # converting hours to minutes
    startTimeInMinutes = int(startTimeMinutes) + (startTimeHour * 60)
    print("startTimeinminutes", startTimeInMinutes)

    # converting duration to minutes
    durationInMinutes = durationMinutes + (durationHour * 60)
    print("durationInMinutes", durationInMinutes)

    totalMinutes = int(startTimeInMinutes) + int(durationInMinutes)
    print(totalMinutes)

    # calculating the total hours
    hours = int(totalMinutes) / 60
    # calculating the total minutes
    minutes = int(totalMinutes) % 60

    # concatenating zero to the minutes if minutes is less than 10
    if len(str(minutes)) < 2:
        new_time = "0" + str(minutes)
    else:
        new_time = minutes

    # calculating days
    # there are 24 hours per day the total number of hours divided by 24 gives us the total number of days
    days = hours / 24
    # the modulus gives us the number of hours left
    # this basically converts the hours to a 24-hour time format
    # answer will always be less than 24
    hour = hours % 24

    # getting the final time in 12-hour format and meridian
    # this converts the 24-hour time format to a 12-hour format
    # the answer will never be greater than 12
    finalHours = int(hour % 12)
    # if hour is 0 then
    # hour will be zero if is less than an hour i.e 00:20 AM, 00:5 = 25min
    # so hours = 26 / 60 = 0 hours
    # now hour = 0 % 24 = 0
    if int(hour / 12) == 0:    # hour is in 24-hour time format so if hour is less than 12 it means the meridian is "AM"
                               # so when hour is divided by 12 it will return 0 because the numerator (hour) is less than the denominator (12)
        finalMeridian = "AM"
        if finalHours == 0:    # # this is to distinguish between 12 AM and 12 PM
            finalHours = 12
    else:                       # if hour is greater than 12 (hour / 12) will return a number greater than 0 meaning it's "PM"
        finalMeridian = "PM"
        if finalHours == 0:     # this is to distinguish between 12 AM and 12 PM
            finalHours = 12

    new_time = str(finalHours) + ":" + str(new_time) + " " + finalMeridian
     if day is not None:
         day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
         pos = 0
         while True:
             if day == day[pos].lower():
                 break
             pos = pos + 1
             newDay = day[((pos + (days % 7)) % 7)]
            new_time = new_time + ", " + newDay

     # output
     if days == 1:
         new_time = new_time + "(next day)"
     if days > 1:
         days = str(days)
         new_time = new_time + " (" + days + " days later)"

     return new_time

print(add_time("08:02 PM", "02:01"))