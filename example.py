# -*- coding: utf-8 -*

import pymosp

try:
    from config import CONFIG
except Exception as e:
    CONFIG = {"MOSP_URL_API": "https://objects.monarc.lu/api/v2/", "TOKEN": ""}


# Instantiate a MOSP connection object
mosp = pymosp.PyMOSP(CONFIG.get("MOSP_URL_API"), CONFIG.get("TOKEN"))


print("Objects:")
mosp.objects()

print("Schemas:")
mosp.schemas()
