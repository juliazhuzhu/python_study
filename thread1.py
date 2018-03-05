#!/usr/bin/python3
"spawn threads until you press 'q'"

import _thread

def child(tid):
	print('hello from child', tid)

def parent():
	i = 0
	while True:
		i += 1
		_thread.start_new_thread(child, (i,))
		if input() == 'q': break

parent()