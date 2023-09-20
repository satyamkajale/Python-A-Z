# wapp to read a year and find if its a leap year or not
# every 4 years / multiple of 4 / divisible by 4 --> %

year = int(input("enter year "))

#logic 1 
if year % 4 == 0:
	print("yes")
else:
	print("no")

# logic 2
res = "yes" if year % 4 == 0 else "no"
print(res)

# logic 3
print("yes") if year % 4 == 0 else print("no")