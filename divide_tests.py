# Author: Daniel Throop
# Date: 04/13/20
# File Name: divide_tests.py
# Description: Methods for application that demonstrates divisibily tests for integers: 4, 9, and 11 (number theory defintion)

def nine_div(x):	
	sum = 0
	
	for i in x:
		sum += int(i)

	if sum % 9 == 0:
		return True
	else:
		return False

def four_div(x):
	if int(x[-2:])%4 == 0:
		return True
	else:
		return False

def eleven_div(x):
	sum = 0
	count = 0

	for i in x:
		if count%2 == 0:
			sum += int(i)
		else:
			sum += -int(i)
		count+=1

	if sum%11 == 0:
		return True
	else:
		return False




