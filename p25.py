# Python Program to read two integers and find the max of two

n1 = int(input("enter first integer "))
n2 = int(input("enter second integer "))

#approach 1
print(max(n1,n2), " is maximum")

#approach 2

if n1 > n2:
	print("max number = ", n1)
else:
	print("max number = ", n2)

#NOTE- only for knowledge --> max() we can supply any number of arguments atleast two

print(max(10,20,40,30,70,90)," is maximum")  
	
