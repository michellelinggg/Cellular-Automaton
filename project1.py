import string
import sys

therule = int(sys.argv[1])
numsteps = int(sys.argv[2])
columns = numsteps*2+1
rows = numsteps+1
binaryNum = '{:08b}'.format(therule)
binaryNum = binaryNum[::-1]

def getPattern(binarynumber):
	"""returns which patterns while turn one bits"""
	patternList = []
	for i in range(0,8):
		if binaryNum[i] == '1':
			patternList.append('{:03b}'.format(i))
	return patternList		

def makeString():
	"""makes the first row of strings"""
	x = 0
	firstString = ""
	while x < (columns):
		if x == numsteps:
			firstString+="1"
		else:
			firstString+="0"
		x+=1
	return firstString

print "P1 ", columns, " ", rows
lastString = makeString()
patternList = getPattern(binaryNum)

def getNewString(oldString, listofpatterns):
	"""gets the new row from the old string row"""
	oldString = '0' + oldString + '0'
	newString = ""
	length = 0
	for i in range(1, columns+1):
		for stringpatt in listofpatterns:
			if oldString[i-1:i+2] == stringpatt:
				newString+="1"
		if len(newString) == length:
			newString+="0"
		i+=1
		length+=1
	return newString

def mainFunction(lastString, numbersteps):
	"""the main function where the rows are printed"""
	if numbersteps == 0:
		print lastString
		return None
	else:
		print lastString
		lastString = getNewString(lastString, patternList)
		return mainFunction(lastString, numbersteps-1)

mainFunction(lastString, numsteps)