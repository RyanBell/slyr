#!/usr/bin/env python
"""
Numeric Format
"""
import binascii
from slyr.parser.object import Object
from slyr.parser.stream import Stream


class NumericFormat(Object):
    """
    Numeric format
    """

    ALIGN_RIGHT = 0
    ALIGN_LEFT = 1

    ROUND_NUMBER_OF_DECIMALS = 0
    ROUND_NUMBER_OF_SIGNIFICANT_DIGITS = 1

    def __init__(self):
        super().__init__()
        self.alignment = self.ALIGN_RIGHT
        self.alignment_width = 12
        self.rounding = self.ROUND_NUMBER_OF_DECIMALS
        self.rounding_value = 6
        self.show_plus_sign = False
        self.use_separator = False
        self.zero_pad = False

    @staticmethod
    def guid():
        return '7e4f4719-8e54-11d2-aad8-000000000000'

    @staticmethod
    def compatible_versions():
        return [1]

    def read(self, stream: Stream, version):
        assert binascii.hexlify(stream.read(12)) == b'000000000000000000000000'
        self.alignment_width = stream.read_ulong('alignment width')
        check = binascii.hexlify(stream.read(6))
        assert check == b'000000000000', check

    def to_dict(self):
        return {
            'alignment': self.alignment,
            'alignment_width': self.alignment_width,
            'rounding': self.rounding,
            'rounding_value': self.rounding_value,
            'show_plus_sign': self.show_plus_sign,
            'use_separator': self.use_separator,
            'zero_pad': self.zero_pad
        }
