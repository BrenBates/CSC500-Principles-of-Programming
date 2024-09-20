# Brennen Bates  9/20/24
# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).  
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).   
# Write a Python program to solve the general version of the above problem.  
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm.   
# Your program should output what time will be on a 24-hour clock when the alarm goes off.

import math

current_time = int(input('Enter the current time rounded to the nearest hour based on 24 hour clock:'))
hours = int(input('Number of hours to wait for an alarm:'))

alarm_time = (current_time + hours) % 24
days = math.floor((current_time+hours)/24)

if days > 0:
    print('Your alarm will go off in',days,'calendar days.')

print('Your alarm will go off at {}.'.format(alarm_time))