import codecs
import os

from setuptools import setup, find_packages


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
    'pytest-runner',
    'wheel',
]

tests_require = [
    'pytest',
]

extras_require = {
    'setup': setup_requires,
    'testing': tests_require,

    ':python_version<"3.3"': ['ipaddress'],
}


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
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
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
    extras_require=extras_require,
    setup_requires=setup_requires,
    tests_require=tests_require,
)
