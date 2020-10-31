# Author: Daniel Throop
# Date: 04/18/20
# File Name: main.py
# Description: Testing in console for divide_tests.py

from divide_tests import four_div, nine_div, eleven_div


print("Divides Tester:")
user_selection = input("Please enter which number you would like to divide by (4, 9, or 11): ")
x = input("Please enter the number by which you would like to divide by " + user_selection + ": ")
print("Calculating...")
print("Does {} | {}?".format(user_selection, x))

if user_selection == '4':
	print(four_div(x))
elif user_selection == '9':
	print(nine_div(x))
else:
	print(eleven_div(x))





