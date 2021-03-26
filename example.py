# -*- coding: utf-8 -*

import pymosp

try:
    from config import CONFIG
except Exception as e:
    CONFIG = {"MOSP_URL_API": "https://objects.monarc.lu/api/v2/", "TOKEN": ""}


# Instantiate a MOSP connection object
mosp = pymosp.PyMOSP(CONFIG.get("MOSP_URL_API"), CONFIG.get("TOKEN"))


# List all objects without filters
print("Objects:")
mosp.objects()
print("="*79)

# List all objects from an unknown organization
print("Objects with params:")
params = {"organization": "Unknown org"}
mosp.objects(params=params)
print("="*79)

# List objects validated by a schema from a specific organization
print("Objects with params:")
params = {"organization": "MONARC", "schema": "Library objects"}
mosp.objects(params=params)
print("="*79)


# print("Schemas:")
mosp.schemas()
