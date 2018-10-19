#!/usr/bin/env python
"""
Field info
"""

import binascii
from slyr.parser.object import Object
from slyr.parser.stream import Stream


class FieldInfo(Object):
    """
    Field Info
    """

    def __init__(self):
        super().__init__()
        self.alias = ''
        self.number_format = None
        self.visible = True

    @staticmethod
    def guid():
        return 'a2baae2d-969b-11d2-ae77-080009ec732a'

    @staticmethod
    def compatible_versions():
        return [2, 4]

    def read(self, stream: Stream, version):
        assert binascii.hexlify(stream.read(4)) == b'ffff0000'
        self.alias = stream.read_string('alias')
        self.number_format = stream.read_object('format')
        if version >= 4:
            check = binascii.hexlify(stream.read(8))
            assert check == b'ffffffffffff0000', check
            self.visible = binascii.hexlify(stream.read(2)) == b'0000'

    def to_dict(self):
        return {
            'alias': self.alias,
            'number_format': self.number_format.to_dict() if self.number_format else None,
            'visible': self.visible
        }
