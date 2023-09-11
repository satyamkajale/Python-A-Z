# wapp to read two integers and find the minimum of two.

n1 = int(input("enter first integer "))
n2 = int(input("enter second integer "))
# logic 1
if n1>n2:
	print("minimum of two integers = ", n2)
else:
	print("minimum of two integers = ", n1)

# logic 2
print( min(n1, n2), " is min")