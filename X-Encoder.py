#!/usr/bin/python

import base64
import sys 

print " __   __     ______                     _           "
print " \ \ / /    |  ____|                   | |          "
print "  \ V / ___ | |__   _ __   ___ ___   __| | ___ _ __ "
print "   > <  ___ |  __| | '_ \ / __/ _ \ / _` |/ _ \ '__|"
print "  / . \     | |____| | | | (_| (_) | (_| |  __/ |   "
print " /_/ \_\    |______|_| |_|\___\___/ \__,_|\___|_|   "
print "	         	  https://github.com/Xpykerz "
print "	                  Ask: https://t.me/MQ_XZ    "
print "\n"

def encode():
	str = raw_input("Enter Text to Encode:\t")
	str = str.encode('base64','strict');
	print "\nEncoded Text:\n"
	print str
	St()

def decode():
	str = raw_input("Enter Text to decode:\t")
	str = str.decode('base64','strict');
	print "\nDecoded Text:\n"
	print str
	St()

def St():
	print "1) Encoding"
	print "2) Decoding"
	print "3) Exit"
	select = input ("Select :  ")

	if select==1:
		encode()
	elif select==2:
		decode()
	elif select==3:
		print "\nSupport @Xpykerz"
		sys.exit()
	else :
		print "Wrong selection"
		St()
St()