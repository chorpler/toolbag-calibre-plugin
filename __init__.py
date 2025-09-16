# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)
import sys
# import pydevd_pycharm

__license__   = 'GPL v3'
__docformat__ = 'restructuredtext en'


from calibre.customize import EditBookToolPlugin

# pydevd_pycharm.settrace('127.0.0.1', port=12345, stdoutToServer=True, stderrToServer=True)
PLUGIN_NAME = "Diaps Editing Toolbag"
PLUGIN_SAFE_NAME = PLUGIN_NAME.strip().lower().replace(' ', '_')
PLUGIN_DESCRIPTION = 'Various tools for ebook editing.'
PLUGIN_VERSION_TUPLE = (0, 6, 0)
PLUGIN_VERSION = '.'.join([str(x) for x in PLUGIN_VERSION_TUPLE])
PLUGIN_AUTHORS = 'DiapDealer'

print("\n\n\nTOOLBAG INIT: PYTHONPATH:\n" + '\n'.join(sys.path) + "\n\n\n")


class EditingToolbagPlugin(EditBookToolPlugin):

    name = PLUGIN_NAME
    version = PLUGIN_VERSION_TUPLE
    author = PLUGIN_AUTHORS
    supported_platforms = ['windows', 'osx', 'linux']
    description = PLUGIN_DESCRIPTION
    minimum_calibre_version = (1, 46, 0)
