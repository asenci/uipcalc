"""
Setup script for uipcalc
"""

import sys
from setuptools import setup


install_requires = ['six']
test_requirements = ['nose', 'tox']

if sys.version_info[:2] < (2, 7):
    install_requires.append('argparse')

if sys.version_info[:2] < (3, 3):
    install_requires.append('ipaddress')


setup(
    name='uipcalc',
    description='Universal (IPv4/IPv6) IP address and netmask calculator',
    long_description=open('README.rst').read(),
    url='http://bitbucket.org/asenci/uipcalc/',

    author='Andre Sencioles Vitorio Oliveira',
    author_email='asenci@gmail.com',
    license='ISC License',

    version='0.3',

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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

    py_modules=['uipcalc'],
    entry_points={'console_scripts': ['uipcalc = uipcalc:main']},
    test_suite='test_uipcalc',

    install_requires=install_requires,
    test_requirements=test_requirements,
)
