myfile = open('test.txt','r')
dictionary = {}

wordlist = []
NMyfile = myfile.read().splitlines()

		
for lines in NMyfile:
	lines = lines.split(' ')
	for word in lines:
		dictionary[word] =0
		wordlist.append(word)
for words in wordlist:
	
	dictionary[words] = dictionary[words]+1	
	
print dictionary
