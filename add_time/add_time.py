# Write a function named add_time that takes in two required parameters and one optional parameter:

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
#/////////////////////////////////////////////////////////////////////////////////
#def add_time(start_time, duration, day):

start_time = "02:00"
duration = "02:30"

if start_time:
    start_time = start_time.split(":")
if duration:
    duration = duration.split(":")

hours = int(start_time[0]) + int(duration[0])
minutes = int(start_time[1]) + int(duration[1])

if hours > 12 and minutes > 60:
    pass
elif hours > 12 and minutes < 60:
    pass
elif hours < 12 and minutes < 60:
    pass
elif hours < 12 and minutes > 60:
    pass


