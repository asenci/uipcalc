from distutils.core import setup

setup(
    name='uipcalc',
    version='0.1',
    scripts=['uipcalc.py'],
    url='https://bitbucket.org/asenci/uipcalc',
    license='ISC License',
    author='Andre Sencioles Vitorio Oliveira',
    author_email='andre@bcp.net.br',
    description='Universal (IPv4/IPv6) CIDR calculator',
    requires=['ipaddr'],
)