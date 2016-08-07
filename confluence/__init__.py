#!/usr/bin/env python
# Licensed to PSF under a Contributor Agreement.
# See http://www.python.org/psf/license for licensing details.
from .package_meta import __version__, __date__, __author__, __copyright__, __email__, __status__
from .confluence import Confluence
import sys

__all__ = ('Confluence', '__version__', '__author__', '__copyright__', '__email__', '__status__', '__date__')

if sys.hexversion < 0x02070000:
    sys.exit("Python 2.7 or newer is required by confluence module.")
