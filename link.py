# link.py  10/01/2013  (c) 2013 @whaleygeek
#
# A simple client/server communications link abstraction
#
# Usage:
# import link
#
# def handler(reason, data):
#   print "server:" + reason + "=" + data
#  
# server = link.runDummyServer(handler)
# client = link.open(server)
#
# for i in range(10):
#   client.send("test " + str(i))


import thread
import Queue

# A placeholder for socket servers (TODO later)
class _Server:
  def rx(self, data):
    pass
    
  def setHandler(self, handler):
    pass
    
  def listen(self):
    pass
    
  def isOpen(self):
    pass

  def wait(self):
    pass
    
  def check(self):
    pass
    
  def send(self, data):
    pass
    
  def close(self):
    pass
    
    



# A placeholder for socket clients (TODO later)

class _Client:
  def open(self, host):
    pass
    
  def isOpen(self):
    pass
    
  def wait(self):
    pass
    
  def check(self):
    pass
    
  def send(self, data):
    pass
    
  def close(self):
    pass


# A server that communicates via an internal queue (mainly for mock testing)    
    
class _DummyServer(_Server):
  handler = None
  queue = Queue.Queue()
  
  def rx(self, data):
    self.queue.put(data)
  
  def setHandler(self, handler):
    self.handler = handler
    
  def listen(self):
    thread.start_new_thread(_DummyServer.thread, (self,))
    
  def thread(self):
    while True:
      data = self.queue.get()
      if (self.handler != None):
        self.handler("data", data)
    
  def send(self, data):
    pass
    
  def close(self):
    pass
    
    
# A client that communicates with a local server (mainly for mock testing)

class _DummyClient(_Client):
  server = None
  
  def __init__(self, server):
    self.server = server
    
  def wait(self):
    pass
    
  def check(self):
    pass
    
  def send(self, data):
    if (self.server != None):
      self.server.rx(data)

  def close(self):
    pass    


# Helper functions to make the module interface nice and clean

def runServer(handler):
  s = _Server()
  s.setHandler(handler)
  s.listen()
  return s
    
def runDummyServer(handler):
  s = _DummyServer()
  s.setHandler(handler)
  s.listen()
  return s

def open(host):
  try:
    host.rx("start")
    print "opening a server proxy connection"
    return _DummyClient(host)
      
  except AttributeError:
    print "opening a client connection"
    c = _Client()
    c.open(host)
    return c
    
    
# MINIMAL TEST HARNESS
# Note this also excercises the "server connect" semantics,
# but these are not implemented yet

if __name__ == "__main__":
  import time
  
  def handler(reason, data):
    print "server:" + reason + "=" + data
    
  print "starting server"
  server = runDummyServer(handler)
  
  print "server started"
  
  for c in range(4):
    print "opening client " + str(c)
    client = open(server)
    
    print "client opened"
    
    for m in range(5):
      print "sending " + str(m)
      client.send("hello " + str(m))
      #testing
      server.send("hello " + str(m))
      
      print "waiting"
      time.sleep(1)
      
    print "closing client " + str(c)
    client.close()
    
  print "closing server"
  server.close()
  
    
  