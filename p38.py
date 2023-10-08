# wapp to read strings and find if they are anagrams
# two strings having same letters but different meanings
# heart	earth  			fired fried
# aehrt	aehrt

s1 = input("enter the string s1 ")
d1 = sorted(s1)
ns1 = "".join(d1)

s2 = input("enter the string s2 ")
d2 = sorted(s2)
ns2 = "".join(d2)

print(s1, s2)
print(ns1, ns2)

if ns1 == ns2:
	print("yes")
else:
	print("no")

