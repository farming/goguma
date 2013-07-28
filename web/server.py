#!/usr/bin/env python
from goguma import goguma
from gevent import monkey
from socketio.server import SocketIOServer

monkey.patch_all()
PORT = 5000

print 'Listening on http://127.0.0.1:%s ' % PORT
SocketIOServer(('', PORT), goguma, namespace="socket.io", policy_server=False).serve_forever()
#goguma.run(host='0.0.0.0', port=PORT, debug = True)
