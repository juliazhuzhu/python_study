#!/usr/bin/python
import os

def os_test():
    print (os.getpid())
    print (os.getcwd())
    os.chdir(os.getcwd() + '/cgi_basic')
    print (os.getcwd())


if __name__ == '__main__':
    os_test()