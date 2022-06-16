# -*- coding: utf-8 -*-

"""
API.
"""
import sys
from typing import List, Dict, Union, Mapping, Iterable

import requests
from urllib.parse import urljoin

from .exceptions import NoURL
from .mospobject import MOSPObject


class PyMOSP:
    """Python API to access MOSP.

    :param url: URL of the MOSP instance you want to connect to
    :param key: API key of the user you want to use
    """

    def __init__(self, url: str, key: str):
        if not url:
            raise NoURL("Please provide the URL of your MOSP instance.")
        self.root_url = url
        self.key: str = key

    # ## BEGIN Objects ##

    def objects(
        self, params: Mapping = {}, pythonify: bool = False
    ) -> Union[Dict, List[MOSPObject]]:
        """Get all the objects from the MOSP instance.
        Filters can be used with the ``params`` parameter.

        >>> params = {"organization": "MONARC", "schema": "Library objects"}
        >>> r = mosp.objects(params=params)
        """
        r = self._prepare_request("GET", "object", params=params)
        return r.json()

    def add_objects(
        self, objects: List[MOSPObject], pythonify: bool = False
    ) -> Union[Dict, List[MOSPObject]]:
        """Add one or several objects on a MOSP instance.

        :param objects: list of objects to add
        :param pythonify: Returns a PyMOSP Object instead of the plain json output

        >>> mosp = pymosp.PyMOSP(mosp_instance, token)
        >>> new_objects = [
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
        >>> r = mosp.add_objects(new_objects)
        """

        r = self._prepare_request("POST", "object/", data=objects)
        return r.json()

    def delete_object(self, id: int) -> int:
        """Delete an object from a MOSP instance.
        Returns the HTTP status code from the MOSP instance.

        :param id: The id of the object to delete.
        """
        r = self._prepare_request("DELETE", "object/{}".format(id))
        return r.status_code

    # ## BEGIN Schemas ##

    def schemas(
        self, params: Mapping = {}, pythonify: bool = False
    ) -> Union[Dict, List[MOSPObject]]:
        """Get all the schemas from the MOSP instance."""
        r = self._prepare_request("GET", "schema", params=params)
        return r.json()

    # Helpers

    def _prepare_request(
        self,
        request_type: str,
        url: str,
        data: Union[str, Iterable, Mapping] = {},
        params: Mapping = {},
    ) -> requests.Response:
        url = urljoin(self.root_url, url)

        user_agent = f'PyMOSP - Python {".".join(map(str, sys.version_info[:2]))}'
        headers = {
            "X-API-KEY": self.key,
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": user_agent,
        }

        r = requests.request(
            request_type, url, headers=headers, json=data, params=params
        )
        # objects_r = self._check_json_response(r)

        # print(r.json())

        return r

    # def _check_json_response(self, response: requests.Response) -> Dict:  # type: ignore
    #     r = self._check_response(response, expect_json=True)
    #     if isinstance(r, (dict, list)):
    #         return r
