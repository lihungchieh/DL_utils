import os
from os.path import isfile, join
import sys

if len(sys.argv) != 3:
  print 'Usage: python img.label.py source_dir, label.txt'

def img_label(dataset, filename):
	file_list = [f for f in os.listdir(dataset) if isfile(join(dataset, f)) and f[-3:] == 'jpg']
	label_file = open(filename, 'wb')
  # a four class classification example
	for f in file_list:
		if f[:3] == 'bg_':   # none type
			label_file.write(f + ' 0\n')
		elif f[:3] == 'car': # cars type
			label_file.write(f + ' 1\n')
		elif f[:3] == 'per': # person type
			label_file.write(f + ' 2\n')
		else:
			label_file.write(f + ' 3\n')
		

	label_file.close()

source_dir = sys.argv[1]
label_file = sys.argv[2]
img_label(source_dir, label_file)
