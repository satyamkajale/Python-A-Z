# wapp to read a string and count the number of lowercase letters,
# number of uppercase letters , number of digits and other characters

s1 = input("enter a string ")

lc, uc, dc, oc = 0, 0, 0, 0

for s in s1:			# s rep each and every character in s1
	if s >= 'a' and s <= 'z':
		lc = lc + 1
	elif s >='A' and s <= 'Z':
		uc = uc + 1
	elif s >='0' and s <= '9':
		dc = dc + 1
	else:
		oc = oc + 1

print(lc, uc, dc, oc)