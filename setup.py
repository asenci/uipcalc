"""
Setup script for uipcalc
"""

import sys
from setuptools import setup


install_requires = ['six']
tests_require = ['nose', 'tox']

if sys.version_info[:2] < (3, 3):
    install_requires.append('ipaddress')


setup(
    name='uipcalc',
    description='Universal (IPv4/IPv6) IP address and netmask calculator',
    long_description=open('README.rst').read(),
    url='https://bitbucket.org/asenci/uipcalc/',
    download_url='https://pypi.python.org/pypi/uipcalc',

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

    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'uipcalc = uipcalc:main',
        ],
    },

    install_requires=install_requires,

    tests_require=tests_require,
    test_suite='nose.collector',
)
