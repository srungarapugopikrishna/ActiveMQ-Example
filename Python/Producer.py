
import time
import sys
import os

import stomp

user = os.getenv("ACTIVEMQ_USER") or "admin"
password = os.getenv("ACTIVEMQ_PASSWORD") or "admin"
host = os.getenv("ACTIVEMQ_HOST") or "localhost"
port = os.getenv("ACTIVEMQ_PORT") or 61613

messages = 2
data = "Python > Work is the integral of the dot product of F and ds"

conn = stomp.Connection(host_and_ports = [("gopi-machine",61613)])
conn.start()
conn.connect(login=user,passcode=password)

# for i in range(1, messages):
#     conn.send("/queue/einstein", data, persistent='false')

conn.send("/queue/einstein", data, persistent='false')
# conn.send("/topic/einstein", "SHUTDOWN", persistent='false')   #To add a topic

conn.disconnect()

