# wapp to read a string and find if its palindrome
# string that reads the same from --> and <--
# nitin, madam

s1 = input("enter the string ")
r1 = s1[::-1]

if s1 == r1:
	print("yes")
else:
	print("no")