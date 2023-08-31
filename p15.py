# wapp to read three numbers and find their sum and avg

print("enter first number ")
s1 = input()
n1 = float(s1)

s2 = input("enter second number ")
n2 = float(s2)

n3 = float(input("enter third number "))

sum = n1 + n2 + n3
avg = sum / 3

print("sum = ", round(sum,2))
print("avg = ", round(avg,2))