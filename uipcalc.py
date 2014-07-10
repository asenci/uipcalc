"""
uipcalc - Universal (IPv4/IPv6) IP address and netmask calculator

Copyright (c) 2011 Andre Sencioles Vitorio Oliveira <andre@bcp.net.br>

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

from __future__ import print_function

# TODO: add support for Python3
import ipaddr

# noinspection PyCompatibility
import argparse


__title__ = 'uipcalc'
__summary__ = 'Universal (IPv4/IPv6) IP address and netmask calculator'
__url__ = 'http://bitbucket.org/asenci/uipcalc'

__version__ = '0.2.1'

__author__ = 'Andre Sencioles Vitorio Oliveira'
__email__ = 'andre@bcp.net.br'

__license__ = 'ISC License'


def address_to_bin(address):
    """Converts an dotted-decimal (IPv4) or groups of hexadecimals (IPv6)
    formatted address to a binary representation

    :param _BaseIP address: The IP address
    :return: A binary representation of the IP address
    :rtype: str
    """

    # IPv4
    if address.version == 4:
        return '.'.join([bin(int(x))[2:].zfill(8)
                         for x in address.exploded.split('.')])

    # IPv6
    else:
        return '.'.join([bin(int(x, 16))[2:].zfill(16)
                         for x in address.exploded.split(':')])


# noinspection PyDocstring
def main():

    parser = argparse.ArgumentParser(description=__summary__)
    parser.add_argument(
        'address', help='IP address with optional netmask in CIDR notation')
    parser.add_argument(
        'netmask', nargs='?', help='Netmask in dotted-decimal notation')
    args = parser.parse_args()

    if args.netmask:

        if '/' in args.address:
            return parser.error(
                'The netmask must be specified either in CIDR or doted-quad'
                ' notation.')

        args.address += '/' + args.netmask

    try:
        network = ipaddr.IPNetwork(args.address)

    except ValueError:
        return parser.error('Invalid address: {0}'.format(args.address))
    
    print('Number of addresses:  {0}'.format(network.numhosts))
    print()
    print('Network:    {0}'.format(network.network.exploded))
    print('Broadcast:  {0}'.format(network.broadcast.exploded))
    print('Netmask:    {0}'.format(network.netmask.exploded))
    print()
    print('Network:    {0}'.format(address_to_bin(network.network)))
    print('Broadcast:  {0}'.format(address_to_bin(network.broadcast)))
    print('Netmask:    {0}'.format(address_to_bin(network.netmask)))
    print()


if __name__ == '__main__':
    main()
