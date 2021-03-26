#! /usr/bin/env python
# -*- coding: utf-8 -

"""create_amvs.py

This script requires 4 CSV input files:
- amvs.csv;
- assets.csv;
- threats.csv;
- vulnerabilities.

The amvs will be created on the remote MOSP instance
with the relations to the corresponding objects
(assets, threats, vulnerabilities).
"""

import csv
import json
import requests

import config

HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}
LANGUAGES = {'EN': '2', 'FR': '1', 'DE': '3', 'NL': '4'}
LANGUAGE = 'EN'

VALIDATING_SCHEMA = 16 # https://objects.monarc.lu/schema/view/16
OWNING_ORGANIZATION = 4


if __name__ == '__main__':
    # Point of entry in execution mode
    assets = {}
    with open('assets.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            assets[row['uuid']] = {
                'FR': row['label1'],
                'EN': row['label2'],
                'DE': row['label3'],
                'NL': row['label4']
            }
            
    threats = {}
    with open('threats.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            threats[row['uuid']] = {
                'FR': row['label1'],
                'EN': row['label2'],
                'DE': row['label3'],
                'NL': row['label4']
            }
            
    vulnerabilities = {}
    with open('vulnerabilities.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vulnerabilities[row['uuid']] = {
                'FR': row['label1'],
                'EN': row['label2'],
                'DE': row['label3'],
                'NL': row['label4']
            }
    

    objects = []
    with open('amvs.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            asset_name = assets[row['asset_id']][LANGUAGE]
            r = requests.get('https://objects.monarc.lu/api/v1/json_object?q=' +
                            '{"filters":[{"name":"schema","op":"has","val":' +
                            '{"name":"name","op":"eq","val": "Assets"}},'+
                            '{"name":"name","op":"eq","val":"'+ asset_name +'"}]}')
            res = json.loads(r.content)
            asset_id = res['objects'][0]['id']

            threat_name = threats[row['threat_id']][LANGUAGE]
            r = requests.get('https://objects.monarc.lu/api/v1/json_object?q=' +
                            '{"filters":[{"name":"schema","op":"has","val":' +
                            '{"name":"name","op":"eq","val": "Threats"}},' +
                            '{"name":"name","op":"eq","val":"'+ threat_name +'"}]}')
            res = json.loads(r.content)
            threat_id = res['objects'][0]['id']

            vulnerability_name = vulnerabilities[row['vulnerability_id']][LANGUAGE]
            r = requests.get('https://objects.monarc.lu/api/v1/json_object?q=' +
                            '{"filters":[{"name":"schema","op":"has","val":' +
                            '{"name":"name","op":"eq","val": "Vulnerabilities"}},' +
                            '{"name":"name","op":"eq","val":"'+ vulnerability_name +'"}]}')
            res = json.loads(r.content)
            vulnerability_id = res['objects'][0]['id']

            #print(asset_id, threat_id, vulnerability_id)

            objects.append({
                'name': row['uuid'],
                'description': 'Asset: ' + asset_name +
                                '. Threat: ' +threat_name +
                                '. Vulnerability: ' + vulnerability_name,
                'org_id': OWNING_ORGANIZATION,
                'schema_id': VALIDATING_SCHEMA,
                'licenses': [{'id': 92}],
                'refers_to': [{'id':asset_id}, {'id':threat_id}, {'id':vulnerability_id}],
                'json_object': {
                    'uuid': row['uuid'],
                    'asset': row['asset_id'],
                    'threat': row['threat_id'],
                    'vulnerability': row['vulnerability_id'],
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
