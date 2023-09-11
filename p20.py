# wapp to read marks between 0 and 100 and print the grade
# marks >=80 print Grade A, marks >= 60 print Grade B
# marks >=40 print Grade C else print Grade D

marks = float(input("enter the marks "))
if marks < 0 or marks > 100:
	print("invalid marks ")
elif marks >= 80:
	print("Grade A")
elif marks >= 60:
	print("Grade B")
elif marks >= 40:
	print("Grade C")
else:
	print("Grade D")