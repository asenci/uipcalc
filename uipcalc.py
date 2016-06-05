"""
uipcalc - Universal (IPv4/IPv6) IP address and netmask calculator

Copyright (c) 2011 Andre Sencioles Vitorio Oliveira <asenci@gmail.com>

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
import argparse
import ipaddress
import six
import sys


def address_to_bin(address, split=None):
    """Converts an dotted-decimal (IPv4) or groups of hexadecimals (IPv6)
    formatted address to a binary representation

    :param address: The IP address
    :type address: ipaddress.IPv4Address or ipaddress.IPv6Address or str
    :param int split: Position to split the address
    :return: A binary representation of the IP address
    :rtype: str
    """

    if isinstance(address, six.string_types):
        address = ipaddress.ip_address(address)

    if address.version == 4:
        bits_total = 32
        bits_step = 8
        bits_sep = '.'
    else:
        bits_total = 128
        bits_step = 16
        bits_sep = ':'

    bits_array = bin(int(address))[2:]
    bits_array = bits_array.zfill(bits_total)
    bits_array = [bits_array[p:p + bits_step] for p in
                  range(0, bits_total, bits_step)]
    bits_array = bits_sep.join(bits_array)

    if split:
        split += split // bits_step
        bits_array = bits_array[:split] + ' ' + bits_array[split:]

    return bits_array


# noinspection PyDocstring
def main(argv=None):

    parser = argparse.ArgumentParser(
        description='Universal (IPv4/IPv6) IP address and netmask calculator')
    parser.add_argument(
        'address', help='IP address with netmask in CIDR or dotted-decimal notation')
    args = parser.parse_args(args=argv)

    try:
        interface = ipaddress.ip_interface(args.address)

    except ValueError as e:
        return parser.error(str(e))

    net = interface.network
    
    print('Number of addresses:  {0}'.format(net.num_addresses))
    print()
    print('Network:    {0}'.format(net.network_address.exploded))
    print('Broadcast:  {0}'.format(net.broadcast_address.exploded))
    print('Netmask:    {0} ({1})'.format(net.netmask.exploded, net.prefixlen))
    print()
    print('Network:    {0}'.format(address_to_bin(net.network_address, net.prefixlen)))
    print('Broadcast:  {0}'.format(address_to_bin(net.broadcast_address, net.prefixlen)))
    print('Netmask:    {0}'.format(address_to_bin(net.netmask, net.prefixlen)))
    print()


if __name__ == '__main__':
    sys.exit(main())
