
from collections import Counter
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
c1 = Counter(s1)
n1 = c1['a'] + c1['e'] + c1['i'] + c1['o'] + c1['u']
s2= String2.reversal()
c2 = Counter(s2)
n2 = c2['a'] + c2['e'] + c2['i'] + c2['o'] + c2['u']
s3= String3.reversal()
c3 = Counter(s3)
n3 = c3['a'] + c3['e'] + c3['i'] + c3['o'] + c3['u']
numberlist = [n1,n2,n3]
stringlist = [s1,s2,s3]
nlist =[stringlist,numberlist]
Max = numberlist.index(max(numberlist))
Min = numberlist.index(min(numberlist))

FirstString = stringlist[Max]
LastString = stringlist[Min]

del stringlist[Max]
del stringlist[Min]

MedString = stringlist[0]

print FirstString
print MedString
print LastString



