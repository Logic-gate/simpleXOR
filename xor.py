#!/usr/bin/env python

import sys

if len(sys.argv) != 3:
	print 'Usage: ./xor.py [file1] [file2]'
else:
	with open(sys.argv[1], "rb") as f:
		content1 = f.read()
	
	with open(sys.argv[2], "rb") as f:
		content2 = f.read()
		
	len1 = len(content1)
	len2 = len(content2)
	crypt = 0
	
	if len1 == len2:	
		crypt = 3
	elif len1 % len2 == 0: 
		crypt = 1
	elif len2 % len1 == 0:
		crypt = 2
	
	result = ""
	
	if crypt == 0:
		print 'Length of bytes for XOR do not match'
	else:
		if crypt == 3:
			for x in range(0, len1):
				result += chr(ord(content1[x]) ^ ord(content2[x]))
		elif crypt == 1:
			for x in range(0, len1):
				result += chr(ord(content1[x]) ^ ord(content2[x % len2]))
		elif crypt == 2:
			for x in range(0, len2):
				result += chr(ord(content2[x]) ^ ord(content1[x % len1]))
				
		print result
		
		
		
		
