from operator import itemgetter
MyFile = open('text.txt','r')
dictionary = {}
nMyFile = MyFile.read().splitlines()
for line in nMyFile:
	
	word = line.split(' ')
	for words in word:
		if words in dictionary:
			dictionary[words] = dictionary[words] + 1
		else:
			dictionary[words] = 1

nList =  sorted(dictionary.items(),key = itemgetter(1),reverse = True)
nnList =  nList[0:9]
LenList = []
for i in range(0,len(nnList)):
	LenList.append(nnList[i][1])
print LenList
Oddlist = [n**2 for n in LenList if n%2!=0]
Avg = sum(LenList)/len(LenList)
print Avg

print LenList
print Oddlist
