from __future__ import absolute_import, print_function

import io

from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext
from setuptools import setup, find_packages


PKG_NAME = 'uipcalc'


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


def about(attr):
    _globals = {}
    exec(read(join(dirname(__file__), 'src', PKG_NAME, 'about.py')), _globals)

    return _globals.get('__{}__'.format(attr), '')


setup(
    name=PKG_NAME,
    description=about('description'),
    long_description=read('README.rst'),
    version=about('version'),

    author='Andre Sencioles',
    author_email='asenci@gmail.com',
    license='ISC License',
    url='https://bitbucket.org/asenci/{}/'.format(PKG_NAME),

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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ],
    keywords='ip ipv4 ipv6 net subnet network netmask calc calculator',

    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude=['tests', 'tests.*']),
    py_modules=[splitext(basename(i))[0] for i in glob(join('src', '*.py'))],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            '{} = {}:main.run'.format(PKG_NAME, PKG_NAME),
        ],
    },

    install_requires=[
        'clint',
        'six',
    ],
    extras_require={
        'setup': [
            'wheel',
        ],

        'testing': [
            'pytest',
            'tox',
        ],

        ':python_version<"3.3"': ['ipaddress'],
    },
)
