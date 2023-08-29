# wapp to read two numbers from the user and exchange their values

print("enter first number ")
s1 = input()
n1 = float(s1)

print("enter second number ")
s2 = input()
n2 = float(s2)

print("n1 = ",n1,"n2 = ",n2)

n3 = n1
n1 = n2
n2 = n3

print("n1 = ",n1,"n2 = ",n2)