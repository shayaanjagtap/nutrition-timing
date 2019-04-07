#!/usr/bin/env pythons
import json
import datetime

from detect_activity import detect_activity
from update_state import return_updated_state

from other_api import get_state_from_other_api

with open('nutrition_map.json', 'r') as jsonfile:
    nutrition_map = json.load(jsonfile)

def recommend_nutrition(state, watch_data):

    # getting the state from the other platform, make async?
    if not state:
        state = get_state_from_other_api()

    # figure out the activity
    activity = detect_activity(data=watch_data)
    if activity:
        state = return_updated_state(state, activity)

    # time of day
    current_hour = datetime.datetime.now().hour
    nrt = nutrition_relevant_time(current_hour)

    # eventually this data should be in a database
    recommendation = nutrition_map[state][nrt]
    return recommendation


def nutrition_relevant_time(hour):

    nrt = ''

    if hour < 12:
        nrt = "morning"

    elif hour < 16:
        nrt = "midday"

    elif hour < 24:
        nrt = "evening"

    return nrt
