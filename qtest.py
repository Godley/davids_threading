# qtest.py  11/10/2013  (c) 2013 @whaleygeek
#
# A demonstration of how to use a Queue.
# These queues are threadsafe.
# By default they block if the queue is full/empty,
# but you can override that with additional parameters that set
# non blocking and a wait timeout.

import Queue

q = Queue.Queue(10)

for i in range(10):
  q.put("item " + str(i))
  
while not q.empty():
  i = q.get()
  print i