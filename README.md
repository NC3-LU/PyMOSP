# PyMOSP

[![Latest release](https://img.shields.io/github/release/CASES-LU/PyMOSP.svg?style=flat-square)](https://github.com/CASES-LU/PyMOSP/releases/latest)
[![License](https://img.shields.io/github/license/CASES-LU/PyMOSP.svg?style=flat-square)](https://www.gnu.org/licenses/agpl-3.0.html)
[![Workflow](https://github.com/CASES-LU/PyMOSP/workflows/Python%20application/badge.svg?style=flat-square)](https://github.com/CASES-LU/PyMOSP/actions?query=workflow%3A%22Python+application%22)
[![PyPi version](https://img.shields.io/pypi/v/pymosp.svg?style=flat-square)](https://pypi.org/project/pymosp)


PyMOSP is a Python library to access [MOSP](https://github.com/CASES-LU/MOSP).


## Installation

### Use it as a command line tool

```bash
$ pipx install pymosp
installed package pymosp 0.4.0, Python 3.9.2
These apps are now globally available
  - pymosp
done! ✨ 🌟 ✨

$ export MOSP_URL_API=https://objects.monarc.lu/api/v2/
$ export TOKEN=<YOUR-TOKEN>

$ pymosp object --list
{'metadata': {'count': '5074', 'offset': '0', 'limit': '10'}, 'data': [{'id': 144, 'name': 'Use of an obsolete version of the messaging server', 'description': '', 'schema_id': 14, 'org_id': 4, 'last_updated': '2021-03-16T12:45:35.046659', 'json_object': {'code': '1118', 'uuid': '69fc03a0-4591-11e9-9173-0800277f0571', 'label': 'Use of an obsolete version of the messaging server', 'language': 'EN', 'description': ''}, 'organization': {'id': 4, 'name': 'MONARC', 'description': 'MONARC is a tool and a method allowing an optimised, precise and repeatable risk assessment.', 'organization_type': 'Non-Profit', 'is_membership_restricted': True, 'last_updated': '2018-05-18T09:50:57'}, 'licences': None},  ... ,  {'id': 284, 'name': 'Tempting equipment (trading value, technology, strategic)', 'description': '', 'schema_id': 14, 'org_id': 4, 'last_updated': '2021-03-16T12:45:33.862787', 'json_object': {'code': '278', 'uuid': '69fc0ee2-4591-11e9-9173-0800277f0571', 'label': 'Tempting equipment (trading value, technology, strategic)', 'language': 'EN', 'description': ''}, 'organization': {'id': 4, 'name': 'MONARC', 'description': 'MONARC is a tool and a method allowing an optimised, precise and repeatable risk assessment.', 'organization_type': 'Non-Profit', 'is_membership_restricted': True, 'last_updated': '2018-05-18T09:50:57'}, 'licences': None}]}
```

### Use it as a Python library

```bash
pip install pymosp
```

```python
import pymosp, os
mosp = pymosp.PyMOSP(os.getenv("MOSP_URL_API"), os.getenv("TOKEN"))
params = {"organization": "MONARC", "schema": "Library objects"}
r = mosp.objects(params=params)
print(r)
```


or via the Git repository:

```bash
$ git clone https://github.com/CASES-LU/PyMOSP
$ cd PyMOSP
$ poetry install
$ poetry run nose2 -v --pretty-assert
```


## Examples

See the examples in the file [example.py](example.py) or in the tests folder.


## License

This software is licensed under
[GNU General Public License version 3](https://www.gnu.org/licenses/gpl-3.0.html).

* Copyright (C) 2019-2022 Cédric Bonhomme
* Copyright (C) 2019-2022 SECURITYMADEIN.LU

For more information, [the list of authors and contributors](AUTHORS.md)
is available.
