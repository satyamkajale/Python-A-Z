# Python Program to read an integer from the user and find if the number is Even or Odd

num = int(input("enter an integer "))

#logic number 1
res = num % 2
if res == 0:
	print("even")
else:
	print("odd")

#logic number 2
if num % 2 == 0:
	print("even")
else:
	print("odd")

#After : there comes indentation which is alternative for C's {   }
