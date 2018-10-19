#!/usr/bin/env python
"""
Simple Renderer
"""

import binascii
from slyr.parser.object import Object
from slyr.parser.stream import Stream


class SimpleRenderer(Object):
    """
    Simple Renderer
    """

    def __init__(self):
        super().__init__()
        self.symbol = None

    @staticmethod
    def guid():
        return 'f3435801-5779-11d0-98bf-00805f7ced21'

    @staticmethod
    def compatible_versions():
        return [3]

    def read(self, stream: Stream, version):
        self.symbol = stream.read_object('symbol')

    def to_dict(self):
        return {
            'symbol': self.symbol.to_dict() if self.symbol else None
        }
