# futurized code

# These were added after trying to pass the --import-all futurize flag recommended to solve some more stuff..
# They didn't make a difference..
# from __future__ import print_function
# from __future__ import unicode_literals
# from __future__ import absolute_import
# from __future__ import division
# from builtins import *

# futurize stage2 automatic code
from future import standard_library
standard_library.install_aliases()
from xmlrpc.client import ServerProxy

# futurize also added this import automatically, which is broken..
# (https://github.com/PythonCharmers/python-future/issues/280,
# https://github.com/PythonCharmers/python-future/issues/567)
# from xmlrpc.server import SimpleXMLRPCServer  # 2.x

# Replaced them with this alpha quality backport (https://python-future.org/standard_library_imports.html)
# It's where the problematic encoding takes place)
from future.backports.xmlrpc.server import SimpleXMLRPCServer

import os
import time


pid = os.fork()
if pid:
    server = SimpleXMLRPCServer(("localhost", 8000))
    server.register_function(lambda x, y: x + y, 'add')

    server.serve_forever()
else:
    time.sleep(1)

    s = ServerProxy('http://localhost:8000', verbose=True)
    print(s.add(2, 3))
