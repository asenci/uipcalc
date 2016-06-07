uipcalc
=======

Universal (IPv4/IPv6) CIDR calculator

Source available at: http://bitbucket.org/asenci/uipcalc/

Please report any issues at: http://bitbucket.org/asenci/uipcalc/issues/


Installing:
-----------

::

    $ pip install uipcalc


Usage:
------

::

    uipcalc [-h] address

    Universal (IPv4/IPv6) IP address and netmask calculator

    positional arguments:
      address     IP address with netmask in CIDR or dotted-decimal notation

    optional arguments:
      -h, --help  show this help message and exit


Examples:
---------

::

    $ uipcalc 192.0.2.4/12
    Number of addresses:  1048576

    Network:    192.0.0.0
    Broadcast:  192.15.255.255
    Netmask:    255.240.0.0 (12)

    Network:    11000000.0000 0000.00000000.00000000
    Broadcast:  11000000.0000 1111.11111111.11111111
    Netmask:    11111111.1111 0000.00000000.00000000

    $ uipcalc 192.0.2.4/255.255.255.192
    Number of addresses:  64

    Network:    192.0.2.0
    Broadcast:  192.0.2.63
    Netmask:    255.255.255.192 (26)

    Network:    11000000.00000000.00000010.00 000000
    Broadcast:  11000000.00000000.00000010.00 111111
    Netmask:    11111111.11111111.11111111.11 000000

    $ uipcalc 2001:DB8::/48
    Number of addresses:  1208925819614629174706176

    Network:    2001:0db8:0000:0000:0000:0000:0000:0000
    Broadcast:  2001:0db8:0000:ffff:ffff:ffff:ffff:ffff
    Netmask:    ffff:ffff:ffff:0000:0000:0000:0000:0000 (48)

    Network:    0010000000000001.0000110110111000.0000000000000000. 0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000
    Broadcast:  0010000000000001.0000110110111000.0000000000000000. 1111111111111111.1111111111111111.1111111111111111.1111111111111111.1111111111111111
    Netmask:    1111111111111111.1111111111111111.1111111111111111. 0000000000000000.0000000000000000.0000000000000000.0000000000000000.0000000000000000

    $ uipcalc 2001:DB8::/60
    Number of addresses:  295147905179352825856

    Network:    2001:0db8:0000:0000:0000:0000:0000:0000
    Broadcast:  2001:0db8:0000:000f:ffff:ffff:ffff:ffff
    Netmask:    ffff:ffff:ffff:fff0:0000:0000:0000:0000 (60)

    Network:    0010000000000001.0000110110111000.0000000000000000.000000000000 0000.0000000000000000.0000000000000000.0000000000000000.0000000000000000
    Broadcast:  0010000000000001.0000110110111000.0000000000000000.000000000000 1111.1111111111111111.1111111111111111.1111111111111111.1111111111111111
    Netmask:    1111111111111111.1111111111111111.1111111111111111.111111111111 0000.0000000000000000.0000000000000000.0000000000000000.0000000000000000


Requirements:
-------------

- Python 2 >= 2.7 or Python 3 >= 3.4
- ipaddress (for Python < 3.3)
- six

License:
--------

Licensed under ISC license.

See `LICENSE.txt <http://bitbucket.org/asenci/uipcalc/raw/master/LICENSE.txt>`_ file for details.
