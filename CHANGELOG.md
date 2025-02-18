Changelog
=========

v0.5.3 (2025-02-18)
-------------------

Changes
~~~~~~~

- Updated dependencies.
- The project is now using Trusted Publishing with Pypi.


v0.5.2 (2024-02-13)
-------------------

Updated Python minimum requirements and dependencies.


v0.5.0 (2022-01-20)
-------------------

New
~~~
- [object] it is now possible to delete an object from a MOSP instance
  with the API. [Cédric Bonhomme]

Changes
~~~~~~~
- [dependencies] Updated Python dependencies. [Cédric Bonhomme]
- [tests] rename a test name. [Cédric Bonhomme]
- Get MOSP instance URL from environment variable. [Cédric Bonhomme]
- [workflow] Updated GitHub workflow. [Cédric Bonhomme]
- [tests] enable test_create_object. [Cédric Bonhomme]
- [tests] tests are now using the test instance of MOSP. [Cédric
  Bonhomme]

Fix
~~~
- [typing] delete_object returns the id of the deleted object. [Cédric
  Bonhomme]
- Fixed an issue when creating new objects. [Cédric Bonhomme]
- [workflow] Updated GitHub workflow. [Cédric Bonhomme]


v0.4.3 (2022-01-12)
-------------------

Changes
~~~~~~~
- [dependencies] Updated request and mypy. [Cédric Bonhomme]
- Cosmethic changes. [Cédric Bonhomme]
- Fixed conflict in AUTHORS.md file. [Cédric Bonhomme]
- Minor changes in README file. [Cédric Bonhomme]

Fix
~~~
- [tests] fixed key name of the result. [Cédric Bonhomme]
- Removed useless import and fixed duplicate value in mospobject.py.
  [Cédric Bonhomme]

Other
~~~~~
- Merge branch 'master' of github.com:CASES-LU/PyMOSP. [Cédric Bonhomme]
- PEP 561 -- Distributing and Packaging Type Information. [Cédric
  Bonhomme]


v0.4.2 (2021-03-31)
-------------------

Changes
~~~~~~~
- [core] Python requirement set to >=3.8,<4.0. [Cédric Bonhomme]

Other
~~~~~
- Updated README for the new release. [Cédric Bonhomme]


v0.4.1 (2021-03-30)
-------------------

Changes
~~~~~~~
- [release] Bumped version number. [Cédric Bonhomme]

Fix
~~~
- [documentation] fix the documentation in the README.
  #HowToFuckUpARelease. [Cédric Bonhomme]

Other
~~~~~
- Updated README. [Cédric Bonhomme]


v0.4.0 (2021-03-30)
-------------------

New
~~~
- [command line] It is now possible to use PyMOSP as a command line
  tool. Only for listing objects for the moment. [Cédric Bonhomme]
- [objects] Added creation of objects and some tests. [Cédric Bonhomme]
- [tests] added files for the future tests on JSON schemas. [Cédric
  Bonhomme]

Changes
~~~~~~~
- [release] Bumped version number. [Cédric Bonhomme]
- [tests] Lint with Flake8. [Cédric Bonhomme]
- [tests] added test on get objects with uuid and language. [Cédric
  Bonhomme]
- Updated .gitgignore to ignore .python-version file. [Cédric Bonhomme]

Fix
~~~
- Typo. [Cédric Bonhomme]
- [documentation] Fixed example file. [Cédric Bonhomme]
- [type] Fixed type of result of objects() and add_objects() function.
  [Cédric Bonhomme]

Other
~~~~~
- Updated chagenlog. [Cédric Bonhomme]
- Updated chagenlog. [Cédric Bonhomme]
- Updated README and pyproject.toml. [Cédric Bonhomme]
- Fixed bad format of link in README. [Cédric Bonhomme]
- Replaced str by map when joining Python version number. [Cédric
  Bonhomme]
- Removed useless file. [Cédric Bonhomme]


v0.3.0 (2021-03-26)
-------------------

Changes
~~~~~~~
- [tests] added test_object.test_get_all_objects_from_unknown_org.
  [Cédric Bonhomme]
- [tests] only use Python 3.9. [Cédric Bonhomme]
- The library is now using the API v2 of MOSP. [Cédric Bonhomme]

Fix
~~~
- The result was a string. [Cédric Bonhomme]

Other
~~~~~
- Updated README and changelog. [Cédric Bonhomme]
- New [tests] Added Python unittests and GitHub workflow for the tests.
  [Cédric Bonhomme]
- Added support for params for MOSP objects and schemas. [Cédric
  Bonhomme]
- The project is now using Poetry. [Cédric Bonhomme]
- Updated README. [Cédric Bonhomme]
- Added module which will implements the PyMOSP API. [Cédric Bonhomme]
- Added files for pypi.org. [Cédric Bonhomme]
- Install PyMOSP with pipx ;-) [Cédric Bonhomme]
- Added default README file. [Cédric Bonhomme]
- Added first files. [Cédric Bonhomme]
- Added Pipfile and Pipfile.lock files. [Cédric Bonhomme]
- Cosmethic changes. [Cédric Bonhomme]
- Default language is EN. [Cédric Bonhomme]
- Cleaned code. [Cédric Bonhomme]
- Initial commit. [Cédric Bonhomme]
