import codecs
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test


class PyTest(test):
    user_options = [
        ('pytest-args=', 'a', "Arguments to pass to py.test"),
    ]

    def initialize_options(self):
        super(PyTest, self).initialize_options()
        self.pytest_args = []

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.pytest_args))


class Tox(test):
    user_options = [
        ('tox-args=', 'a', "Arguments to pass to tox"),
    ]

    def initialize_options(self):
        super(Tox, self).initialize_options()
        self.tox_args = []

    def finalize_options(self):
        super(Tox, self).finalize_options()
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        import shlex
        if self.tox_args:
            self.tox_args = shlex.split(self.tox_args)
        sys.exit(tox.cmdline(args=self.tox_args))


def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts)) as file:
        return file.read()


NAME = 'uipcalc'
DESCRIPTION = 'Universal (IPv4/IPv6) IP address and netmask calculator'
KEYWORDS = 'ip ipv4 ipv6 net subnet network netmask calc calculator'
VERSION = '0.4'


install_requires = [
    'clint',
    'six',
]

setup_requires = [
    'wheel',
]

tests_require = [
    'pytest',
    'tox',
]


setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=read('README.rst'),
    keywords=KEYWORDS,
    version=VERSION,

    author='Andre Sencioles',
    author_email='asenci@gmail.com',
    license='ISC License',
    url='https://bitbucket.org/asenci/{}/'.format(NAME),

    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Console :: Curses',
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

    install_requires=install_requires,
    extras_require={
        ':python_version<"3.3"': ['ipaddress'],
        'setup': setup_requires,
        'testing': tests_require,
    },
    setup_requires=setup_requires,
    tests_require=tests_require,
    cmdclass={
        'pytest': PyTest,
        'tox': Tox,
    },
)
