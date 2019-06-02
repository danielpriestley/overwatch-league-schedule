#!/usr/bin/env python3

import requests
import json
import datetime



# requests json api from url and assigns to schedules variable
r = requests.get(url='https://api.overwatchleague.com/schedule')
schedules = r.json()


# defines stage_three_matches as a list
stage_three_matches = []


# loops through json and adds all matches from stage 3 to the stage_three_matches list
for matches in schedules['data']['stages'][3]['matches']:
    stage_three_matches.append(matches)

# loops through stage_three_matches list
for matches in stage_three_matches:

    # converts times from javascript json notation to a more readable format
    times = datetime.datetime.strptime(
        matches['startDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
    
    # checks if matches are still to be played
    if matches['state'] == 'PENDING': 

        # prints out the team names
        print(
            '\n\t' 
            + matches['competitors'][0]['name'] 
            + ' vs ' 
            + matches['competitors'][1]['name']
            )
        
        # prints out the times of the matches
        print('\tTime: ' + str(times))
        
    

