#!/usr/bin/env python
"""
A registry for all known objects which can be decoded from a Stream
"""

from slyr.parser.object import Object
from slyr.parser.exceptions import (NotImplementedException,
                                    UnknownGuidException)


class ObjectRegistry:
    """
    A registry for all known objects which can be decoded from a Stream.
    """

    NOT_IMPLEMENTED_GUIDS = {
        # Picture layers
        '22c8c5a1-84fc-11d4-834d-0080c79f0371': 'PictureLineSymbol',

        # Uncommon stuff
        '9a1eba10-cdf9-11d3-81eb-0080c79f0371': 'DotDensityFillSymbol',
        'b65a3e74-2993-11d1-9a43-0080c7ec5c96': 'TextSymbol',
        '40987040-204c-11d3-a3f2-0004ac1b1d86': 'ColorRampSymbol',
        '99dccb66-2e09-11d3-a626-0008c7bf3347': 'RasterRGBSymbol',
        '2b74125d-5c1b-4dbd-967a-7412dfff1f09': 'TextMarkerSymbol',

        # 3D symbols
        '6e8ec8f7-e90a-11d5-a129-00508bd60cb9': 'CharacterMarker3DSymbol',
        '773f7274-aefb-11d5-8112-00c04fa0adf8': 'Marker3DSymbol',
        '470b7275-3552-11d6-a12d-00508bd60cb9': 'SimpleLine3DSymbol',
        '773f7270-aefb-11d5-8112-00c04fa0adf8': 'SimpleMarker3DSymbol',
        '8d738780-c069-42e0-9dfa-2b7b61707ba9': 'TextureFillSymbol',
        'b5710c9c-a9bc-4a16-b578-54be176ed57b': 'TextureLineSymbol',

        # Chart symbols
        '5031736a-bd70-11d3-9f79-00c04f6bc709': 'BarChartSymbol',
        '50317368-bd70-11d3-9f79-00c04f6bc709': 'PieChartSymbol',
        '50317369-bd70-11d3-9f79-00c04f6bc709': 'StackedChartSymbol',

        '52353152-891a-11d0-bec6-00805f7c4268': 'CLASS_FEATURECLASS',
        '7a566981-c114-11d2-8a28-006097aff44e': 'CLASS_TABLE',
        'e3676993-c682-11d2-8a2a-006097aff44e': 'CLASS_ANNOTATION',
        '24429589-d711-11d2-9f41-00c04f6bc6a5': 'CLASS_ANNOTATION_EXTENSION',
        '496764fc-e0c9-11d3-80ce-00c04f601565': 'CLASS_DIMENSION',
        '48f935e2-da66-11d3-80ce-00c04f601565': 'CLASS_DIMENSION_EXTENSION',
        'cee8d6b8-55fe-11d1-ae55-0000f80372b4': 'CLASS_SIMPLEJUNCTION',
        'e7031c90-55fe-11d1-ae55-0000f80372b4': 'CLASS_SIMPLEEDGE',
        'a30e8a2a-c50b-11d1-aea9-0000f80372b4': 'CLASS_COMPLEXEDGE',
        '3eaa2478-5332-40f8-8fa8-62382390a3ba': 'CLASS_RASTERCATALOG',
        'a07e9cb1-9a95-11d2-891a-0000f877762d': 'CLASS_ATTRIBUTED_RELATIONSHIP',

        'ae5f7ea2-8b48-11d0-8356-080009b996cc': 'ClassBreaksRenderer',
        '207c19f5-ed81-11d0-8bba-080009ee4e41': 'ScaleDependentRenderer',
        'c3346d29-b2bc-11d1-8817-080009ec732a': 'UniqueValueRenderer',
        '4eab568e-8f9c-11d2-ab21-00c04fa334b3': 'ProportionalSymbolRenderer',
        'b899ccd3-cd1c-11d2-9f25-00c04f6bc709': 'BiUniqueValueRenderer',
        '4f17939a-c490-11d3-9f7a-00c04f6bc709': 'ChartRenderer',
        '4b62f73d-0502-11d4-9f7c-00c04f6bc709': 'CalcRendererValues',
        '9c7776ba-0421-11d4-9f7c-00c04f6bc709': 'DotDensityRenderer',
        'a9401a47-4649-11d1-880b-080009ec732a': 'HorizontalLegendItem',
        'a9401a48-4649-11d1-880b-080009ec732a': 'VerticalLegendItem',
        '2b65d211-c2c7-11d3-92f3-00600802e603': 'HorizontalBarLegendItem',
        '2b65d212-c2c7-11d3-92f3-00600802e603': 'NestedLegendItem',
        '167c5ea3-af20-11d1-8817-080009ec732a': 'LegendClass',
        '7a3f91e6-b9e3-11d1-8756-0000f8751720': 'LegendClassFormat',
        '167c5ea2-af20-11d1-8817-080009ec732a': 'LegendGroup',
        '2066267e-e3b8-11d2-b868-00600802e603': 'AreaPatch',
        '2066267f-e3b8-11d2-b868-00600802e603': 'LinePatch',
        'e663a651-8aad-11d0-bec7-00805f7c4268': 'FeatureLayer',
        '198846cf-ca42-11d1-aa7c-00c04fa33a15': 'FeatureDatasetName',
        'a06adb96-d95c-11d1-aa81-00c04fa33a15': 'ShapefileWorkspaceFactory',
        'd9b4fa40-d6d9-11d1-aa81-00c04fa33a15': 'SdeWorkspaceFactory',
        '4eab5691-8f9c-11d2-ab21-00c04fa334b3': 'SingleSymbolPropertyPage',
        '1d5849f3-0d33-11d2-a26f-080009b6f22b': 'AnnotateLayerPropertiesCollection'
    }

    def __init__(self):
        self.objects = {}

    def register(self, object_class: Object):
        """
        Registers a new object class to the registry.
        """
        self.objects[object_class.guid()] = object_class

    def create_object(self, guid: str):
        """
        Creates a new object of the type associated with guid
        """
        if guid == '00000000-0000-0000-0000-000000000000':
            return None
        if guid in self.NOT_IMPLEMENTED_GUIDS:
            raise NotImplementedException('{} objects are not yet supported'.format(self.NOT_IMPLEMENTED_GUIDS[guid]))
        elif guid not in self.objects:
            raise UnknownGuidException('Unknown GUID: {}'.format(guid))
        return self.objects[guid]()

    @staticmethod
    def guid_to_hex(guid: str):
        """
        Converts a string GUID to the binary equivalent stored in a block
        E.g.
        '7914e603-c892-11d0-8bb6-080009ee4e41' to
        03e6147992c8d0118bb6080009ee4e41
        """

        # Note: this is correct - confirmed by checking against WINE source
        # https://github.com/wine-mirror/wine/blob/6d801377055911d914226a3c6af8d8637a63fa13/dlls/compobj.dll16/compobj.c#L380

        g = guid.replace('-', '')
        res = b''
        res += g[6:8].encode()
        res += g[4:6].encode()
        res += g[2:4].encode()
        res += g[0:2].encode()
        res += g[10:12].encode()
        res += g[8:10].encode()
        res += g[14:16].encode()
        res += g[12:14].encode()
        res += g[16:].encode()
        return res

    @staticmethod
    def hex_to_guid(hex_value) -> str:
        """
        Converts a binary value to a GUID
        eg 03e6147992c8d0118bb6080009ee4e41
        to 7914e603-c892-11d0-8bb6-080009ee4e41
        """
        res = ''
        res += hex_value[6:8].decode()
        res += hex_value[4:6].decode()
        res += hex_value[2:4].decode()
        res += hex_value[0:2].decode()
        res += '-'
        res += hex_value[10:12].decode()
        res += hex_value[8:10].decode()
        res += '-'
        res += hex_value[14:16].decode()
        res += hex_value[12:14].decode()
        res += '-'
        res += hex_value[16:20].decode()
        res += '-'
        res += hex_value[20:].decode()
        return res


REGISTRY = ObjectRegistry()
