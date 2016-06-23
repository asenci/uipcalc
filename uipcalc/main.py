import argparse
# noinspection PyCompatibility
import ipaddress

from uipcalc import __description__
from uipcalc.utils import analise_interface


# noinspection PyDocstring
def run(args=None):

    arg_parser = argparse.ArgumentParser(description=__description__)

    arg_parser.add_argument(
        'address',
        help='IP address with netmask in CIDR or dotted-decimal notation')

    args = arg_parser.parse_args(args=args)

    try:
        interface = ipaddress.ip_interface(args.address)

    except ValueError as e:
        return arg_parser.error(str(e))

    data = analise_interface(interface)

    print('Number of addresses:  {0}'.format(data['network_numadresses']))
    print()
    print('Network:    {0}'.format(data['network_address']))
    print('Broadcast:  {0}'.format(data['network_broadcast']))
    print('Netmask:    {0}'.format(data['network_netmask']))
    print()
    print('Network:    {0}'.format(''.join(data['network_address_bin'])))
    print('Broadcast:  {0}'.format(''.join(data['network_broadcast_bin'])))
    print('Netmask:    {0}'.format(''.join(data['network_netmask_bin'])))
    print()
