#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import unittest

import pymosp


class TestObject(unittest.TestCase):
    def setUp(self):
        token = os.getenv("MOSP_TOKEN")
        self.mosp = pymosp.PyMOSP("https://objects.monarc.lu/api/v2/", token)

    def test_get_all_objects(self):
        r = self.mosp.objects()
        assert r.json()["metadata"]["count"] != 0, "no result"
