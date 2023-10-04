# wapp to read username and password and hide password
# if username is kamal and password is classes then o/p success else failure

from getpass import *

username = input("enter username ")
password = getpass("enter password ")

if (username == "kamal") and (password == "classes"):
	print("success")
else:
	print("failure")

# getpass --> module ka naam hain aur us module mein
# getpass --> naam ka ek method hai which hides password while typing.