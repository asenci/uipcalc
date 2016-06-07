from setuptools import setup, find_packages

install_requires = [
    'six',
]
tests_require = [
    'nose',
    'tox',
]

try:
    import ipaddress
except ImportError:
    install_requires.append('ipaddress')

setup(
    name='uipcalc',
    description='Universal (IPv4/IPv6) IP address and netmask calculator',
    long_description=open('README.rst').read(),
    version='0.3.1',
    author='Andre Sencioles',
    author_email='asenci@gmail.com',
    license='ISC License',
    url='https://bitbucket.org/asenci/uipcalc/',
    download_url='https://pypi.python.org/pypi/uipcalc',

    platforms='any',
    keywords='ip ipv4 ipv6 calculator',
    classifiers=[
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

    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'uipcalc = uipcalc:main',
        ],
    },

    install_requires=install_requires,
    extras_require={
        ':python_version<"3.3"': ['ipaddress']
    },
    tests_require=tests_require,
    test_suite='nose.collector',
)
