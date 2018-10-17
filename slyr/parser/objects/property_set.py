#!/usr/bin/env python
"""
std OLE Font
"""

from slyr.parser.object import Object
from slyr.parser.stream import Stream
from slyr.parser.exceptions import UnreadableSymbolException


class PropertySet(Object):
    """
    A set of properties (dict)
    """

    VBEMPTY = 0
    VBNULL = 1
    VBINTEGER = 2
    VBLONG = 3
    VBSINGLE = 4
    VBDOUBLE = 5
    VBCURRENCY = 6
    VBDATE = 7
    VBSTRING = 8
    VBOBJECT = 9
    VBERROR = 10
    VBBOOLEAN = 11
    VBVARIANT = 12
    VBDATAOBJECT = 13
    VBDECIMAL = 14
    VBBYTE = 17
    VBLONGLONG = 20
    VBUSERDEFINEDTYPE = 36
    VBARRAY = 8192
    USER_PASSWORD = 8209

    def __init__(self):
        super().__init__()
        self.properties = {}

    @staticmethod
    def guid():
        return '588e5a11-d09b-11d1-aa7c-00c04fa33a15'

    @staticmethod
    def compatible_versions():
        return [1]

    def read(self, stream: Stream, version):
        length = stream.read_uint('length')
        for _ in range(length):
            key = stream.read_string('key')
            property_type = stream.read_ushort('type')
            if property_type == self.VBSTRING:
                value = stream.read_string('value')
            elif property_type == self.VBLONG:
                value = stream.read_ulong('value')
            elif property_type == self.VBINTEGER:
                value = stream.read_int('value')
            elif property_type in (self.VBNULL, self.VBEMPTY):
                value = None
            elif property_type == self.VBDOUBLE:
                value = stream.read_double('value')
            elif property_type == self.USER_PASSWORD:
                length = stream.read_uint('password length')
                value = '*' * length
                stream.read(length)
            else:
                raise UnreadableSymbolException('Unknown property type {}'.format(property_type))
            self.properties[key] = value

    def to_dict(self):
        return self.properties
