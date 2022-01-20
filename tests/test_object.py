#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

import pymosp


class TestObject(unittest.TestCase):
    def setUp(self):
        mosp_instance = os.getenv("MOSP_INSTANCE", "https://objects.monarc.lu/api/v2/")
        token = os.getenv("MOSP_TOKEN")
        self.mosp = pymosp.PyMOSP(mosp_instance, token)

    def test_get_all_objects(self):
        r = self.mosp.objects()
        assert r["metadata"]["count"] != "0", "no result"

    def test_get_all_objects_from_unknown_org(self):
        r = self.mosp.objects(params={"organization": "Unknown org"})
        assert r["metadata"]["count"] == "0"

    def test_object_with_uuid_and_language(self):
        r = self.mosp.objects(
            params={"uuid": "69fbfe14-4591-11e9-9173-0800277f0571", "language": "EN"}
        )
        assert r["metadata"]["count"] == "1"
        assert r["data"][0]["name"] == "The principle of least privilege is not applied"

    def test_create_obect_and_delete(self):
        new_objects = [
            {
                "name": "Possibility of installing correction programmes, etc.",
                "description": "Description of the new object.",
                "licenses": [{"license_id": "CC0-1.0"}],
                "schema_id": 3,
                "org_id": 1,
                "json_object": {
                    "code": "10",
                    "description": "Description of the new object.",
                    "label": "Possibility of installing correction programmes, etc.",
                    "type": "Primary",
                    "version": 1,
                    "language": "EN",
                    "uuid": "69fbfe01-4591-11e9-9173-0800277f0572",
                }
            }
        ]
        # Check that the object has been created
        r = self.mosp.add_objects(new_objects)
        assert r["metadata"]["count"] == "1"

        # Delete the created object and check the result code
        r = self.mosp.delete_object(r["data"][0]["id"])
        assert 204 == r

    def test_create_obect_with_bad_schema(self):
        new_objects = [
            {
                "name": "Possibility of installing correction programmes, patches, etc.",
                "description": "Description of the new object.",
                "licenses": [{"license_id": "CC0-1.0"}],
                "schema_id": 2,
                "org_id": 1,
                "json_object": {
                    "code": "10",
                    "description": "",
                    "label": "Possibility of installing correction programmes, patches, etc.",
                    "language": "EN",
                    "uuid": "69fbfe01-4591-11e9-9173-0800277f0572",
                },
            }
        ]
        r = self.mosp.add_objects(new_objects)
        assert "The object submited is not validated by the schema" in r["description"]
