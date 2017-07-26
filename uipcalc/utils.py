import ipaddress


def address_to_bin(address):
    """Return the binary representation of an IP address as a bit list

    :param address: IPv4Address or IPv6Address object
    :return: binary representation of the IP address
    :rtype: list

    >>> from six import u
    >>>
    >>> ipv4_addr = ipaddress.ip_address(u('192.0.2.254'))
    >>> ipv6_addr = ipaddress.ip_address(u('2001:DB8::F'))
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

    >>> from six import u
    >>>
    >>> ipv4_interface = ipaddress.ip_interface(u('192.0.2.254/24'))
    >>> ipv6_interface = ipaddress.ip_interface(u('2001:DB8::F/64'))
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
