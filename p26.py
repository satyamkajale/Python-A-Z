# wapp to read +ve integer and find the reverse
# 8732   2378

num = int(input("enter a +ve integer "))
if num < 0:
	print("Invalid input")
else:
	print("num = ", num)
	rev = 0
	while num > 0:
		digit = num % 10
		rev = rev * 10 + digit
		num = num//10
	print("rev = ", rev)
