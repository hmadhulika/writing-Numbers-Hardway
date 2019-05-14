from fractions import Fraction
import math

def callFraction(item):
	# define an empty list
	empty_list = []

	d = {}
	# for numerator in a range 1 to 100
	for numr in range(1,100):
		# denominator in a range numerator+1 to 100
		for denr in range(numr+1,101):
			if int((numr/denr)*100) == int(item*100):
				# add it to empty array list
				empty_list.append((numr,denr))
	
	d[item] = empty_list
	
	empty_list = []

	for keys in d:
		(numerator,denominator) = min(d[keys])
		#print("{} cent(s) => {}/{} dollar".format(int(keys*100), numerator,denominator))
		return numerator,denominator

amt = input("Enter the positive amount ")
amt = float(amt)
amtTuple = math.modf(amt)
integerVar = int(amtTuple[1])
if amt < 0:
	print("Please enter the positive Integer")
else:
	n,d = callFraction(amtTuple[0])
	print("{} {}/{} dollar".format(integerVar,n,d))