import os
for dirname, dirnames, filenames in os.walk('.'):
    if dirname=='.':
        for i in filenames:
            print(i)