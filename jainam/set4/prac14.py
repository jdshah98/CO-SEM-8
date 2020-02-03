import os

path=input("Enter path: ")
os.chdir(path)
for dirname, dirnames, filenames in os.walk('.'):
	if dirname=='.':
		for i in filenames:
			if i!='prac14.py':
				os.remove(i)
		print("Deleted All Files")
dirname = input("Enter Directory Name: ")
os.mkdir(dirname)
print("Directory Created")
os.rmdir(dirname)
print("Directory Deleted")
