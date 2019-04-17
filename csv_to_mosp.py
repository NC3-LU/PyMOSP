#! /usr/bin/env python
# -*- coding: utf-8 -

import csv
import json
import requests

import config

HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}
LANGUAGES = {'EN': '2', 'FR': '1', 'DE': '3', 'NL': '4'}
LANGUAGE = 'EN'

CSV_FILE = 'vulnerabilities.csv'
VALIDATING_SCHEMA = 14 # https://objects.monarc.lu/schema/14
OWNING_ORGANIZATION = 4 # https://objects.monarc.lu/organization/MONARC


if name == '__main__':
    objects = []
    # Loads the objects from the CSV file
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            objects.append({
                'name': row['label'+LANGUAGES[LANGUAGE]],
                'description': row['description'+LANGUAGES3[LANGUAGE]],
                'language': LANGUAGE,
                'org_id': OWNING_ORGANIZATION,
                'schema_id': VALIDATING_SCHEMA,
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
    for obj in objects:
        r = requests.post(config.MOSP_API,
                          auth=(config.USERNAME, config.PASSWORD),
                          headers=HEADERS,
                          data=json.dumps(obj))
        if r.status_code != 201:
            print(r.status_code)
            print(r.reason)
            print(obj)


