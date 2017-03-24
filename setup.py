import codecs
import os

from setuptools import setup, find_packages

NAME = 'uipcalc'

install_requires = [
    'clint',
    'six',
]

setup_requires = [
    'pytest-runner',
    'setuptools-git',
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


def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts)) as file:
        return file.read()


def about(attr):
    about_file = '{}/about.py'.format(NAME)
    content = read(about_file)

    runtime_globals = runtime_locals = {}
    # noinspection PyCompatibility
    exec(content, runtime_globals, runtime_locals)

    return runtime_globals.get('__{}__'.format(attr), '')


setup(
    name=NAME,
    description=about('description'),
    long_description=read('README.rst'),
    version=about('version'),

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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ],
    keywords='ip ipv4 ipv6 net subnet network netmask calc calculator',

    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            '{} = {}:main.run'.format(NAME, NAME),
        ],
    },

    install_requires=install_requires,
    extras_require=extras_require,
    setup_requires=setup_requires,
    tests_require=tests_require,
)
