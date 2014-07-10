"""
Setup script for uipcalc
"""

import sys
from setuptools import setup

import uipcalc


install_requires = [
    'ipaddr>=2.1',
]

if sys.version_info[:2] < (2, 7):
    install_requires.append('argparse')


setup(
    name=uipcalc.__title__,
    description=uipcalc.__summary__,
    long_description=open('README.rst').read(),
    url=uipcalc.__url__,

    author=uipcalc.__author__,
    author_email=uipcalc.__email__,
    license=uipcalc.__license__,

    version=uipcalc.__version__,

    platforms='any',
    keywords=['ip', 'ipv4', 'ipv6', 'calculator'],
    classifiers=[
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

    entry_points={'console_scripts': ['uipcalc = uipcalc:main']},
    test_suite='test_uipcalc',

    install_requires=install_requires
)
