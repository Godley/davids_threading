# demo1.py  11/10/2013  (c) 2013 @whaleygeek
#
# A very simple demo of using keyboard and link to build a chat program
# At the moment this just runs inside the same program using mocks.

import link
import keyboard
import time

def handler(reason, data):
  print "server:" + reason + "=" + data
  

server = link.runDummyServer(handler)
client = link.open(server)

while True:
  key = keyboard.get()
  client.send("pressed " + key)
