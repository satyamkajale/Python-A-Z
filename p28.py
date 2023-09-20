# wapp to find the factorial of the given number
# 0! = 1	1! = 1	 	2! = 2	  3! = 6

num = int(input("enter the integer "))

if num < 0:
	print("invalid input")
else:
	fact = 1
	for i in range(1,num+1):
		fact = fact * i 
	print("fact = ",fact)   