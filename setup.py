#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
import os

from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

def _lines_from_file(filename):
    with open(filename) as f:
        return f.read().splitlines()


# version
here = os.path.dirname(os.path.abspath(__file__))
version = next((line.split('=')[1].strip().replace("'", "")
                for line in _lines_from_file(os.path.join(here, 'yfjquote', '__init__.py'))
                if line.startswith('__version__ = ')),
                '0.0.dev0')

setup(
    name='yfjquote',
    version=version,
    url='https://github.com/survivor7777777/yfjquote',
    author='survivor7777777',
    author_email='leukemic.survivor@gmail.com',
    description='Stock Quote Extraction from Yahoo! Japan Finance with Python',
    long_description=readme,
    packages=find_packages(),
    install_requires=_lines_from_file('requirements.txt'),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Software Development :: Libraries'
    ],
    python_requires='>=3',
    extras_require={
        "tests": _lines_from_file(filename='tests/requirements.txt'),
        "docs": _lines_from_file(filename='docs/requirements.txt'),
    },
    project_urls={
        'Bug Reports': 'https://github.com/survivor7777777/yfjquote/issues',
        'Source': 'https://github.com/survivor7777777/yfjquote',
        'Documentation': 'https://github.com/survivor7777777/yfjquote',
    },
)
