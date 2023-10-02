# Python Program to read a string and count the number of lowercase letters,
# number of uppercase letters , number of digits and other characters

s1 = input("enter a string ")

lc, uc, dc, oc = 0, 0, 0, 0

for s in s1:			# s rep each and every character in s1
	if s.islower():
		lc = lc + 1
	elif s.isupper():
		uc = uc + 1
	elif s.isdigit():
		dc = dc + 1
	else:
		oc = oc + 1

print(lc, uc, dc, oc)
