import json


def json_formatter(data):
    """Return IP interface data as JSON

    :param data: IP interface data
    :return: IP interface data
    :rtype: str

    >>> import ipaddress
    >>> from six import u
    >>>
    >>> from uipcalc.utils import analise_interface
    >>>
    >>> ipv4_interface = ipaddress.ip_interface(u('192.0.2.254/24'))
    >>> data = analise_interface(ipv4_interface)
    >>> output = json_formatter(data)
    """

    return json.dumps(data)


def curses_formatter(data):
    pass
