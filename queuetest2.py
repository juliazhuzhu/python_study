#!/usr/bin/python3

"producer and consumer threads communicating with a shared queue"

numconsumers = 2
numproducers = 4
nummessages  = 4

import _thread as thread, queue, time
import threading

sameprint = thread.allocate_lock()
dataQueue = queue.Queue()

def producer(idnum,dataqueue):
	for msgnum in range(nummessages):
		time.sleep(idnum)
		dataqueue.put('[producer id=%id, count=%d]'%(idnum,msgnum))

def consumer(idnum,dataqueue):
	while True:
		time.sleep(0.1)
		try:
			data = dataqueue.get(block=False)
		except queue.Empty:
			pass
		else:
			with sameprint:
				print('consumer',idnum, 'got =>', data)


if __name__ == '__main__':
	for i in range(numconsumers):
		thread = threading.Thread(target=consumer,args=(i,dataQueue))
		thread.daemon = True #else cannot exit!
		thread.start()

	waitfor = []

	for i in range(numproducers):
		for i in range(numproducers):
			thread = threading.Thread(target=producer,args=(i,dataQueue))
			waitfor.append(thread)
			thread.start()

	for thread in waitfor: thread.join()

	print("Main thread exiting.")