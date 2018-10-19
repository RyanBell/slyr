#!/usr/bin/env python
"""
std OLE Font
"""

from slyr.parser.object import Object
from slyr.parser.stream import Stream


class WorkspaceName(Object):
    """
    Workspace name information
    """

    ESRI_FILESYSTEM_WORKSPACE = 0
    ESRI_LOCALDATABASE_WORKSPACE = 1
    ESRI_REMOTEDATABASE_WORKSPACE = 2

    def __init__(self):
        super().__init__()
        self.name = ''
        self.category = ''
        self.connection_properties = {}
        self.path_name = ''
        self.type = self.ESRI_FILESYSTEM_WORKSPACE

    @staticmethod
    def guid():
        return '5a350011-e371-11d1-aa82-00c04fa33a15'

    @staticmethod
    def compatible_versions():
        return [1]

    def read(self, stream: Stream, version):
        self.name = stream.read_string('name')
        self.type = stream.read_ushort('type')
        _ = stream.read_string('unknown')
        self.category = stream.read_string('category')
        self.connection_properties = stream.read_object('connection properties')
