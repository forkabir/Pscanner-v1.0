#!/usr/bin/python
#Coded By Badreddine CHamkhi 14/10/2017
#Don't Change my fucking rights ;*
#Basic Port Scanner
# -*- coding: utf-8 -*-
#import_zone
import optparse
from socket import *
from threading import *
from platform import system
import os 
#clearscrn
def clearscrn(): 
	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')
clearscrn()
#banner 
print ''' \033[1;36m
						#####   ####   ####    ##   #    # #    # ###### #####  
						#    # #      #    #  #  #  ##   # ##   # #      #    # 
						#    #  ####  #      #    # # #  # # #  # #####  #    # 
						#####       # #      ###### #  # # #  # # #      #####  
						#      #    # #    # #    # #   ## #   ## #      #   #  
						#       ####   ####  #    # #    # #    # ###### #    # 
                                                        
												v 1.0

\033[1;m
'''
print ''' \033[1;37m
							Coded By Badreddine Camkhi
\033[1;m
'''

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send('hello\r\n')
		
		results = connSkt.recv(100)
		screenLock.acquire()
		print "[+] " + str(tgtPort) + "/tcp open"
	except:
		screenLock.acquire()
		print "[-] " + str(tgtPort) + "/tcp closed"
	finally:
		screenLock.release()
		connSkt.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve " + tgtHost + ": Unknown host"
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print "\n[+] Scan Results for: " + tgtName[0]
	except:
		print "\n[+] Scan results for: " + tgtIP
	
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()

def Main():
	parser = optparse.OptionParser('usage %prog '+\
		'-H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', \
		help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', \
		help='specify target port[s] seperated by comma')
	(options, args) = parser.parse_args()
	if (options.tgtHost == None) | (options.tgtPort == None):
		print parser.usage
		exit(0)
	else:
		tgtHost = options.tgtHost
		tgtPorts = str(options.tgtPort).split(',')

	portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
	Main()



