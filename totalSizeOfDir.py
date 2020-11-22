import sys,os

# Usage - python totalSizeOfDir.py 'H:\Software\Code\python-learning'

path = sys.argv[1]


def totalSize(path):
	totalSize= 0
	for i in os.listdir(path):
		totalSize = totalSize + os.path.getsize(os.path.join(path,i))
		print("Size of "+ i + " is "+str(os.path.getsize(os.path.join(path,i))))
	print("Total size - "+ str(totalSize))
	
	
totalSize(path)