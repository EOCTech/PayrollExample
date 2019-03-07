#!/usr/bin/env python3

import time
import datetime

# Get list of events for a specific employee
def getEvents(employee):
    events = []
    with open('fakelog.txt') as f:
        for line in f:
            if employee in line:
                events.append(line)
    return events

# Convert a human readable timestamp into epoch time
def convertTime(humanTime):
    pattern = '%Y-%m-%d %H:%M:%S' # Your pattern may be different 
    return int(time.mktime(time.strptime(humanTime,pattern)))

def calcHours(employee):
    eventList = getEvents(employee)
    # Start a new pay period
    timeWorked = 0

    # Keep track of clock-ins and clock-outs
    inTimes = []
    outTimes = []
    for event in eventList:
        # If it is a clock-in, grab its time and add it to inTimes
        if 'CLOCK IN' in event:
            event = event.split(' - ')[0] # Split the line at the ' - ' keep the first element
            inTimes.append(event)
        # Else grab its time and add it to outTimes
        else:
            event = event.split(' - ')[0]
            outTimes.append(event)
    
    # Match clock-ins with clock-outs and subtract
    for i in range(len(outTimes)):
        # subtract the matched up clock-ins from the clock-outs and add to timeWorked
        timeWorked += convertTime(outTimes[i])-convertTime(inTimes[i]) # Note: this time is in seconds
    
    # Convert seconds to hours and minutes
    timeWorked = str(datetime.timedelta(seconds=timeWorked))
    return timeWorked

# Test the code by feeding it an id number, a name, or a dept
print(calcHours('1001'))
print(calcHours('Hillbilly Jim'))
print(calcHours('GoodGuys'))
