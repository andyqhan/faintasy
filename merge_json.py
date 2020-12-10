#!/usr/bin/env python3

import json
import os
import csv

STATS_DIR = './stats_data/'
PROFILE_DIR = './profile_data/'

def merge_json(directory):
    files = os.listdir(directory)
    result = []
    for player in files:
        with open(directory + player, 'r') as player_file:
            result.append(json.load(player_file))
    with open('big_nfl_data.json', 'w') as output:
        json.dump(result, output)
    return

