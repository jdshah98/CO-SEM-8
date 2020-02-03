import os
for dirname, dirnames, filenames in os.walk('.'):
	if dirname=='.':
		print(filenames)
