# Create a program that allows a user to choose any of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then dispaly the time in that timezone, as
# well as local time and UTC time.
# Entering 0 as the choice will quit the program
#
# Display the dates and times in a format suitable for the user
# of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

timezonesList = ["Portugal", "Iran", "Hongkong", "Greenwich", "Cuba", "Egypt", "GB", "Iceland", "PRC"]

print("Available timezones are: ")
for tZone in timezonesList:
    print(tZone)

print("Please enter a timezone or 0 to quit", end="\n")

while True:
    choice = input()
    if choice == '0':
        break
    if choice in timezonesList:
        wantedTimezone = pytz.timezone(choice)
        print("The current time in {} is {}".format(wantedTimezone, datetime.datetime.utcnow().astimezone(wantedTimezone)))
        print()
