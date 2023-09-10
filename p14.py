# Python program to read temperature in farenheit and convert into celcius

far = float(input("enter amount in far "))
cel = (far - 32) * 5/9

print("far = ", far)
print("cel = ", cel)

print("far = ", round(far,2))
print("cel = ", round(cel,3), "\u00B0")
