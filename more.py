#/usr/bin/python
""" split and interactively page a string or file of text 
"""
import sys 
def more(text, numlines=15):

	lines = text.splitlines() 
	while lines:		# like split('\n') but no '' at end
		chunk = lines[:numlines] 
		lines = lines[numlines:] 
		for line in chunk: 
			print(line) 
		if lines and input('More?') not in ['y', 'Y']: 
			break

def string_test():
	myStr = 'SpurnYou'
	if 'Sprn' in myStr:
		print ('yes')
	else:
		print ('no')

	#find is case sensitive
	if (myStr.find('You') != -1):
		print ('yes')
	else:
		print ('no')
	
	print (myStr.upper())
	print (myStr.lower())
	print (myStr.capitalize())

	testStr = 'xxSpurnxxFuck'
	splitStr = testStr.split('xx')
	print(splitStr)
	print('mlgb'.join(splitStr))

	print(int("57") + 1)
	print('{:d}'.format(558))
	print( str(32) + repr(43))

	file = open('spurn.txt', 'w')
	file.write(str("fuck you")*5 + '\n')
	file.close()

	file = open('spurn.txt', 'r')
	text = file.read()

	file.close()
	print (text[:])

	print (sys.platform[:])
if __name__ == '__main__':
	
	#more(open(sys.argv[1]).read(), 10)
	string_test()

# when run, not imported # page contents of file on cmdline