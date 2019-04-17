#! /usr/bin/env python
# -*- coding: utf-8 -

import io
import csv
import json
import requests

import config


HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}
LANGUAGES = {'en': '2', 'fr': '1', 'de': '3', 'nl': '4'}
LANGUAGE = 'en'

CSV_FILE = 'vulnerabilities.csv'

ORG_ID = 4
SCHEMA_ID = 14


OBJECTS = []

# Loads the objects from the CSV file
with open(CSV_FILE, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        OBJECTS.append({
                    'name': row['label'+LANGUAGES[LANGUAGE]],
                    'description': row['description'+LANGUAGES[LANGUAGE]],
                    'org_id': ORG_ID,
                    'schema_id': SCHEMA_ID,
                    'licenses': [{'id': 92}],
                    'json_object': {
                        'uuid': row['uuid'],
                        'label': row['label'+LANGUAGES[LANGUAGE]],
                        'description': row['description'+LANGUAGES[LANGUAGE]],
                        'mode': int(row['mode']),
                        'code': row['code'],
                        'status': int(row['status'])
                    }
        })


# Create the new objects on MOSP
for obj in OBJECTS:
    r = requests.post(config.MOSP_API,
                auth=(config.USERNAME, config.PASSWORD),
                headers=HEADERS,
                data=json.dumps(obj))
    if r.status_code != 201:
        print(r.status_code)
        print(r.reason)
        print(obj)



