# Python Program to read an integer and find the sum of digits
# i/p: 154  1 + 5 + 4 = 10

num = int(input("enter an integer "))
if num < 0:
	print("invalid input")
else:
	sum = 0
	while num > 0:
		digit = num % 10
		sum = sum + digit
		num = num // 10
	print("sum = ", sum)
