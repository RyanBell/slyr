#!/usr/bin/env python
"""
std OLE Font
"""

from slyr.parser.object import Object
from slyr.parser.stream import Stream


class FeatureClassName(Object):
    """
    Feature class name
    """

    # feature types
    FT_SIMPLE = 1
    FT_SIMPLE_JUNCTION = 7
    FT_SIMPLE_EDGE = 8
    FT_COMPLEX_JUNCTION = 9
    FT_COMPLEX_EDGE = 10
    FT_ANNOTATION = 11
    FT_COVERAGE_ANNOTATION = 12
    FT_DIMENSION = 13
    FT_RASTER_CATALOG_ITEM = 14

    # geometry types
    GEOMETRY_NULL = 0
    GEOMETRY_POINT = 1
    GEOMETRY_MULTIPOINT = 2
    GEOMETRY_LINE = 13
    GEOMETRY_CIRCULAR_ARC = 14
    GEOMETRY_ELLIPTIC_ARC = 16
    GEOMETRY_BEZIER_CURVE = 15
    GEOMETRY_PATH = 6
    GEOMETRY_POLYLINE = 3
    GEOMETRY_RING = 11
    GEOMETRY_POLYGON = 4
    GEOMETRY_ENVELOPE = 5
    GEOMETRY_ANY = 7
    GEOMETRY_BAG = 17
    GEOMETRY_MULTIPATCH = 9
    GEOMETRY_TRIANGLE_STRIP = 18
    GEOMETRY_TRIANGLE_FAN = 19
    GEOMETRY_RAY = 20
    GEOMETRY_SPHERE = 21
    GEOMETRY_TRIANGLES = 22

    def __init__(self):
        super().__init__()
        self.dataset_name = ''
        self.feature_type = self.FT_SIMPLE
        self.shape_field_name = ''
        self.shape_type = self.GEOMETRY_NULL

    @staticmethod
    def guid():
        return '198846d0-ca42-11d1-aa7c-00c04fa33a15'

    @staticmethod
    def compatible_versions():
        return [2]

    def read(self, stream: Stream, version):
        self.dataset_name = stream.read_string('name')
        _ = stream.read_string('unknown')
        self.shape_field_name = stream.read_string('name')
        self.shape_field_name = stream.read_string('name')
        self.shape_type = stream.read_uint('type')
        self.feature_type = stream.read_uint('type')
