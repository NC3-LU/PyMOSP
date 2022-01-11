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
        """Get all the events from the MOSP instance."""
        r = self._prepare_request("GET", "object", params=params)
        return r.json()

    def add_objects(
        self, objects: List[MOSPObject], pythonify: bool = False
    ) -> Union[Dict, List[MOSPObject]]:
        """Add a new object on a MOSP instance.

        :param objects: event to add
        :param pythonify: Returns a PyMOSP Object instead of the plain json output
        """

        r = self._prepare_request("POST", "object", data=objects)
        return r.json()

    # ## BEGIN Schemas ##

    def schemas(
        self, params: Mapping = {}, pythonify: bool = False
    ) -> Union[Dict, List[MOSPObject]]:
        """Get all the events from the MOSP instance."""
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
