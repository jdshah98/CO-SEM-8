try:
	fin = open("input.txt","r")
	lines = fin.readlines()
	if lines==[]:
		print("File is Empty")
	else:
		content=''.join(lines)
		print(content)
		print("Count: ",content.count(" "));
	fin.close()
except FileNotFoundError:
	print("File Doesn't exist")
