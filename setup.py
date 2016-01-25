#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) Jean-Paul Calderone 2008-2015, All rights reserved
#

"""
Installation script for the NFC module
"""

from setuptools import setup


# XXX Deduplicate this
__version__ = '0.10.2'

setup(name='nfc', version=__version__,
      packages = ['nfc','nfc.clf','nfc.handover','nfc.llcp','nfc.ndef','nfc.snep','nfc.tag'],
      description = 'Python NFC libraries',
      url = 'https://launchpad.net/nfcpy',
      install_requires=["pyusb>=1.0.0b2"],
      classifiers = [
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',

        # General classifiers to indicate "this project supports Python 2" and
        # "this project supports Python 3".
        'Programming Language :: Python :: 2',
        # In particular, this makes pyOpenSSL show up on
        # https://pypi.python.org/pypi?:action=browse&c=533&show=all and is in
        # accordance with
        # http://docs.python.org/2/howto/pyporting.html#universal-bits-of-advice
        'Programming Language :: Python :: 3',

        # More specific classifiers to indicate more precisely which versions
        # of those languages the project supports.
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        ],
)
