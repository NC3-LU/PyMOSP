#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = [
]

scripts = [
]

requires = ['request']

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    readme = f.read()
with codecs.open(os.path.join(here, 'CHANGELOG.rst'), encoding='utf-8') as f:
    changelog = f.read()

setup(
    name='PyMOSP',
    version='0.1',
    author='Cédric Bonhomme',
    author_email='cedric@cedricbonhomme.org',
    packages=packages,
    include_package_data=True,
    scripts=scripts,
    url='https://github.com/CASES-LU/PyMOSP',
    description='Python Library to access MOSP',
    long_description=readme + '\n|\n\n' + changelog,
    platforms = ['Linux'],
    license='GPLv3',
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
    ]
)
