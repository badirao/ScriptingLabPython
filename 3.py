3)Write a python class to reverse a sentence (initialized via constructor) word by word.
Example: “I am here” should be reversed as “here am I”. Create instances of this class for each of the
three strings input by the user and display the reversed string for each, in descending order of number of
vowels in the string. 








from operator import itemgetter
dictionary = {}
class r_string:
	
		
	def __init__(self,string):
		self.string = string
	def reversal(self):
    	 n_string = self.string.split(' ')
         rev_list = n_string[::-1]
         reversed_string = " ".join(rev_list)
         return reversed_string

String1 = r_string(raw_input('enter string1'))
String2 = r_string(raw_input('enter string2'))
String3 = r_string(raw_input('enter string3'))

s1=String1.reversal()


s2= String2.reversal()


s3= String3.reversal()


vowels1 = 0
vowels2 = 0
vowels3 = 0

for i in range(0,len(s1)):
	if s1[i] == 'a' or s1[i] == 'e' or s1[i] == 'i' or s1[i] == 'o' or s1[i] == 'u':
		vowels1 = vowels1 + 1
for i in range(0,len(s2)):
	if s2[i] == 'a' or s2[i] == 'e' or s2[i] == 'i' or s2[i] == 'o' or s2[i] == 'u':
		vowels2 = vowels2 + 1  
for i in range(0,len(s3)):
	if s3[i] == 'a' or s3[i] == 'e' or s3[i] == 'i' or s3[i] == 'o' or s3[i] == 'u':
		vowels3 = vowels3 + 1 

dictionary[s1] = vowels1
dictionary[s2] = vowels2
dictionary[s3] = vowels3

sorted_dict = sorted(dictionary.items(),key = itemgetter(1),reverse = True)
print sorted_dict



