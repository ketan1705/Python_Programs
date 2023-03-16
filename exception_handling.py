'''try:
	a = 10/0
	print(a)
except(ArithmeticError):
	print("This statement is raising an exception error")
else:
	print("Welcome")'''

'''
def fun(a,b):
	try:
		c= (a + b)/(a-b)
	except(ArithmeticError):
		print("ARITHMETIC EXCEPTION")
	else:
		print(c)
	finally:
		print("End of the world")
fun(2.0,3.0)
fun(3.0,3.0)'''



# Argument of an Exception
'''
def fun(a):
	try:
		return int(a)
	except ValueError as VE:
		print("argument is not a number")
fun(11)
fun("String")'''

