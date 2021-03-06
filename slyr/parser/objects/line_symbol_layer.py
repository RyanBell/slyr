#!/usr/bin/env python
"""
Line symbol layer subclasses
"""

import binascii
from slyr.parser.objects.symbol_layer import SymbolLayer
from slyr.parser.stream import Stream
from slyr.parser.exceptions import UnreadableSymbolException


class LineSymbolLayer(SymbolLayer):
    """
    Base class for line symbol layers
    """

    def __init__(self):
        super().__init__()
        self.color = None

    def children(self):
        res = super().children()
        if self.color:
            res.append(self.color)
        return res

    @staticmethod
    def read_cap(stream: Stream):
        """
        Reads a line cap style from the stream
        """
        cap_bin = stream.read_uchar()
        if cap_bin == 0:
            return 'butt'
        elif cap_bin == 1:
            return 'round'
        elif cap_bin == 2:
            return 'square'
        else:
            raise UnreadableSymbolException('unknown cap style {}'.format(cap_bin))

    @staticmethod
    def read_join(stream: Stream):
        """
        Reads a line join style from the stream
        """
        join_bin = stream.read_uchar()
        if join_bin == 0:
            return 'miter'
        elif join_bin == 1:
            return 'round'
        elif join_bin == 2:
            return 'bevel'
        else:
            raise UnreadableSymbolException('unknown join style {}'.format(join_bin))

    @staticmethod
    def read_line_type(stream: Stream):
        """
        Interprets the line type bytes
        """
        line_type = stream.read_uint()
        types = {0: 'solid',
                 1: 'dashed',
                 2: 'dotted',
                 3: 'dash dot',
                 4: 'dash dot dot',
                 5: 'null'}
        if line_type not in types:
            raise UnreadableSymbolException('unknown line type {} at {}'.format(line_type, hex(stream.tell() - 4)))
        return types[line_type]


class SimpleLineSymbolLayer(LineSymbolLayer):
    """
    Simple line symbol layer
    """

    def __init__(self):
        super().__init__()
        self.width = None
        self.line_type = None

    @staticmethod
    def guid():
        return '7914e5f9-c892-11d0-8bb6-080009ee4e41'

    def read(self, stream: Stream, version):
        self.color = stream.read_object('color')
        self.width = stream.read_double('width')

        self.line_type = self.read_line_type(stream)
        stream.log('read line type of {}'.format(self.line_type))
        stream.read_0d_terminator()


class CartographicLineSymbolLayer(LineSymbolLayer):
    """
    Cartographic line symbol layer
    """

    def __init__(self):
        super().__init__()
        self.width = None
        self.cap = None
        self.join = None
        self.offset = None
        self.template = None
        self.decoration = None

    @staticmethod
    def guid():
        return '7914e5fb-c892-11d0-8bb6-080009ee4e41'

    def children(self):
        res = super().children()
        if self.template:
            res.append(self.template)
        if self.decoration:
            res.append(self.decoration)
        return res

    def read(self, stream: Stream, version):
        self.cap = self.read_cap(stream)

        unknown = binascii.hexlify(stream.read(3))
        if unknown != b'000000':
            raise UnreadableSymbolException('Differing unknown string {}'.format(unknown))
        self.join = self.read_join(stream)
        unknown = binascii.hexlify(stream.read(3))
        if unknown != b'000000':
            raise UnreadableSymbolException('Differing unknown string {}'.format(unknown))

        self.width = stream.read_double('width')

        unknown = binascii.hexlify(stream.read(1))
        if unknown != b'00':
            raise UnreadableSymbolException('Differing unknown byte')

        self.offset = stream.read_double('offset')
        self.color = stream.read_object('color')
        self.template = stream.read_object('template')

        self.decoration = stream.read_object('decoration')
        stream.read_0d_terminator()

        _ = stream.read_uchar('unknown char')
        _ = stream.read_double()
        _ = stream.read_double()


class MarkerLineSymbolLayer(LineSymbolLayer):
    """
    Marker line symbol layer
    """

    def __init__(self):
        super().__init__()
        self.cap = None
        self.join = None
        self.offset = None
        self.template = None
        self.pattern_marker = None
        self.decoration = None

    @staticmethod
    def guid():
        return '7914e5fd-c892-11d0-8bb6-080009ee4e41'

    @staticmethod
    def compatible_versions():
        return [2]

    def children(self):
        res = super().children()
        if self.template:
            res.append(self.template)
        if self.decoration:
            res.append(self.decoration)
        if self.pattern_marker:
            res.append(self.pattern_marker)
        return res

    def read(self, stream: Stream, version):
        self.cap = self.read_cap(stream)
        stream.log('read cap of {}'.format(self.cap), 1)

        self.offset = stream.read_double('offset')
        self.pattern_marker = stream.read_object('pattern marker')
        self.template = stream.read_object('template')
        self.decoration = stream.read_object('decoration')

        stream.read_0d_terminator()

        _ = stream.read_double('unknown double')
        _ = stream.read_int('unknown int')
        _ = stream.read_uchar('unknown char')

        self.join = self.read_join(stream)
        unknown = binascii.hexlify(stream.read(3))
        if unknown != b'000000':
            raise UnreadableSymbolException('Differing unknown string {}'.format(unknown))

        _ = stream.read_double('unknown double')


class HashLineSymbolLayer(LineSymbolLayer):
    """
    Hash line symbol layer
    """

    def __init__(self):
        super().__init__()
        self.cap = None
        self.join = None
        self.offset = None
        self.template = None
        self.decoration = None
        self.line = None
        self.width = 0
        self.angle = 90

    @staticmethod
    def guid():
        return '7914e5fc-c892-11d0-8bb6-080009ee4e41'

    @staticmethod
    def compatible_versions():
        return [1]

    def children(self):
        res = super().children()
        if self.template:
            res.append(self.template)
        if self.decoration:
            res.append(self.decoration)
        if self.line:
            res.append(self.line)
        return res

    def read(self, stream: Stream, version):
        self.angle = stream.read_double('angle')
        self.cap = self.read_cap(stream)
        unknown = binascii.hexlify(stream.read(3))
        if unknown != b'000000':
            raise UnreadableSymbolException('Differing unknown string {}'.format(unknown))
        self.join = self.read_join(stream)
        unknown = binascii.hexlify(stream.read(3))
        if unknown != b'000000':
            raise UnreadableSymbolException('Differing unknown string {}'.format(unknown))
        self.width = stream.read_double('width')
        stream.read(1)
        self.offset = stream.read_double('offset')

        self.line = stream.read_object('line')

        self.color = stream.read_object('color')
        self.template = stream.read_object('template')

        self.decoration = stream.read_object('decoration')
        stream.read_0d_terminator()

        _ = stream.read_uchar('unknown char')
        _ = stream.read_double('unknown')
        _ = stream.read_double('unknown')
