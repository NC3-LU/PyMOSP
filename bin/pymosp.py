#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PyMOSP - PyMOSP is a Python library to access MOSP.
# Copyright (C) 2019-2022 Cédric Bonhomme - https://www.cedricbonhomme.org
# Copyright (C) 2019-2022 SECURITYMADEIN.LU
#
# For more information : https://github.com/CASES-LU/PyMOSP
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import os
import argparse

try:
    import pymosp
except Exception:
    print("Install PyMOSP: pipx install pymosp")


def main():
    try:
        py_mosp = pymosp.PyMOSP(os.getenv("MOSP_URL_API", ""), os.getenv("TOKEN", ""))
    except Exception as e:
        print(e)

    parser = argparse.ArgumentParser(prog="PyMOSP")
    subparsers = parser.add_subparsers(help="sub-command help", dest="command")

    # Subparser: Object
    parser_object = subparsers.add_parser("object", help="object help")
    parser_object.add_argument(
        "--list", default=True, action=argparse.BooleanOptionalAction
    )

    arguments = parser.parse_args()

    if arguments.command == "object":
        if arguments.list:
            r = py_mosp.objects()
            print(r)


if __name__ == "__main__":
    main()
