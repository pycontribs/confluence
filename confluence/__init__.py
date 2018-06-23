#!/usr/bin/env python
from pbr.version import VersionInfo
from .confluence import Confluence
import sys

_v = VersionInfo('confluence').semantic_version()
__version__ = _v.release_string()
version_info = _v.version_tuple()

__all__ = ('Confluence', '__version__', '__author__', '__copyright__', '__email__', '__status__', '__date__')

if sys.hexversion < 0x02070000:
    sys.exit("Python 2.7 or newer is required by confluence module.")
