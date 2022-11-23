#!/usr/bin/env python

import os
import re
import sys
import argparse

my_parser = argparse.ArgumentParser(description='Search a file for patterns and perform different operations', usage=' search.py --pattern PATTERN [--list] [--list-line] [--number] [--count] [--delete-lines] [--replace REPLACE [--cipher CIPHER] [--out OUT] file')

my_parser.add_argument('--pattern', '-p', type=str, help='regular expression to match file content to', required=True)
my_parser.add_argument('--list', '-l', action='store_true', help='list matches in the file')
my_parser.add_argument('--list-lines', action='store_true', help='print lines that contain matches')
my_parser.add_argument('--number', action='store_true', help='print line numbers before matching')
my_parser.add_argument('--count', '-c', action='store_true', help='only count matches in the file')
my_parser.add_argument('--delete-lines', action='store_true', help='delete lines that contain matches from input file')
my_parser.add_argument('--replace', '-r', type=str, help='string to replace matches with')
my_parser.add_argument('--mask', help='a character to mask matches with')
my_parser.add_argument('--out', '-o', help='output file to write changes to instead of applying them to input file', required=True)

args = my_parser.parse_args()

input_file = sys.argv.pop()
pat = args.pattern

counter = 0
pattern = re.compile(pat)
replacement = args.replace
mask = args.mask

if (args.list == True):		#To print the matches in the file
	counter = 0
	for i, line in enumerate(open(input_file)):
		for match in re.finditer(pattern, line):
			counter += 1
			print ('Found a match: %s' % (match.group()))
	if (args.count == True):	#To print the number of matches in a file
		print ("The number of matches is:", counter)
		
if (args.number == True):	#To print line numbers		
	counter = 0
	for i, line in enumerate(open(input_file)):
		for match in re.finditer(pattern, line):
			counter += 1
			print ('Found a match on line %s: %s' % (i+1, match.group()))
	if (args.count == True):
		print ("The number of matches is:", counter)
			
if (args.list_lines == True):	#To print the lines that contains a match along with line number
	counter = 0
	for i, line in enumerate(open(input_file)):
		for match in re.finditer(pattern, line):
			counter += 1
			print ('Found a match on line %s: %s' % (i+1, line))
	if (args.count == True):
		print ("The number of matches is:", counter)
        		
if (args.delete_lines == True):		#To delete the lines that contains a match
	try:
		with open(input_file, 'r') as f:
			lines = f.readlines()
			
		with open('temp1.txt', 'w') as fw:
			for line in lines:
				match = re.search(pat, line)
				if match == None:
					fw.write(line)
		print ("Matches has been Deleted Successfully")	
		os.replace('temp1.txt', input_file) 			
	except:
		print ("Something went wrong, no Matches were Deleted")
		
if (args.replace != None):		#Replace the matches with a string 
	with open(input_file, 'r') as f:
		lines = f.readlines()
		for line in lines:
			line = re.sub(pat, replacement, line)
			print (line)
			
'''		
if (args.mask != None):		#Mask the matches with a character 
	for i, line in enumerate(open(input_file)):
		for match in re.finditer(pattern, line):			#Mask the matches with a character did not work
			print (line[-1:0].rjust(len(line), + mask))
'''			
			
			
