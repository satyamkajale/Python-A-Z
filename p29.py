# wapp to read a string and find the number of characters in string

s1 = input("enter a string ")

# logic 1
r1 = len(s1)
print(r1)

# logic 2
r2 = 0
for s in s1:		
	r2 = r2 + 1
print(r2)