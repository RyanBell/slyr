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

    NOT_IMPLEMENTED_GUIDS = {'9a1eba10-cdf9-11d3-81eb-0080c79f0371': 'DotDensityFillSymbol',
                             'b65a3e74-2993-11d1-9a43-0080c7ec5c96': 'TextSymbol',
                             '2b74125d-5c1b-4dbd-967a-7412dfff1f09': 'TextMarkerSymbol',
                             '6e8ec8f7-e90a-11d5-a129-00508bd60cb9': 'CharacterMarker3DSymbol',
                             '773f7274-aefb-11d5-8112-00c04fa0adf8': 'Marker3DSymbol',
                             '470b7275-3552-11d6-a12d-00508bd60cb9': 'SimpleLine3DSymbol',
                             '773f7270-aefb-11d5-8112-00c04fa0adf8': 'SimpleMarker3DSymbol',
                             '8d738780-c069-42e0-9dfa-2b7b61707ba9': 'TextureFillSymbol',
                             'b5710c9c-a9bc-4a16-b578-54be176ed57b': 'TextureLineSymbol',
                             '5031736a-bd70-11d3-9f79-00c04f6bc709': 'BarChartSymbol',
                             '50317368-bd70-11d3-9f79-00c04f6bc709': 'PieChartSymbol',
                             '50317369-bd70-11d3-9f79-00c04f6bc709': 'StackedChartSymbol',
                             'ae5f7ea2-8b48-11d0-8356-080009b996cc': 'ClassBreaksRenderer',
                             '207c19f5-ed81-11d0-8bba-080009ee4e41': 'ScaleDependentRenderer',
                             'c3346d29-b2bc-11d1-8817-080009ec732a': 'UniqueValueRenderer',
                             '4eab568e-8f9c-11d2-ab21-00c04fa334b3': 'ProportionalSymbolRenderer',
                             'b899ccd3-cd1c-11d2-9f25-00c04f6bc709': 'BiUniqueValueRenderer',
                             '4f17939a-c490-11d3-9f7a-00c04f6bc709': 'ChartRenderer',
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
                             '1d5849f3-0d33-11d2-a26f-080009b6f22b': 'AnnotateLayerPropertiesCollection',
                             '78ff7fa1-fb2f-11d1-94a2-080009eebecb': 'UID',
                             '53da75df-d01a-11d2-9f27-00c04f6bc69e': 'FileName',
                             'de162780-1dd1-11b2-bf4f-08002022f573': 'LinearUnit',
                             '74ad43f4-d31c-11d1-bc9b-0000f875bcce': 'AngularUnit',
                             '2b929480-1dd2-11b2-bf4f-08002022f573': 'Spheroid',
                             '862bf080-1dd2-11b2-bf4f-08002022f573': 'Datum',
                             'c55a4180-1dd1-11b2-bf50-08002022f573': 'PrimeMeridian',
                             'a6a87a80-1dd1-11b2-bf51-08002022f573': 'GeographicCoordinateSystem',
                             'e2dbdb00-1dd1-11b2-bf51-08002022f573': 'Parameter',
                             '2a626700-1dd2-11b2-bf51-08002022f573': 'ProjectedCoordinateSystem',
                             '7ca36480-c8f4-11d1-bc93-0000f875bcce': 'Projection',
                             '0f024430-c1f8-11d2-bd07-0000f875bcce': 'GeocentricTranslation',
                             '0f024431-c1f8-11d2-bd07-0000f875bcce': 'CoordinateFrameTransformation',
                             '0cdf92b1-c2a0-11d2-bd08-0000f875bcce': 'PositionVectorTransformation',
                             '0cdf92b0-c2a0-11d2-bd08-0000f875bcce': 'MolodenskyTransformation',
                             'dd2f68d0-c6b0-11d2-bd09-0000f875bcce': 'AbridgedMolodenskyTransformation',
                             '6f3c0002-da7f-11d3-9f60-00c04f6bdd7f': 'LongitudeRotationTransformation',
                             'd661941c-da8a-11d3-9f60-00c04f6bdd7f': 'NADCONTransformation',
                             'df146878-da8a-11d3-9f60-00c04f6bdd7f': 'HARNTransformation',
                             '5847fb82-dbae-11d3-9f60-00c04f6bdd7f': 'CompositeGeoTransformation',
                             'b286c06b-0879-11d2-aaca-00c04fa33c20': 'UnknownCoordinateSystem',
                             '00a5cb41-52da-11d0-a8f2-00608c85ede5': 'Point',
                             '30707212-52d5-11d0-a8f2-00608c85ede5': 'Envelope',
                             '00a5cb40-52da-11d0-a8f2-00608c85ede5': 'Multipoint',
                             '30707210-52d5-11d0-a8f2-00608c85ede5': 'Polyline',
                             '00a5cb42-52da-11d0-a8f2-00608c85ede5': 'Polygon',
                             '10b5f5c0-3781-11d2-bcc5-0000f875bcce': 'GeometryBag',
                             'f3c041c6-ae4d-11d2-9c93-00c04fb17838': 'MultiPatch',
                             '7e4f471a-8e54-11d2-aad8-000000000000': 'CurrencyFormat',
                             '7e4f471b-8e54-11d2-aad8-000000000000': 'PercentageFormat',
                             '7e4f471c-8e54-11d2-aad8-000000000000': 'FractionFormat',
                             '7e4f471d-8e54-11d2-aad8-000000000000': 'LatLonFormat',
                             '7e4f471e-8e54-11d2-aad8-000000000000': 'AngleFormat',
                             '7e4f471f-8e54-11d2-aad8-000000000000': 'ScientificFormat',
                             '7e4f4721-8e54-11d2-aad8-000000000000': 'RateFormat',
                             '7e4f4722-8e54-11d2-aad8-000000000000': 'CustomNumberFormat',
                             'ac0e9829-91cb-11d1-8813-080009ec732a': 'StyleGalleryItem',
                             'ac0e9827-91cb-11d1-8813-080009ec732a': 'StyleGallery',
                             'ce259b71-280c-11d2-aa2f-000000000000': 'AcceleratorTable',
                             'fa73ef95-b87c-11d1-947b-080009eebecb': 'CommandItem',
                             'ad754a65-13b4-11d3-b89d-00600802e603': 'TransparencyDisplayFilter',
                             '1c352f40-298e-11d3-9f4f-00c04f6bc619': 'IlluminationProps',
                             'b65a3e76-2993-11d1-9a43-0080c7ec5c96': 'SimpleTextPath',
                             '2de21000-bdeb-11d1-970b-0080c7e04196': 'BezierTextPath',
                             'c8d09ed2-4fbb-11d1-9a72-0080c7ec5c96': 'BalloonCallout',
                             'c8d09ed3-4fbb-11d1-9a72-0080c7ec5c96': 'LineCallout',
                             'c5c02d50-7282-11d2-9816-0080c7e04196': 'MarkerTextBackground',
                             '936ce290-0971-11d3-bcad-0080c7e04196': 'FontSize',
                             '0e5d8c66-8d91-11d3-9fca-00c04f6bc6a5': 'SymbolCollection',
                             'e0554440-25cf-11d3-9f97-00c04f6bc6a5': 'OverposterTextPath',
                             'fa37b822-a959-4acd-834a-0e114bf420b8': 'SimpleLineCallout',
                             '3ebbe031-557d-11d1-b254-0000f878229e': 'NetWeight',
                             '19bdc491-6201-11d1-b255-0000f878229e': 'NetWeightAssociation',
                             'f94f7534-9fdf-11d0-bec7-00805f7c4268': 'Field',
                             'f94f7535-9fdf-11d0-bec7-00805f7c4268': 'Fields',
                             '826e2701-4da6-11d1-8824-0000f877762d': 'Index',
                             '03859813-4da5-11d1-8824-0000f877762d': 'Indexes',
                             '439a0d52-3915-11d1-9ca7-0000f8780619': 'GeometryDef',
                             'fdfebd95-ed75-11d0-9a95-080009ec734b': 'QueryFilter',
                             'fdfebd96-ed75-11d0-9a95-080009ec734b': 'SpatialFilter',
                             '06783db1-e5ee-11d1-b0a2-0000f8780820': 'TableName',
                             '905cec64-0b2c-11d4-a060-00c04f6bdd84': 'ObjectClassName',
                             '81caa5d8-90c5-11d3-9f7b-00c04f6bc886': 'TableQueryName',
                             'dab3ee10-0f92-455d-8aa2-3d4ade5b2f7d': 'RelQueryTableName',
                             '81caa5d9-90c5-11d3-9f7b-00c04f6bc886': 'FeatureQueryName',
                             '311c2ee1-da65-11d2-8a54-000000000000': 'RelationshipClassName',
                             '6dba211b-ebdb-11d3-9f84-00c04f6bc886': 'MemoryRelationshipClassName',
                             'f452b4d2-9a95-11d2-aacf-00c04fa37b82': 'GeometricNetworkName',
                             'f84c6c1b-47ff-11d2-9933-0000f80372b4': 'CodedValueDomain',
                             'f290d9e0-58e5-11d2-ab26-000000000000': 'EdgeConnectivityRule',
                             'f290d9e1-58e5-11d2-ab26-000000000000': 'JunctionConnectivityRule',
                             'f84c6c1a-47ff-11d2-9933-0000f80372b4': 'RangeDomain',
                             'f84c6c1e-47ff-11d2-9933-0000f80372b4': 'RelationshipRule',
                             '99f50761-c137-11d2-9f83-00c04f8ed211': 'XmlPropertySet',
                             'd4224309-a5cb-11d2-9b10-00c04fa33299': 'CadDrawingName',
                             'e28c4e63-3f55-11d1-885e-0000f87808ee': 'Paper',
                             'ae064d01-d6ce-11d0-867a-0000f8751720': 'EmfPrinter',
                             'e28c4e61-3f55-11d1-885e-0000f87808ee': 'PsPrinter',
                             '8ab7fbe1-d871-11d0-8389-080009b996cc': 'LineElement',
                             '530fd712-ef0c-11d0-83a0-080009b996cc': 'MarkerElement',
                             '3a9767c2-f253-11d0-83a4-080009b996cc': 'RectangleElement',
                             '3a9767c7-f253-11d0-83a4-080009b996cc': 'PolygonElement',
                             '204034d3-f6ea-11d0-83ad-080009b996cc': 'TextElement',
                             '827b9a90-c067-11d2-9f22-00c04f6bc8dd': 'EmfPictureElement',
                             '827b9a91-c067-11d2-9f22-00c04f6bc8dd': 'BmpPictureElement',
                             '974111db-c5d2-11d2-9f28-00c04f6bc8dd': 'CircleElement',
                             '4eda1081-12ea-11d3-9f8f-00c04f6bc8dd': 'EllipseElement',
                             '803577d2-f8a3-11d0-83af-080009b996cc': 'GroupElement',
                             'e01ba2c5-24b2-11d3-b8aa-00600802e603': 'FrameElement',
                             'e91ae5c9-2c16-11d4-80e2-00c04fa0adf8': 'MultiPatchElement',
                             'f6705e85-523b-11d1-86e7-0000f8751720': 'OleFrame',
                             'ce8f3972-e9be-11d1-a232-080009b6f22b': 'ElementCollection',
                             'a5d0f017-62dd-11d2-87be-0000f8751720': 'SymbolBorder',
                             '1baa33e9-e13b-11d2-b868-00600802e603': 'SymbolBackground',
                             'a8861e66-57aa-47d0-aaf8-b288b4fd5240': 'SymbolShadow',
                             '3141f2fc-38e2-11d1-8809-080009ec732a': 'BasicOverposter',
                             'ee535289-41c9-11d1-880a-080009ec732a': 'BasicOverposterLayerProperties',
                             '2442958c-d711-11d2-9f41-00c04f6bc6a5': 'LineLabelPosition',
                             '261a4377-d9d5-11d2-a806-cc9f870bcd5a': 'LineLabelPlacementPriorities',
                             '261a4372-d9d5-11d2-a806-cc9f870bcd5a': 'PointPlacementPriorities',
                             'aa157207-e079-11d2-9f48-00c04f6bc6a5': 'AnnotationVBScriptEngine',
                             'aa157208-e079-11d2-9f48-00c04f6bc6a5': 'AnnotationJScriptEngine',
                             '4c90de7b-cb77-11d2-9f34-00c04f6bc6a5': 'LabelStyle',
                             '01004145-0d1c-11d2-a26f-080009b6f22b': 'LabelEngineLayerProperties',
                             'f3435801-5779-11d0-98bf-00805f7ced21': 'SimpleRenderer',
                             '3036d35e-ede5-11d0-87fe-080009ec732a': 'Hyperlink',
                             'e3875b71-d9f5-11d1-add4-080009ec732a': 'SelectionEnvironment',
                             'a2baae2d-969b-11d2-ae77-080009ec732a': 'FieldInfo',
                             '9646bb83-9512-11d2-a2f6-080009b6f22b': 'CompositeGraphicsLayer',
                             'd5bb4b88-e0a1-11d2-9f4d-00c04f6bc78e': 'FeatureIDSet',
                             'edad6647-1810-11d1-86ae-0000f8751720': 'GroupLayer',
                             '0c22a4c9-dafd-11d2-9f46-00c04f6bc78e': 'CoverageAnnotationLayer',
                             '8c439002-14ec-11d2-a27e-080009b6f22b': 'AnnotateMap',
                             '8c439001-14ec-11d2-a27e-080009b6f22b': 'AnnotateMapProperties',
                             '34b2ef83-f4ac-11d1-a245-080009b6f22b': 'FDOGraphicsLayer',
                             '85c3dac6-6578-11d3-9fba-00c04f6bc6a5': 'GraphicsLayerScale',
                             'e6bdaa76-4d35-11d0-98be-00805f7ced21': 'Map',
                             '6589f140-f7f7-11d2-b872-00600802e603': 'ScaleLine',
                             '6589f141-f7f7-11d2-b872-00600802e603': 'SteppedScaleLine',
                             '6589f143-f7f7-11d2-b872-00600802e603': 'HollowScaleBar',
                             '6589f146-f7f7-11d2-b872-00600802e603': 'SingleDivisionScaleBar',
                             '7a3f91db-b9e3-11d1-8756-0000f8751720': 'Scalebar',
                             '6589f147-f7f7-11d2-b872-00600802e603': 'AlternatingScaleBar',
                             '6589f148-f7f7-11d2-b872-00600802e603': 'DoubleAlternatingScaleBar',
                             '7a3f91dc-b9e3-11d1-8756-0000f8751720': 'ScaleText',
                             '7a3f91dd-b9e3-11d1-8756-0000f8751720': 'MarkerNorthArrow',
                             '7a3f91de-b9e3-11d1-8756-0000f8751720': 'Overview',
                             '7a3f91df-b9e3-11d1-8756-0000f8751720': 'MapTitle',
                             '7a3f91e3-b9e3-11d1-8756-0000f8751720': 'MapInset',
                             '7a3f91e4-b9e3-11d1-8756-0000f8751720': 'Legend',
                             '7a3f91e5-b9e3-11d1-8756-0000f8751720': 'LegendFormat',
                             'bbb1ae73-41e3-11d2-ae1e-080009ec732a': 'AOIBookmark',
                             'ec65b35b-4342-11d2-ae22-080009ec732a': 'FeatureBookmark',
                             'ee7c5047-e3db-11d3-a096-00c04f6bc626': 'StandaloneTable',
                             'dd94d770-836d-11d0-87ec-080009ec732a': 'MapFrame',
                             '83ffcae1-edca-11d0-8683-0000f8751720': 'MapSurroundFrame',
                             'ce41c506-9df9-11d2-aade-000000000000': 'DMSGridLabel',
                             'ce41c507-9df9-11d2-aade-000000000000': 'FormattedGridLabel',
                             'ce41c508-9df9-11d2-aade-000000000000': 'MixedFontGridLabel',
                             'ce41c50d-9df9-11d2-aade-000000000000': 'BackgroundTabStyle',
                             'ce41c50e-9df9-11d2-aade-000000000000': 'ContinuousTabStyle',
                             'ac81ecf7-9ee4-11d2-aadf-000000000000': 'RoundedTabStyle',
                             'ac81ecf8-9ee4-11d2-aadf-000000000000': 'ButtonTabStyle',
                             'ac81ecfb-9ee4-11d2-aadf-000000000000': 'SimpleMapGridBorder',
                             '6ca416b0-e160-11d2-9f4e-00c04f6bc78e': 'CalibratedMapGridBorder',
                             '03762c8f-f4d0-11d1-ade8-080009ec732a': 'Graticule',
                             '03762c90-f4d0-11d1-ade8-080009ec732a': 'MeasuredGrid',
                             '03762c91-f4d0-11d1-ade8-080009ec732a': 'IndexGrid',
                             'ff501c8a-d74b-11d2-9f43-00c04f6bc78e': 'CustomOverlayGrid',
                             '83ffcae2-edca-11d0-8683-0000f8751720': 'LocatorRectangle',
                             'dd94d76e-836d-11d0-87ec-080009ec732a': 'PageLayout',
                             'dd94d76f-836d-11d0-87ec-080009ec732a': 'Page',
                             '31e081ac-cb02-11d1-876c-0000f8751720': 'RulerSettings',
                             '31e081ad-cb02-11d1-876c-0000f8751720': 'SnapGrid',
                             '31e081ae-cb02-11d1-876c-0000f8751720': 'SnapGuides',
                             '56fd87f7-ddce-11d1-8778-0000f8751720': 'GraphicSnapEnvironment',
                             'fc27fab0-db88-11d1-8778-0000f8751720': 'GridSnap',
                             'fc27fab1-db88-11d1-8778-0000f8751720': 'GuideSnap',
                             'fc27fab2-db88-11d1-8778-0000f8751720': 'MarginSnap',
                             'fc27fab3-db88-11d1-8778-0000f8751720': 'RulerSnap',
                             'bdbbb415-d0b2-11d1-aed9-080009ec734b': 'GxFileFilter',
                             '3beb09e4-3941-4a07-9d1a-ec2b43ba7d50': 'ShortcutName',
                             'b1de27ae-d892-11d1-aa81-064342000000': 'GxContentsView',
                             '22e48ecb-f92d-11d3-a68d-0008c7d3ae8d': 'GxContentsViewColumn',
                             'e299adbd-a5c3-11d2-9b10-00c04fa33299': 'CadLayer',
                             'e0f384b6-e0c1-11d2-9b30-00c04fa33299': 'CadFeatureLayer',
                             'e1b71879-a5df-11d4-a215-444553547777': 'CadAnnotationLayer',
                             '006b1afe-c66c-11d0-b94c-080009ee4e51': 'MxDocument',
                             'fddb19f0-cb6f-11d2-9f38-00c04f6bc78e': 'TOCDisplayView',
                             '089874fb-cc18-11d2-9f39-00c04f6bc78e': 'TOCCatalogView',
                             '4657d950-5ffb-11d3-9f6c-00c04f6bc886': 'TableProperties',
                             '4657d952-5ffb-11d3-9f6c-00c04f6bc886': 'TableProperty',
                             '8945ac7e-d51e-11d3-a65e-0008c7df88db': 'DataGraphWindow',
                             '9685caf0-bf13-4283-b388-a5730352c778': 'LocatorWorkspaceName',
                             'c24ffe64-88be-11d3-9f66-00c04f6bdf06': 'LocatorName',
                             '71045ca2-7902-11d4-9fe5-00c04f6bdf06': 'XYEvent2FieldsProperties',
                             '309aa920-eaec-11d3-9f8a-00c04f6bdf06': 'XYEventSourceName',
                             'c13d6537-3c80-11d4-9fcd-00c04f6bdf06': 'RouteMeasurePointProperties',
                             '35bdf2f0-3b21-11d4-9fcb-00c04f6bdf06': 'RouteMeasureLineProperties',
                             '63be9174-b8c7-11d3-9f7c-00c04f6bdf06': 'RouteEventSourceName',
                             '8cc373a6-2121-11d4-9fc2-00c04f6bdf06': 'RouteMeasureLocatorName',
                             'f8842f20-bb23-11d0-802b-0000f8037368': 'Editor',
                             '5e81b7ca-ce16-11d0-802d-0000f8037368': 'FeatureSnap',
                             '055b2b99-f2c9-11d2-9fc1-00c04f8ed211': 'MetadataExtension',
                             '76360e01-ec46-11d1-8d21-0000f8780535': 'RasterDatasetName',
                             'bc25e113-168b-11d2-8d25-0000f8780535': 'RasterBandName',
                             '942ac1c0-fec4-11d3-8d6f-00c04f5b87b2': 'SdeRasterTableName',
                             '0842b595-4f2f-11d2-9f43-00c04f8ece3d': 'RasterUniqueValueRenderer',
                             'ce8b2f44-a027-11d2-aae7-00c04fa33416': 'RasterClassifyColorRampRenderer',
                             '577f1870-7037-11d2-9f29-00c04f8ed1d7': 'RasterRGBRenderer',
                             'a301a3b2-74d7-11d2-9f29-00c04f8ed1d7': 'RasterStretchColorRampRenderer',
                             'd02371c9-35f7-11d2-b1f2-00c04f8edeff': 'RasterLayer',
                             '1493c960-f620-11d3-8d6c-00c04f5b87b2': 'RasterCatalogLayer',
                             'b81f9ae0-026e-11d3-9c1f-00c04f5aa6ed': 'ColorSymbol',
                             'c7b5a5ef-c211-11d2-babe-00c04fa33c20': 'EdgeFlagDisplay',
                             'ed830eed-c211-11d2-babe-00c04fa33c20': 'JunctionFlagDisplay',
                             '5f13f416-42bc-11d2-a569-0000f8774f0f': 'TinName',
                             'f12e6df0-384c-11d2-b1f2-00c04f8edeff': 'TinFaceRenderer',
                             '13cb60ab-88a0-11d2-81eb-00104bc4cd03': 'TinEdgeRenderer',
                             '6ef19ac2-84aa-11d2-81eb-00104bc4cd03': 'TinNodeRenderer',
                             '91fb1b62-8944-11d2-81ec-00104bc4cd03': 'TinSlopeRenderer',
                             'bebd2dae-8bc7-11d2-81ec-00104bc4cd03': 'TinAspectRenderer',
                             'ebb7311b-99f8-11d2-81ed-00104bc4cd03': 'TinElevationRenderer',
                             'aa8745c8-aa66-11d2-81fa-00104bc4cd03': 'TinFaceValueRenderer',
                             '322934b8-b224-11d2-81fc-00104bc4cd03': 'TinNodeValueRenderer',
                             'ba20564c-dbe3-11d2-9f39-00c04f6bc619': 'TinNodeElevationRenderer',
                             'ba20564f-dbe3-11d2-9f39-00c04f6bc619': 'TinBreaklineRenderer',
                             'fe308f38-bdca-11d1-a523-0000f8774f0f': 'TinLayer',
                             '3549c4f9-f9c2-11d3-9f64-00c04f8ed1d7': 'RasterAnalysis',
                             '630f3de8-e213-4a5e-ac01-2bd5bcd646b6': 'IMSServiceName',
                             'ee16a1e6-bde9-47ed-be03-d711db3102e5': 'ACSimpleRenderer',
                             '1acdebe9-9f89-48dd-bc28-780acd9d4256': 'ACGroupRenderer',
                             '69d20498-f616-454e-9cca-54e0f600c25a': 'ACScaleDependentRenderer',
                             'd2ea35c1-d393-4066-901b-b44108163cb3': 'ACSimpleLineSymbol',
                             'b019758d-5f2b-4310-b409-c042391f6149': 'ACSimpleFillSymbol',
                             '72341cc3-1a6b-4ee9-9810-ba77fd277a2a': 'ACSimplePolygonSymbol',
                             '7fe0318e-3246-483f-9590-ed69e9c09af8': 'ACSimpleMarkerSymbol',
                             '22e484b7-1ae7-4b13-92aa-3e081d00b539': 'ACTextSymbol',
                             '05b3287e-db2b-436b-bb3d-b01ef5236446': 'ACValueMapRenderer',
                             '58063155-bded-4188-b996-a09a73e93f0a': 'ACTrueTypeMarkerSymbol',
                             '76315040-c3b0-4100-b949-135948839c67': 'ACRasterMarkerSymbol',
                             '8d574cab-ff08-473e-8b73-bcb9e7605a20': 'ACRasterShieldSymbol',
                             '53455d9e-c3e8-4ffa-81f0-38ed2e238b9b': 'ACHashLineSymbol',
                             '34a16eda-8a58-44a4-9342-98533b8564a9': 'ACRasterFillSymbol',
                             '3235e2dd-b46b-4448-b7e7-aeed8ed0b272': 'ACGradientFillSymbol',
                             'd33fe4fb-e17b-4ea9-a01e-a03f5f394e96': 'ACCalloutMarkerSymbol',
                             'f2005b08-f5d0-44b9-bcd5-4d6215c58e4e': 'ACShieldSymbol',
                             '2c231f73-0467-473c-b257-23ce3b89d31c': 'ACTextMarkerSymbol',
                             'd10f211f-3083-4bfe-9d3f-ad77bcb151f0': 'ACSimpleLabelRenderer',
                             '3d7551d0-6eef-4dc8-9098-99c9925eb233': 'ACValueMapLabelRenderer',
                             'e774fd60-5f97-4630-bc9b-9116645ac184': 'ACMap',
                             '5ab8731f-4db7-44d6-8c27-d94fe9c6528a': 'ACFeatureLayer',
                             '0046627f-7def-4aa1-ad72-a1b02b22d39b': 'ACImageLayer',
                             '6c3ad32d-e553-4422-b649-357027f701eb': 'ACAcetateLayer',
                             'dc850600-d521-11d3-9ff4-00c04f6bc6a5': 'IMSMapLayer',
                             'c08e2878-f9ff-11d3-80d3-00c04f601565': 'DimensionStyle',
                             '45b2fa28-fa01-11d3-80d3-00c04f601565': 'DimensionStyles',
                             'd27a074a-10ad-11d4-80d7-00c04f601565': 'DimensionShape',
                             'f1e27e32-0ca7-11d4-80d7-00c04f601565': 'DimensionLayer'}

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
