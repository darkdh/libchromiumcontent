#!/usr/bin/env python

import os

BINARIES = {
  'darwin': [
    'libupdate_client.a',
    'libclient_update_protocol.a',
    'libcomponent_updater.a',
    'libcourgette_lib.a',
    'liblzma_sdk.a',
    'libversion_info.a',
    'libzip.a',
    'libminizip.a',
  ],
  'linux': [
    'libupdate_client.a',
    'libclient_update_protocol.a',
     'libcomponent_updater.a',
     'libcourgette_lib.a',
     'liblzma_sdk.a',
     'libversion_info.a',
     'libzip.a',
     'libminizip.a',
  ],
  'win32': [
    os.path.join('obj', 'components', 'client_update_protocol.lib'),
    os.path.join('obj', 'components', 'component_updater.lib'),
    os.path.join('obj', 'components', 'update_client.lib'),
    os.path.join('obj', 'components', 'version_info.lib'),
    os.path.join('obj', 'courgette', 'courgette_lib.lib'),
    os.path.join('obj', 'third_party', 'lzma_sdk', 'lzma_sdk.lib'),
    os.path.join('obj', 'third_party', 'zlib', 'google', 'zip.lib'),
    os.path.join('obj', 'third_party', 'zlib', 'minizip.lib'),
    os.path.join('obj', 'third_party', 'zlib', 'zlib.lib'),
  ],
}
