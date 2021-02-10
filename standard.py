from xmlrpclib import ServerProxy
from SimpleXMLRPCServer import SimpleXMLRPCServer

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
