# Python P to find the sum of first "n" +ve integers
# i/p:5 1+2+3+4+5 = 15

num = int(input("enter +ve integer "))

#approach 1
if num < 0:
	print("invalid input")
else:
	sum , i = 0 , 1
	while i <= num:
		sum += i
		i += 1
	print("sum = ", sum)
