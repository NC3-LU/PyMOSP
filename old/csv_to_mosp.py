#! /usr/bin/env python
# -*- coding: utf-8 -

import csv
import json
import requests

import config

HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}
LANGUAGES = {'EN': '2', 'FR': '1', 'DE': '3', 'NL': '4'}
LANGUAGE = 'EN'

CSV_FILE = 'assets.csv'
VALIDATING_SCHEMA = 1 # https://objects.monarc.lu/schema/14
OWNING_ORGANIZATION = 4 # https://objects.monarc.lu/organization/MONARC


if __name__ == '__main__':
    # Point of entry in execution mode

    # Loads the objects from the CSV file
    objects = []
    types = {1: 'Primary', 2: 'Secondary'}
    #themes = {}
    #with open('themes.csv', newline='') as csvfile:
        #reader = csv.DictReader(csvfile)
        #for row in reader:
            #themes[row['id']] = {'FR': row['label1'], 'EN': row['label2'], 'DE': row['label3'], 'NL': row['label4']}
    
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            objects.append({
                'name': row['label'+LANGUAGES[LANGUAGE]],
                'description': row['description'+LANGUAGES[LANGUAGE]],
                'org_id': OWNING_ORGANIZATION,
                'schema_id': VALIDATING_SCHEMA,
                'licenses': [{'id': 92}],
                'json_object': {
                    'uuid': row['uuid'],
                    'label': row['label'+LANGUAGES[LANGUAGE]],
                    'description': row['description'+LANGUAGES[LANGUAGE]],
                    'type': types[int(row['type'])],
                    #'theme': themes[row['theme_id']][LANGUAGE],
                    'code': row['code'],
                    #'c': int(row['c']),
                    #'i': int(row['i']),
                    #'a': int(row['a']),
                    'language': LANGUAGE,
                    'version': 1
                }
            })

    # Create the new objects on MOSP
    for obj in objects:
        r = requests.post(config.MOSP_URL_API,
                          auth=(config.USERNAME, config.PASSWORD),
                          headers=HEADERS,
                          data=json.dumps(obj))
        if r.status_code != 201:
            print(r.status_code)
            print(r.text)
            print(obj)
