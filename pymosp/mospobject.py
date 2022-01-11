# -*- coding: utf-8 -*-

from datetime import datetime


class MOSPObject:
    def __init__(self):
        self.name: str
        self.description: str
        self.last_updated: datetime
        self.json_object: dict
