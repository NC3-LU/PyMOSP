#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

import pymosp


class TestObject(unittest.TestCase):
    def setUp(self):
        token = os.getenv("MOSP_TOKEN")
        self.mosp = pymosp.PyMOSP("https://objects.monarc.lu/api/v2/", token)

    def test_get_all_objects(self):
        r = self.mosp.objects()
        assert r.json()["metadata"]["count"] != "0", "no result"

    def test_get_all_objects_from_unknown_org(self):
        r = self.mosp.objects(params={"organization": "Unknown org"})
        assert r.json()["metadata"]["count"] == "0"

    def test_object_with_uuid_and_language(self):
        r = self.mosp.objects(
            params={"uuid": "69fbfe14-4591-11e9-9173-0800277f0571", "language": "EN"}
        )
        assert r.json()["metadata"]["count"] == "1"
        assert (
            r.json()["data"][0]["name"]
            == "The principle of least privilege is not applied"
        )
