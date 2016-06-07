import os
import codecs
from setuptools import setup, find_packages


def read(*parts):
    return codecs.open(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), *parts)).read()


tests_require = ['nose', 'tox']

setup(
    name='uipcalc',
    description='Universal (IPv4/IPv6) IP address and netmask calculator',
    long_description=read('README.rst'),
    version='0.3.2',
    author='Andre Sencioles',
    author_email='asenci@gmail.com',
    license='ISC License',
    url='https://bitbucket.org/asenci/uipcalc/',

    platforms='any',
    keywords='ip ipv4 ipv6 net subnet network netmask calc calculator',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        # 'Environment :: Console :: Curses',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ],

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'uipcalc = uipcalc:main',
        ],
    },

    install_requires=['six'],
    extras_require={
        ':python_version<"3.3"': ['ipaddress'],
        'testing': tests_require
    },
    tests_require=tests_require,
    test_suite='nose.collector',
)
