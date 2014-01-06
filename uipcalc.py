#!/usr/bin/env python2.7
# encoding: utf-8
'''
pccalc.py

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
'''
import ipaddr

def bit_count(netmask):
    '''Counts the number of bits set on a doted-quad formated mask
    
    Returns the number of bits set on the netmask
    '''
    import re
    
    try:
        ipaddr.IPv4Address(netmask)
    except ipaddr.AddressValueError:
        return -1
    
    bits = 0
    for num in netmask.split('.'):
        binseq = bin(int(num))
        if re.match(r'^0b1*0*$', binseq):
            bits = bits + binseq.count('1')
        else:
            return -1

    return bits

def to_bin(address):
    '''Converts the address to binary format
    
    '''
    binaddr=[]
    
    if '.' in address:
        for num in address.split('.'):
            binaddr.append(bin(int(num))[2:].zfill(8))
    elif ':' in address:
        for num in address.split(':'):
            binaddr.append(bin(int(num, 16))[2:].zfill(16))

    return '.'.join(binaddr)

def parse_args():
    '''Parses the received arguments
    
    Returns a list with the parser object and the arguments dictonary.
    
    '''
    import argparse
    
    parser = argparse.ArgumentParser(description='Universal IP Calculator')
    parser.add_argument('ipaddr', metavar='IPADDR',
                        help='IP address with netmask in CIDR notation')
    parser.add_argument('netmask', metavar='NETMASK', nargs='?',
                        help='Netmask in doted decimal notation')
    
    return [parser, vars(parser.parse_args())]

def main():
    parser, args = parse_args()
    
    if args['netmask']:
        if '/' in args['ipaddr']:
            parser.error('enter the netmask either in CIDR or doted-quad '
                         'notation.')
        else:
            try:
                ipaddr.IPv4Address(args['ipaddr'])
            except ipaddr.AddressValueError:
                parser.error('Invalid IP address: {ipaddr}'.format(args))

            args['bits'] = bit_count(args['netmask'])
            if args['bits'] < 0:
                parser.error('Invalid netmask: {netmask}'.format(args))
            else:
                address = '{ipaddr}/{0}'.format(args['bits'], **args)
    else:
        address = args['ipaddr']
    
    try:
        network = ipaddr.IPNetwork(address)
    except:
        parser.error('Invalid address: {}'.format(address))
    
    print ('Number of addresses:  {0}\n'
           '\n'
           'First address:  {1}\n'
           'Last address:   {2}\n'
           'Netmask:        {3}\n'
           '\n'
           'Net:   {4}\n'
           'Mask:  {5}\n'
           'Last:  {6}\n').format(network.numhosts,
                                  network.network.exploded,
                                  network.broadcast.exploded,
                                  network.netmask.exploded,
                                  to_bin(network.network.exploded),
                                  to_bin(network.netmask.exploded),
                                  to_bin(network.broadcast.exploded))

if __name__ == '__main__':
    main()