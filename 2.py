from operator import itemgetter


TempList = []

def c2k(temp):
	choice = raw_input('Celsius to Kelvin or the other way around 1.c2k 2.k2c')
	if choice == '1':
		tempk = temp + 273
		TempList.append(tuple((temp,tempk)))
		return tempk
	if choice == '2':
		tempc = temp - 273
		TempList.append(tuple((temp,tempc)))
		return tempc
def c2f(temp):
	choice = raw_input('Celsius to Farenheit or other way around 1. c2f 2.f2c')
	if choice == '1':
 		tempf = ((5/3)*temp)+32
		TempList.append(tuple((temp,tempf)))
		return tempf
	if choice == '2':
		tempc = (3*(temp-32))/5
		TempList.append(tuple((temp,tempc)))
		return tempc
def k2f(temp):
	choice = raw_input('kelvin to Farenheit or other way around 1. k2f 2.f2k')
	if choice == '1':
		tempf = ((9/5)*temp)-459
		TempList.append(tuple((temp,tempf)))
		return tempf
	if choice == '2':
		tempk = (5*(temp+459))/9
		TempList.append(tuple((temp,tempk)))
		return tempk
while True:
	mainChoice = raw_input('1.c2k and k2c 2.c2f and f2c 3.k2f and k2c 4.display conversions')
	print mainChoice
	if mainChoice == '1':
		temp = int(raw_input('Enter Tempreature'))
		ntemp= c2k(temp)
		print ntemp
	elif mainChoice == '2':
		temp = int(raw_input('Enter Tempreature'))
		print c2f(temp)
	elif mainChoice == '3':
		temp = int(raw_input('Enter Tempreature'))
		print k2f(temp)
	elif mainChoice == '4':
		sorted_choice = int(raw_input('ToValue or FromValue?'))
		if sorted_choice == 1:
			sorted(TempList,key = itemgetter(1))
			print TempList
		if sorted_choice == 2:
			sorted(TempList,key = itemgetter(0))
			print TempList
		
