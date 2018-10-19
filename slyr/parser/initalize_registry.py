#!/usr/bin/env python
"""
Registers all known objects with the registry singleton
"""

from slyr.parser.object_registry import REGISTRY

from slyr.parser.objects.line_template import LineTemplate
from slyr.parser.objects.colors import (
    CMYKColor,
    RgbColor,
    HSVColor,
    HSLColor,
    GrayColor
)
from slyr.parser.objects.decoration import (
    LineDecoration,
    SimpleLineDecoration)
from slyr.parser.objects.line_symbol_layer import (
    SimpleLineSymbolLayer,
    CartographicLineSymbolLayer,
    MarkerLineSymbolLayer,
    HashLineSymbolLayer
)
from slyr.parser.objects.fill_symbol_layer import (
    SimpleFillSymbolLayer,
    ColorSymbol,
    GradientFillSymbolLayer,
    LineFillSymbolLayer,
    MarkerFillSymbolLayer,
    PictureFillSymbolLayer
)
from slyr.parser.objects.marker_symbol_layer import (
    ArrowMarkerSymbolLayer,
    CharacterMarkerSymbolLayer,
    SimpleMarkerSymbolLayer,
    PictureMarkerSymbolLayer
)
from slyr.parser.objects.font import Font
from slyr.parser.symbol_parser import (
    FillSymbol,
    LineSymbol,
    MarkerSymbol
)
from slyr.parser.objects.ramps import (
    RandomColorRamp,
    PresetColorRamp,
    MultiPartColorRamp,
    AlgorithmicColorRamp
)
from slyr.parser.objects.picture import StdPicture
from slyr.parser.objects.property_set import PropertySet
from slyr.parser.objects.workspace_name import WorkspaceName
from slyr.parser.objects.feature_class_name import FeatureClassName
from slyr.parser.objects.numeric_format import NumericFormat
from slyr.parser.objects.field_info import FieldInfo
from slyr.parser.objects.simple_renderer import SimpleRenderer


def initialize_registry():
    """
    Registers all known objects with the registry singleton
    """

    REGISTRY.register(LineTemplate)
    REGISTRY.register(CMYKColor)
    REGISTRY.register(RgbColor)
    REGISTRY.register(HSVColor)
    REGISTRY.register(HSLColor)
    REGISTRY.register(GrayColor)
    REGISTRY.register(LineDecoration)
    REGISTRY.register(SimpleLineDecoration)
    REGISTRY.register(SimpleLineSymbolLayer)
    REGISTRY.register(CartographicLineSymbolLayer)
    REGISTRY.register(MarkerLineSymbolLayer)
    REGISTRY.register(SimpleFillSymbolLayer)
    REGISTRY.register(ColorSymbol)
    REGISTRY.register(ArrowMarkerSymbolLayer)
    REGISTRY.register(CharacterMarkerSymbolLayer)
    REGISTRY.register(SimpleMarkerSymbolLayer)
    REGISTRY.register(Font)
    REGISTRY.register(FillSymbol)
    REGISTRY.register(LineSymbol)
    REGISTRY.register(MarkerSymbol)
    REGISTRY.register(RandomColorRamp)
    REGISTRY.register(PresetColorRamp)
    REGISTRY.register(MultiPartColorRamp)
    REGISTRY.register(AlgorithmicColorRamp)
    REGISTRY.register(GradientFillSymbolLayer)
    REGISTRY.register(LineFillSymbolLayer)
    REGISTRY.register(MarkerFillSymbolLayer)
    REGISTRY.register(HashLineSymbolLayer)
    REGISTRY.register(PictureMarkerSymbolLayer)
    REGISTRY.register(PictureFillSymbolLayer)
    REGISTRY.register(StdPicture)
    REGISTRY.register(NumericFormat)
    REGISTRY.register(FieldInfo)
    REGISTRY.register(PropertySet)
    REGISTRY.register(WorkspaceName)
    REGISTRY.register(FeatureClassName)
    REGISTRY.register(SimpleRenderer)
