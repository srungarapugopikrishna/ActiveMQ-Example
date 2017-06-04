import time
import sys

import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

conn = stomp.Connection([("gopi-machine",61613)])
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', 'password', wait=True)


#conn.send("/topic/ZAXB", "My message 1to10", persistent='false')
conn.subscribe(destination='/queue/einstein', id=1, ack='auto')
#conn.send(body='My message 1to10'.join(sys.argv[1:]), destination='/queue/ZAXB')

time.sleep(2)
conn.disconnect()