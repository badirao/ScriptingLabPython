
a = [1,2,3,4,5,6,4,2,3]
nList = [n for n in a if n%2 == 0 ]
print nList
def singularize(List):
	nList = set(List)
	return nList
def reverse(List):
	nList = List[::-1]
	return nList
if __name__ == '__main__':
 List = list(singularize(a))
 print List
 
 List = reverse(List)
 print List
