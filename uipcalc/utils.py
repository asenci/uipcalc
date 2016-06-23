# noinspection PyCompatibility
import ipaddress


def address_to_bin(address):
    """Return the binary representation of an IP address as a bit list

    :param address: IPv4Address or IPv6Address object
    :return: binary representation of the IP address
    :rtype: list

    >>> from pprint import pprint
    >>> ipv4_addr = ipaddress.ip_address('192.0.2.254')
    >>> pprint(address_to_bin(ipv4_addr), width=72, compact=True)
    ['1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
     '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '1',
     '1', '1', '1', '0']
    >>> ipv6_addr = ipaddress.ip_address('2001:DB8::F')
    >>> pprint(address_to_bin(ipv6_addr), width=72, compact=True)
    ['0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
     '0', '1', '0', '0', '0', '0', '1', '1', '0', '1', '1', '0', '1', '1',
     '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
     '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
     '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
     '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
     '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
     '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
     '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1',
     '1', '1']
    """

    # binary representation of the address as integer ('0b01010101...')
    bin_addr_str = bin(int(address))

    # remove the '0b' prefix from the string
    bin_addr = bin_addr_str[2:]

    # fill in the address length (eg: 32 bits for IPv4 addresses)
    bits = bin_addr.zfill(address.max_prefixlen)

    return list(bits)


def analise_interface(interface):
    """Return information about the IP interface as a dict

    :param interface: IPv4Interface or IPv6Interface object
    :return: information about the IP interface
    :rtype: dict

    >>> from pprint import pprint
    >>> ipv4_interface = ipaddress.ip_interface('192.0.2.254/24')
    >>> pprint(analise_interface(ipv4_interface), width=72, compact=True)
    {'interface_address': '192.0.2.254',
     'interface_address_bin': ['1', '1', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '1', '0', '1', '1', '1',
                               '1', '1', '1', '1', '0'],
     'network_address': '192.0.2.0',
     'network_address_bin': ['1', '1', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '1', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0'],
     'network_broadcast': '192.0.2.255',
     'network_broadcast_bin': ['1', '1', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '1', '0', '1', '1', '1',
                               '1', '1', '1', '1', '1'],
     'network_netmask': '255.255.255.0',
     'network_netmask_bin': ['1', '1', '1', '1', '1', '1', '1', '1', '1',
                             '1', '1', '1', '1', '1', '1', '1', '1', '1',
                             '1', '1', '1', '1', '1', '1', '0', '0', '0',
                             '0', '0', '0', '0', '0'],
     'network_numadresses': 256,
     'network_prefixlen': 24}
    >>> ipv6_interface = ipaddress.ip_interface('2001:DB8::F/64')
    >>> pprint(analise_interface(ipv6_interface), width=72, compact=True)
    {'interface_address': '2001:0db8:0000:0000:0000:0000:0000:000f',
     'interface_address_bin': ['0', '0', '1', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '1', '0', '0',
                               '0', '0', '1', '1', '0', '1', '1', '0', '1',
                               '1', '1', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '1', '1',
                               '1', '1'],
     'network_address': '2001:0db8:0000:0000:0000:0000:0000:0000',
     'network_address_bin': ['0', '0', '1', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '1', '0', '0',
                             '0', '0', '1', '1', '0', '1', '1', '0', '1',
                             '1', '1', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0'],
     'network_broadcast': '2001:0db8:0000:0000:ffff:ffff:ffff:ffff',
     'network_broadcast_bin': ['0', '0', '1', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '1', '0', '0',
                               '0', '0', '1', '1', '0', '1', '1', '0', '1',
                               '1', '1', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '0', '0', '0', '0', '0', '0', '0', '0',
                               '0', '1', '1', '1', '1', '1', '1', '1', '1',
                               '1', '1', '1', '1', '1', '1', '1', '1', '1',
                               '1', '1', '1', '1', '1', '1', '1', '1', '1',
                               '1', '1', '1', '1', '1', '1', '1', '1', '1',
                               '1', '1', '1', '1', '1', '1', '1', '1', '1',
                               '1', '1', '1', '1', '1', '1', '1', '1', '1',
                               '1', '1', '1', '1', '1', '1', '1', '1', '1',
                               '1', '1'],
     'network_netmask': 'ffff:ffff:ffff:ffff:0000:0000:0000:0000',
     'network_netmask_bin': ['1', '1', '1', '1', '1', '1', '1', '1', '1',
                             '1', '1', '1', '1', '1', '1', '1', '1', '1',
                             '1', '1', '1', '1', '1', '1', '1', '1', '1',
                             '1', '1', '1', '1', '1', '1', '1', '1', '1',
                             '1', '1', '1', '1', '1', '1', '1', '1', '1',
                             '1', '1', '1', '1', '1', '1', '1', '1', '1',
                             '1', '1', '1', '1', '1', '1', '1', '1', '1',
                             '1', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0', '0', '0', '0', '0', '0', '0', '0',
                             '0', '0'],
     'network_numadresses': 18446744073709551616,
     'network_prefixlen': 64}
    """

    net = interface.network
    data = {
        'interface_address': interface.ip.exploded,
        'interface_address_bin': address_to_bin(interface.ip),
        'network_address': net.network_address.exploded,
        'network_address_bin': address_to_bin(net.network_address),
        'network_broadcast': net.broadcast_address.exploded,
        'network_broadcast_bin': address_to_bin(net.broadcast_address),
        'network_netmask': net.netmask.exploded,
        'network_netmask_bin': address_to_bin(net.netmask),
        'network_numadresses': net.num_addresses,
        'network_prefixlen': net.prefixlen,
    }

    return data
