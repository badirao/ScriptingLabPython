l = [2,3,4,1,5,7,3,2]
i = 2
def recmax(l,n):
  global i
  a = l[0:i]
  if len(a) == 1:
	print a[0]
  else:
    l.remove(min(a))
    i = i+1
    recmax(l,len(l))
recmax(l,len(l))
